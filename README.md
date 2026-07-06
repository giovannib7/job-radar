# Job Radar

A small personal tool that checks employers once a day for economics-PhD-level
openings, flags anything **new** since the last check, writes an HTML dashboard,
and (optionally) emails you a digest.

## Files
- `config.py` — the only file you edit: employers, keywords, email settings.
- `job_radar.py` — the program (fetch → filter → dedup → dashboard → email).
- `jobs.html` — the dashboard. **Double-click to open it in your browser.**
- `seen_jobs.csv` — memory of everything seen so far (so "new" means new).
- `run.sh`, `com.giovanni.jobradar.plist` — the daily auto-scheduler.
- `run.log` — what happened on each daily run.

## How the daily schedule works
A macOS **launchd** agent runs `run.sh` every day at **08:00**
(if the Mac is asleep, it runs at the next wake). It is already installed.

Useful commands (paste into Terminal):
```bash
# run it right now instead of waiting for 8am:
launchctl start com.giovanni.jobradar

# turn it off / on:
launchctl unload ~/Library/LaunchAgents/com.giovanni.jobradar.plist
launchctl load   ~/Library/LaunchAgents/com.giovanni.jobradar.plist

# change the time: edit Hour/Minute in the .plist, copy it over, reload:
cp "com.giovanni.jobradar.plist" ~/Library/LaunchAgents/ && \
launchctl unload ~/Library/LaunchAgents/com.giovanni.jobradar.plist && \
launchctl load   ~/Library/LaunchAgents/com.giovanni.jobradar.plist
```

## Run it manually any time
```bash
/Users/giovanniborraccia/anaconda3/bin/python3 job_radar.py
```

## Add an employer
Open `config.py`, add one line to `SOURCES`. Most firms use Greenhouse or Lever;
find the slug in their job-page URL (e.g. `boards.greenhouse.io/<slug>`), then:
```python
{"name": "Some Firm", "type": "greenhouse", "slug": "somefirm"},
```
Supported types: `greenhouse`, `smartrecruiters`, `lever`, `workday`, and
`link` (a manual bookmark for sites with no open API).

## Turn on email
In `config.py`, set `EMAIL["ENABLED"] = True`, then create a Google **App
Password** (Google Account → Security → App passwords — your normal password
will not work) and paste it into `EMAIL["APP_PASSWORD"]`. Set `FROM` to that
Gmail address. If the Graduate Institute account blocks app passwords, use a
personal Gmail as the sender; it can still send to your institute address.

## What is covered now
The dashboard is grouped into clearly separated **category sections**, each with
a live count and a **Deadline** column.

**Auto-fetched (live APIs, checked daily):**
- International institutions: **IMF**, **OECD**.
- Central banks: **Federal Reserve System (all 12 regional banks)**, **RBA**.
- Rating agencies: **S&P Global**.
- Economic consultancies: **Charles River Associates**, **Brattle Group**,
  **Keystone Strategy**.
- Buy-side / trading: **AQR, Point72, Man Group, Marshall Wace, Jane Street,
  DRW, IMC, Jump Trading, Virtu, Flow Traders** (matches risk analyst,
  fixed-income/rates/macro strategist, quant researcher, credit analyst,
  portfolio manager, etc.).
- Private sector / tech (economist roles only): **Airbnb, Lyft, Instacart,
  Pinterest, Stripe, Block, Roblox, Spotify**.

**Bookmarks (opened manually from the dashboard, grouped by the same categories):**
- Aggregators — **AEA JOE, eFinancialCareers, EconJobMarket, INOMICS,
  Fed Econ Jobs, LinkedIn**.
- Central banks — **ECB, Bank of England, Bank of Canada, BIS, Fed Board**.
- Rating agencies — **Moody's, Fitch, Morningstar/DBRS**.
- Buy-side / asset managers — **BlackRock, PIMCO, Vanguard, Fidelity, Citadel,
  Two Sigma, Bridgewater, Millennium**.
- Sell-side / banks — **Goldman Sachs, J.P. Morgan, Morgan Stanley, Citi,
  Barclays, UBS, Deutsche Bank**.
- Economic consultancies — **NERA, Analysis Group, Cornerstone Research,
  Compass Lexecon**.
- Private sector — **Amazon Economists**.

## About deadlines
Workday-based employers (IMF, the Fed, RBA, S&P Global) publish an application
close date, which the tool fetches and shows. But **most professional and
research roles have no published deadline** — they are open until filled — so
those rows read *"rolling / see posting."* That is the real state of the data;
the column fills in whenever an employer actually sets a closing date.

## Keyword profiles (in config.py)
- **core** — economist roles only (institutions, central banks, tech).
- **consultancy** — also Associate/Consultant/Analyst (econ-consulting firms).
- **finance** — risk/strategist/quant/credit/portfolio roles (buy/sell-side,
  rating agencies).
Each source picks one profile; edit the INCLUDE_* lists to tune matching.

## Honest limits (why "everything" is a bookmark, not an API)
No tool can auto-fetch the *entire* private sector or *all ~190* central banks:
most run on token-locked systems (Cornerstone, SuccessFactors) or bespoke pages
with no open API, and **AEA JOE / EconJobMarket forbid scraping** in their terms.
The auto-fetched list above is everything with a clean, permitted JSON API; the
**aggregator bookmarks (JOE especially) are the real catch-all** — check them to
cover anything the APIs miss. Add more direct-API employers any time via
`config.py` (find a firm's Greenhouse/Lever slug in its job-page URL).

## A note on the Federal Reserve fetch
Workday (the Fed's system) throttles rapid page requests and will silently
return short results if hit too fast. The fetcher paces itself and retries, so a
normal once-a-day run gets the full list; if you run it many times in quick
succession you may temporarily see fewer Fed roles until the throttle resets.
