
PPT Translation Comparator
=========================

How to run (local):
1. Create a virtual environment (recommended):
   python3 -m venv venv
   source venv/bin/activate

2. Install requirements:
   pip install -r requirements.txt

3. Run the Flask app:
   python app.py

4. Open http://127.0.0.1:5000 in your browser, upload the original English PPTX and the translated PPTX, and click Compare.

Notes:
- The app uses deep-translator's GoogleTranslator for back-translation, which uses web requests.
- For hosting, you can use Gunicorn or any WSGI hosting. Make sure to secure the secret key and disable debug mode.
