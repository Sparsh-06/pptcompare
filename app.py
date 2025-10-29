from flask import Flask, request, render_template, send_file, Response, jsonify
from werkzeug.utils import secure_filename
from pathlib import Path
import os, uuid, json, threading, time
from compare_pptx_logic import compare_presentations_with_progress

UPLOAD_FOLDER = "uploads"
REPORT_FOLDER = "reports"

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["REPORT_FOLDER"] = REPORT_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

progress_status = {"current": 0, "total": 0, "done": False, "message": ""}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/compare", methods=["POST"])
def compare_files():
    global progress_status
    progress_status = {"current": 0, "total": 0, "done": False, "message": "Starting..."}

    eng_file = request.files.get("english")
    trans_file = request.files.get("translated")
    target_lang = request.form.get("target_lang", "auto")

    if not eng_file or not trans_file:
        return jsonify({"error": "Please upload both files"}), 400

    def save_uploaded(f):
        filename = secure_filename(f.filename)
        token = uuid.uuid4().hex[:8]
        out = Path(app.config["UPLOAD_FOLDER"]) / f"{token}__{filename}"
        f.save(out)
        return out

    eng_path = save_uploaded(eng_file)
    trans_path = save_uploaded(trans_file)
    outdir = Path(app.config["REPORT_FOLDER"]) / uuid.uuid4().hex[:10]
    outdir.mkdir(parents=True, exist_ok=True)

    # Run in a separate thread so frontend stays responsive
    def worker():
        compare_presentations_with_progress(
            eng_path,
            trans_path,
            outdir,
            cache_file=outdir / "cache.json",
            threshold=0.70,
            backtrans_target="en",
            progress=progress_status,
        )

    threading.Thread(target=worker, daemon=True).start()

    return jsonify({"message": "Processing started"})


@app.route("/progress")
def progress():
    def event_stream():
        while not progress_status["done"]:
            data = json.dumps(progress_status)
            yield f"data: {data}\n\n"
            time.sleep(1)
        yield f"data: {json.dumps(progress_status)}\n\n"

    return Response(event_stream(), mimetype="text/event-stream")


@app.route("/report")
def get_report():
    reports = sorted(Path(REPORT_FOLDER).rglob("translation_comparison_report.html"), key=os.path.getmtime)
    if not reports:
        return "No report found", 404
    return send_file(reports[-1], mimetype="text/html")


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV") != "production"
    app.run(host="0.0.0.0", port=port, debug=debug)
