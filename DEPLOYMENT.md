# PPT Translation Comparator - Deployment Guide

## Quick Docker Commands

### Build the image:
```bash
docker build -t ppt-translation-comparator .
```

### Run locally:
```bash
docker run -d --name ppt-comparator -p 5000:5000 ppt-translation-comparator
```

### Using docker-compose:
```bash
docker-compose up -d
```

## Free Hosting Options

### 1. **Railway** (Recommended - Easiest)
- **Cost**: Free tier with 500 hours/month
- **Setup**: Connect GitHub repo, auto-deploys
- **URL**: https://railway.app
- **Steps**:
  1. Sign up with GitHub
  2. Create new project
  3. Connect your GitHub repository
  4. Railway will auto-detect Dockerfile and deploy
  5. Get a live URL instantly

### 2. **Render**
- **Cost**: Free tier available
- **Setup**: GitHub integration
- **URL**: https://render.com
- **Steps**:
  1. Sign up with GitHub
  2. Create new Web Service
  3. Connect repository
  4. Select "Docker" as environment
  5. Deploy automatically

### 3. **Fly.io**
- **Cost**: Free tier with limitations
- **Setup**: CLI-based deployment
- **URL**: https://fly.io
- **Steps**:
  1. Install flyctl CLI
  2. Run `fly launch` in your project directory
  3. Follow prompts to deploy

### 4. **Heroku** (Container Registry)
- **Cost**: Free tier discontinued, but cheapest paid plans
- **Setup**: Container deployment
- **URL**: https://heroku.com
- **Steps**:
  1. Install Heroku CLI
  2. Login: `heroku login`
  3. Create app: `heroku create your-app-name`
  4. Push container: `heroku container:push web`
  5. Release: `heroku container:release web`

### 5. **DigitalOcean App Platform**
- **Cost**: $5/month minimum
- **Setup**: GitHub integration
- **URL**: https://digitalocean.com
- **Steps**:
  1. Create DigitalOcean account
  2. Go to App Platform
  3. Connect GitHub repository
  4. Select Dockerfile deployment
  5. Deploy

## Environment Variables for Production

Set these environment variables in your hosting platform:

```
FLASK_ENV=production
PORT=5000
```

## Monitoring and Logs

All platforms provide:
- Application logs
- Resource usage monitoring
- Custom domain support (usually paid)
- SSL certificates (usually free)

## Recommended Choice

**Railway** is the easiest option for beginners:
- Free tier is generous
- Automatic HTTPS
- Easy GitHub integration
- Great for small projects
- Simple dashboard

Just push your code to GitHub, connect it to Railway, and you'll have a live URL in minutes!