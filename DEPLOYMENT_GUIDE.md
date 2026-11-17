# LoanPulse — Complete Cloud Deployment Guide (100% Free)

This guide walks you through taking your **LoanPulse — Loan Management & Risk Assessment System** live on the public internet so anyone can access it from their phone, laptop, or anywhere in the world!

---

## 🌟 The Best & Recommended Architecture (100% Free Tier)

| Component | Platform | Free Features | URL Example |
| :--- | :--- | :--- | :--- |
| **Frontend** (React 19) | **Vercel** or **Netlify** | Free Global CDN, Custom Domain, Automatic HTTPS SSL | `https://loanpulse.vercel.app` |
| **Backend** (Django + ASGI) | **Render** or **Railway** | Free Web Service, Automatic Python Build, WebSockets | `https://loanpulse-api.onrender.com` |
| **Database** | **Render PostgreSQL** / **Supabase** | Free Relational Database (or pre-bundled SQLite) | PostgreSQL Connection URL |

---

## 📋 Step-by-Step Instructions

### Step 1: Push Code to GitHub

1. Go to [GitHub.com](https://github.com) and create a new repository named `loanpulse` (set to **Public** or **Private**).
2. In your VS Code terminal (or project folder), run:
```bash
git init
git add .
git commit -m "feat: complete LoanPulse system ready for production"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/loanpulse.git
git push -u origin main
```

---

### Step 2: Deploy Backend on Render (Free)

1. Go to [Render.com](https://render.com) and sign up / log in with your GitHub account.
2. Click **New +** $\to$ **Web Service**.
3. Select your `loanpulse` GitHub repository.
4. Configure the settings:
   * **Name**: `loanpulse-backend`
   * **Root Directory**: `backend`
   * **Environment**: `Python 3`
   * **Region**: Choose closest (e.g. *Singapore* or *Frankfurt*)
   * **Branch**: `main`
   * **Build Command**:
     ```bash
     pip install -r requirements.txt && python manage.py migrate
     ```
   * **Start Command**:
     ```bash
     daphne -b 0.0.0.0 -p $PORT loanpulse_project.asgi:application
     ```
   * **Instance Type**: **Free**
5. Under **Environment Variables**, add:
   * `SECRET_KEY`: `any-secure-random-string-12345`
   * `DEBUG`: `False`
   * `PYTHON_VERSION`: `3.11.9`
6. Click **Create Web Service**.
7. Once deployed, Render will give you a public URL like:
   👉 `https://loanpulse-backend.onrender.com`

---

### Step 3: Deploy Frontend on Vercel (Free)

1. Go to [Vercel.com](https://vercel.com) and sign up / log in with your GitHub account.
2. Click **Add New...** $\to$ **Project**.
3. Select your `loanpulse` repository and click **Import**.
4. Configure Project:
   * **Framework Preset**: `Vite`
   * **Root Directory**: Click *Edit* and select **`frontend`**
   * **Build Command**: `npm run build`
   * **Output Directory**: `dist`
5. Open **Environment Variables** section and add:
   * **Key**: `VITE_API_BASE`
   * **Value**: `https://loanpulse-backend.onrender.com/api`  *(Your Render URL from Step 2 with /api)*
6. Click **Deploy**.
7. In ~60 seconds, Vercel will launch your live site:
   👉 **`https://loanpulse.vercel.app`** 🎉

---

## ⚡ Instant 2-Minute Demo Live Link (Without Cloud Accounts)

If you just want to generate an instant live public HTTPS link right now to test on your mobile phone or show a friend:

1. In your project, make sure both local servers are running (`run_all.bat` or `Launch_LoanPulse.bat`).
2. Open a new terminal and run:
   ```bash
   npx localtunnel --port 5173
   ```
3. It will give you a live public link instantly:
   👉 `https://your-custom-name.loca.lt`
4. Anyone on the internet can open this link on their mobile device or laptop!

---

## 🔑 Production Demo Login Credentials

Once your live site opens, test using these pre-configured accounts:

| Role | Username | Password |
| :--- | :--- | :--- |
| **Customer** | `customer` | `customer123` |
| **Loan Officer** | `officer` | `officer123` |
| **Risk Manager** | `manager` | `manager123` |
