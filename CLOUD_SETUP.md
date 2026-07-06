# Move Job Radar to the cloud (email even when your Mac is off)

Follow these once. After that it runs by itself every day on GitHub's servers:
it emails your gmail AND publishes the dashboard at a public link you can share.

Your app password (the 16-character Gmail code) is typed straight into GitHub in
Step 4 — it is never written into any file, so nothing sensitive gets uploaded.

---

## 1. Make a free GitHub account
Go to https://github.com/signup and sign up (free). Verify your email.

## 2. Create a repository
- Go to https://github.com/new
- **Repository name:** `job-radar`
- **Visibility:** Private
- Do **not** tick "Add a README".
- Click **Create repository**.

## 3. Upload the tool's files
On the new empty repo page, click the link **"uploading an existing file"**.
- Open the `job_radar` folder on your Mac.
- Select and drag these files into the browser:
  `job_radar.py`, `config.py`, `requirements.txt`, `seen_jobs.csv`,
  `jobs.html`, `README.md`, `.gitignore`
- Click **Commit changes**.

Now add the workflow file (the daily scheduler). GitHub hides folders that start
with a dot, so create it by hand:
- Click **Add file → Create new file**.
- In the filename box type exactly:  `.github/workflows/job_radar.yml`
  (typing the slashes creates the folders automatically)
- Paste in the contents of the file `.github/workflows/job_radar.yml` from your
  `job_radar` folder (open it in a text editor and copy everything).
- Click **Commit changes**.

## 4. Add your Gmail app password as a secret
- In the repo: **Settings → Secrets and variables → Actions**.
- Click **New repository secret**.
- **Name:** `JOBRADAR_APP_PW`
- **Secret:** paste your 16-character Gmail app password (no spaces).
- Click **Add secret**.

## 5. Turn on the public dashboard page
- In the repo: **Settings → Pages**.
- Under **Build and deployment → Source**, choose **GitHub Actions**.

## 6. Run it once to test
- Go to the **Actions** tab. If it asks, click to enable workflows.
- Click **Job Radar** on the left, then **Run workflow → Run workflow**.
- Wait 1–2 minutes. Two things should happen:
  1. An email arrives at **giovanni.borraccia7@gmail.com** (check spam the first time).
  2. Click into the finished run — it shows a **github-pages** link like
     `https://<your-username>.github.io/job-radar/`. **That is your shareable
     dashboard URL** — send it to anyone; it refreshes itself every day.

## Done
From now on it runs automatically every morning (~08:00 Geneva), whether your
computer is on or off. To change the time, edit the `cron:` line in
`.github/workflows/job_radar.yml`. To add employers or recipients, edit
`config.py` in the repo (GitHub lets you edit files in the browser).

## Notes
- To share the digest with someone, edit `TO` in `config.py` (comma-separated).
- The local 8am scheduler on your Mac is now redundant; you can ignore it or
  I can remove it.
