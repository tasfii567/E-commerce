# Deployment Guide — PythonAnywhere (Free, No Card Required)

Your live URL will be: **`https://YOUR_USERNAME.pythonanywhere.com`**

---

## Step 1 — Create a PythonAnywhere account

1. Go to [pythonanywhere.com](https://www.pythonanywhere.com)
2. Click **"Create a Beginner account"** — it's completely free, no card needed
3. Choose a username — this becomes part of your site URL, e.g. `myshop.pythonanywhere.com`

---

## Step 2 — Upload your project

### Option A — From GitHub (recommended)
Push this project to GitHub, then in PythonAnywhere:

1. Go to **Dashboard → Consoles → Bash**
2. Run:
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
```

### Option B — Upload the zip directly
1. Go to **Dashboard → Files**
2. Click **Upload a file** and upload `Ecommerce-pythonanywhere.zip`
3. Open a **Bash console** and run:
```bash
unzip Ecommerce-pythonanywhere.zip
```

---

## Step 3 — Set up a virtual environment and install dependencies

In the Bash console:

```bash
cd Ecommerce-pythonanywhere
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Step 4 — Create the MySQL database

1. Go to **Dashboard → Databases**
2. Set a database password (remember it — you'll need it in Step 6)
3. Click **Create** — PythonAnywhere creates a database named `YOUR_USERNAME$default`
4. Note your database connection details shown on the page:
   - **Host:** `YOUR_USERNAME.mysql.pythonanywhere-services.com`
   - **Username:** `YOUR_USERNAME`
   - **Database name:** `YOUR_USERNAME$default`

---

## Step 5 — Create the Web App

1. Go to **Dashboard → Web → Add a new web app**
2. Click **Next** (keep your free domain)
3. Select **Manual configuration** (NOT "Django" — that's for new projects only)
4. Select **Python 3.10**
5. Click **Next** until done

---

## Step 6 — Configure the Web App

On the Web tab, fill in these fields:

### Source code
```
/home/YOUR_USERNAME/Ecommerce-pythonanywhere
```

### Working directory
```
/home/YOUR_USERNAME/Ecommerce-pythonanywhere
```

### Virtualenv
```
/home/YOUR_USERNAME/Ecommerce-pythonanywhere/venv
```

### Static files
| URL | Directory |
|-----|-----------|
| `/static/` | `/home/YOUR_USERNAME/Ecommerce-pythonanywhere/staticfiles` |

---

## Step 7 — Set environment variables

Still on the Web tab, scroll to **"Environment variables"** and add:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | Any long random string, e.g. `h8k2!x9mq@3rz#7wvp$6nt` |
| `PYTHONANYWHERE_DOMAIN` | `YOUR_USERNAME.pythonanywhere.com` |
| `DATABASE_URL` | `mysql://YOUR_USERNAME:YOUR_DB_PASSWORD@YOUR_USERNAME.mysql.pythonanywhere-services.com/YOUR_USERNAME$default` |
| `EMAIL_HOST_USER` | your Gmail address |
| `EMAIL_HOST_PASSWORD` | your Gmail App Password (see below) |
| `EMAIL_RECEIVING_USER` | email to receive contact form messages |

> **Tip:** For `SECRET_KEY`, go to [djecrety.ir](https://djecrety.ir) to generate one instantly.

---

## Step 8 — Configure the WSGI file

1. On the Web tab, click the **WSGI configuration file** link (looks like `/var/www/YOUR_USERNAME_pythonanywhere_com_wsgi.py`)
2. **Delete everything** in that file
3. **Paste the contents of `pythonanywhere_wsgi.py`** (included in this project)
4. Replace `YOUR_USERNAME` with your actual username
5. Click **Save**

---

## Step 9 — Run migrations and collect static files

Back in the Bash console:

```bash
cd /home/YOUR_USERNAME/Ecommerce-pythonanywhere
source venv/bin/activate

# Set env vars temporarily so manage.py can connect to the database
export DATABASE_URL="mysql://YOUR_USERNAME:YOUR_DB_PASSWORD@YOUR_USERNAME.mysql.pythonanywhere-services.com/YOUR_USERNAME$default"
export SECRET_KEY="your-secret-key-here"
export PYTHONANYWHERE_DOMAIN="YOUR_USERNAME.pythonanywhere.com"

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

---

## Step 10 — Reload and go live!

1. Go back to the **Web tab**
2. Click the big green **Reload** button
3. Visit `https://YOUR_USERNAME.pythonanywhere.com` — your site is live! 🎉

---

## Gmail App Password Setup

Regular Gmail passwords don't work for SMTP. You need an App Password:

1. Go to [myaccount.google.com/security](https://myaccount.google.com/security)
2. Enable **2-Step Verification**
3. Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
4. Create a new App Password → name it anything → copy the 16-character code
5. Use that code as `EMAIL_HOST_PASSWORD`

---

## Updating your site later

Whenever you make changes:

```bash
# In PythonAnywhere Bash console
cd /home/YOUR_USERNAME/Ecommerce-pythonanywhere
git pull   # if using GitHub
source venv/bin/activate
python manage.py migrate          # only if you changed models
python manage.py collectstatic --noinput   # only if you changed static files
```

Then go to Web tab → **Reload**.

---

## Summary of files changed for PythonAnywhere

| File | What changed vs original |
|------|--------------------------|
| `ecommerce/settings.py` | SECRET_KEY, DEBUG, ALLOWED_HOSTS, MySQL DB, email — all from env vars |
| `requirements.txt` | Added `whitenoise`, `dj-database-url`, `mysqlclient`; removed `psycopg2` |
| `pythonanywhere_wsgi.py` | New file — paste into PythonAnywhere's WSGI editor |
| `.gitignore` | Ignores `db.sqlite3`, `.env`, `staticfiles/` |
| `.env.example` | Template for local development |
