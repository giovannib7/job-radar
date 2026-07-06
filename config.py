# =============================================================================
# job_radar configuration
# Edit THIS file to add/remove employers, change keywords, and set up email.
# You do not need to touch job_radar.py.
# =============================================================================

# -----------------------------------------------------------------------------
# 1. KEYWORDS  (case-insensitive; substrings count, so "econom" catches
#    economist / economics / econometrics / macroeconomics)
#
#    Each source uses ONE profile:
#      "core"        -> economist-type roles only (institutions, central banks,
#                       tech firms whose boards are mostly engineering).
#      "consultancy" -> also Associate/Consultant/Analyst (at an econ-consulting
#                       firm those ARE the economist roles).
#      "finance"     -> buy/sell-side + rating-agency roles: risk analyst,
#                       fixed-income/rates/macro strategist, quant researcher,
#                       credit analyst, portfolio manager, etc.
#    A job is kept if it matches its profile's INCLUDE list and no EXCLUDE term.
# -----------------------------------------------------------------------------
INCLUDE_CORE = [
    "econom", "monetary", "research economist", "research scientist, econom",
    "policy analyst", "policy economist", "postdoc", "post-doc",
    "research fellow", "quantitative research",
]

INCLUDE_CONSULTANCY = INCLUDE_CORE + [
    "associate", "consultant", "consulting", "principal", "analyst",
    "research assistant",
]

INCLUDE_FINANCE = INCLUDE_CORE + [
    # risk
    "risk analyst", "risk management", "market risk", "credit risk",
    "model risk", "quantitative risk", "risk strategist",
    # strategy / research desks
    "strategist", "macro research", "macro strategist", "rates strategist",
    "investment strategist", "research analyst", "research associate",
    "investment analyst", "investment research",
    # fixed income & rates
    "fixed income", "fixed-income", "rates", "interest rate", "sovereign",
    "credit analyst", "credit research", "structured finance", "securitization",
    "ratings analyst", "rating analyst",
    # quant / portfolio
    "quant research", "quantitative research", "quantitative analyst",
    "quantitative researcher", "quantitative trader", "quantitative strategies",
    "portfolio manager", "portfolio analyst", "asset allocation", "multi-asset",
    "financial economist",
]

EXCLUDE = [
    "intern", "internship", "student", "co-op", "apprentice",
    "administrative assistant", "executive assistant", "receptionist",
    "recruiter", "talent acquisition", "sales", "graphic designer",
    "software engineer", "quantitative developer", "help desk",
    "custodian", "cleaner",
]

# Order in which category sections appear on the dashboard.
CATEGORY_ORDER = [
    "International institutions",
    "Central banks",
    "Rating agencies",
    "Economic consultancies",
    "Buy-side / trading",
    "Sell-side / banks",
    "Private sector / tech",
    "Aggregators (catch-all)",
]

# -----------------------------------------------------------------------------
# 2. SOURCES
#    "type": greenhouse | smartrecruiters | lever | workday | link
#    "profile": "core" (default) | "consultancy" | "finance"
#    "category": one of CATEGORY_ORDER above (groups the dashboard)
#      greenhouse/smartrecruiters/lever -> need "slug"
#      workday   -> need "host","tenant","site"  (deadlines auto-fetched)
#      link      -> no API; a bookmark you open manually ("url")
# -----------------------------------------------------------------------------
SOURCES = [
    # ===================== International institutions ========================
    {"name": "IMF", "category": "International institutions", "type": "workday",
     "host": "imf.wd5.myworkdayjobs.com", "tenant": "imf", "site": "IMF"},
    {"name": "OECD", "category": "International institutions",
     "type": "smartrecruiters", "slug": "OECD"},

    # ===================== Central banks (clean APIs) =======================
    {"name": "Federal Reserve System (12 banks)", "category": "Central banks",
     "type": "workday", "host": "rb.wd5.myworkdayjobs.com",
     "tenant": "rb", "site": "FRS"},
    {"name": "Reserve Bank of Australia", "category": "Central banks",
     "type": "workday", "host": "rba.wd105.myworkdayjobs.com",
     "tenant": "rba", "site": "RBA_Careers"},

    # ===================== Rating agencies ==================================
    {"name": "S&P Global", "category": "Rating agencies", "type": "workday",
     "profile": "finance", "host": "spgi.wd5.myworkdayjobs.com",
     "tenant": "spgi", "site": "SPGI_Careers"},

    # ===================== Economic consultancies ===========================
    {"name": "Charles River Associates", "category": "Economic consultancies",
     "type": "greenhouse", "slug": "charlesriverassociates", "profile": "consultancy"},
    {"name": "Brattle Group", "category": "Economic consultancies",
     "type": "greenhouse", "slug": "thebrattlegroup", "profile": "consultancy"},
    {"name": "Keystone Strategy", "category": "Economic consultancies",
     "type": "greenhouse", "slug": "keystonestrategy", "profile": "consultancy"},

    # ===================== Buy-side / trading (finance profile) =============
    {"name": "AQR Capital", "category": "Buy-side / trading",
     "type": "greenhouse", "slug": "aqr", "profile": "finance"},
    {"name": "Point72", "category": "Buy-side / trading",
     "type": "greenhouse", "slug": "point72", "profile": "finance"},
    {"name": "Man Group", "category": "Buy-side / trading",
     "type": "greenhouse", "slug": "mangroup", "profile": "finance"},
    {"name": "Marshall Wace", "category": "Buy-side / trading",
     "type": "greenhouse", "slug": "marshallwace", "profile": "finance"},
    {"name": "Jane Street", "category": "Buy-side / trading",
     "type": "greenhouse", "slug": "janestreet", "profile": "finance"},
    {"name": "DRW", "category": "Buy-side / trading",
     "type": "greenhouse", "slug": "drweng", "profile": "finance"},
    {"name": "IMC Trading", "category": "Buy-side / trading",
     "type": "greenhouse", "slug": "imc", "profile": "finance"},
    {"name": "Jump Trading", "category": "Buy-side / trading",
     "type": "greenhouse", "slug": "jumptrading", "profile": "finance"},
    {"name": "Virtu Financial", "category": "Buy-side / trading",
     "type": "greenhouse", "slug": "virtu", "profile": "finance"},
    {"name": "Flow Traders", "category": "Buy-side / trading",
     "type": "greenhouse", "slug": "flowtraders", "profile": "finance"},

    # ===================== Private sector / tech (econ teams) ================
    {"name": "Airbnb",    "category": "Private sector / tech", "type": "greenhouse", "slug": "airbnb"},
    {"name": "Lyft",      "category": "Private sector / tech", "type": "greenhouse", "slug": "lyft"},
    {"name": "Instacart", "category": "Private sector / tech", "type": "greenhouse", "slug": "instacart"},
    {"name": "Pinterest", "category": "Private sector / tech", "type": "greenhouse", "slug": "pinterest"},
    {"name": "Stripe",    "category": "Private sector / tech", "type": "greenhouse", "slug": "stripe"},
    {"name": "Block",     "category": "Private sector / tech", "type": "greenhouse", "slug": "block"},
    {"name": "Roblox",    "category": "Private sector / tech", "type": "greenhouse", "slug": "roblox"},
    {"name": "Spotify",   "category": "Private sector / tech", "type": "lever", "slug": "spotify"},

    # =======================================================================
    #  BOOKMARKS — no open/permitted API, so opened manually. Grouped by the
    #  same categories on the dashboard.
    # =======================================================================
    # --- Aggregators (carry hundreds of employers each) ---------------------
    {"name": "AEA JOE — Job Openings for Economists (THE catch-all)",
     "category": "Aggregators (catch-all)", "type": "link",
     "url": "https://www.aeaweb.org/joe/listings"},
    {"name": "eFinancialCareers (buy/sell-side)", "category": "Aggregators (catch-all)",
     "type": "link", "url": "https://www.efinancialcareers.com/jobs-Economist"},
    {"name": "EconJobMarket", "category": "Aggregators (catch-all)",
     "type": "link", "url": "https://econjobmarket.org/positions"},
    {"name": "INOMICS economist jobs", "category": "Aggregators (catch-all)",
     "type": "link", "url": "https://inomics.com/jobs"},
    {"name": "Fed Econ Jobs (all Fed economist roles)",
     "category": "Aggregators (catch-all)", "type": "link",
     "url": "https://www.fedeconjobs.org/"},
    {"name": "LinkedIn: economist, senior level", "category": "Aggregators (catch-all)",
     "type": "link", "url": "https://www.linkedin.com/jobs/search/?keywords=economist&f_E=4&sortBy=DD"},

    # --- Central banks ------------------------------------------------------
    {"name": "ECB", "category": "Central banks", "type": "link",
     "url": "https://talent.ecb.europa.eu/careers"},
    {"name": "Bank of England", "category": "Central banks", "type": "link",
     "url": "https://www.bankofengland.co.uk/careers/current-vacancies"},
    {"name": "Bank of Canada", "category": "Central banks", "type": "link",
     "url": "https://www.bankofcanada.ca/careers/find-job/"},
    {"name": "BIS", "category": "Central banks", "type": "link",
     "url": "https://www.bis.org/careers/vacancies.htm"},
    {"name": "Federal Reserve Board of Governors", "category": "Central banks",
     "type": "link",
     "url": "https://frbog.taleo.net/careersection/frs_external_career_section/jobsearch.ftl"},
    # --- European central banks (no open API — direct careers pages) --------
    {"name": "Deutsche Bundesbank", "category": "Central banks", "type": "link",
     "url": "https://www.bundesbank.de/en/bundesbank/career"},
    {"name": "Banque de France", "category": "Central banks", "type": "link",
     "url": "https://www.banque-france.fr/en/banque-de-france/careers"},
    {"name": "Banca d'Italia", "category": "Central banks", "type": "link",
     "url": "https://www.bancaditalia.it/chi-siamo/lavora-con-noi/index.html?com.dotmarketing.htmlpage.language=1"},
    {"name": "Banco de España", "category": "Central banks", "type": "link",
     "url": "https://www.bde.es/wbe/en/sobre-banco/trabaja-nosotros/"},
    {"name": "De Nederlandsche Bank", "category": "Central banks", "type": "link",
     "url": "https://www.dnb.nl/en/careers/"},
    {"name": "Sveriges Riksbank", "category": "Central banks", "type": "link",
     "url": "https://www.riksbank.se/en-gb/about-the-riksbank/work-at-the-riksbank/vacancies/"},
    {"name": "Norges Bank", "category": "Central banks", "type": "link",
     "url": "https://www.norges-bank.no/en/topics/about/Vacancies/"},
    {"name": "Swiss National Bank (SNB)", "category": "Central banks", "type": "link",
     "url": "https://www.snb.ch/en/the-snb/career"},
    {"name": "Bank of Finland", "category": "Central banks", "type": "link",
     "url": "https://www.suomenpankki.fi/en/bank-of-finland/open-positions/"},
    {"name": "Central Bank of Ireland", "category": "Central banks", "type": "link",
     "url": "https://www.centralbank.ie/careers/search-careers"},
    {"name": "National Bank of Belgium", "category": "Central banks", "type": "link",
     "url": "https://www.nbb.be/en/jobs"},
    {"name": "Banco de Portugal", "category": "Central banks", "type": "link",
     "url": "https://www.bportugal.pt/en/page/recruitment"},
    {"name": "Oesterreichische Nationalbank (OeNB)", "category": "Central banks",
     "type": "link", "url": "https://www.oenb.at/en/About-Us/Career.html"},
    {"name": "Bank of Greece", "category": "Central banks", "type": "link",
     "url": "https://www.bankofgreece.gr/en/the-bank/job-opportunities"},
    {"name": "Narodowy Bank Polski (NBP)", "category": "Central banks", "type": "link",
     "url": "https://nbp.pl/en/about-us/careers/"},
    {"name": "Czech National Bank (CNB)", "category": "Central banks", "type": "link",
     "url": "https://www.cnb.cz/en/about_cnb/career/"},
    {"name": "Magyar Nemzeti Bank (MNB)", "category": "Central banks", "type": "link",
     "url": "https://www.mnb.hu/en/careers"},
    {"name": "INOMICS: central bank economist jobs (live listings)",
     "category": "Central banks", "type": "link",
     "url": "https://inomics.com/jobs?keywords=central%20bank"},

    # --- Rating agencies ----------------------------------------------------
    {"name": "Moody's", "category": "Rating agencies", "type": "link",
     "url": "https://careers.moodys.com/jobs"},
    {"name": "Fitch Ratings", "category": "Rating agencies", "type": "link",
     "url": "https://www.fitch.group/careers"},
    {"name": "Morningstar / DBRS", "category": "Rating agencies", "type": "link",
     "url": "https://careers.morningstar.com/us/en/search-results"},

    # --- Buy-side / asset managers ------------------------------------------
    {"name": "BlackRock", "category": "Buy-side / trading", "type": "link",
     "url": "https://careers.blackrock.com/search-jobs/"},
    {"name": "PIMCO", "category": "Buy-side / trading", "type": "link",
     "url": "https://www.pimco.com/en-us/our-firm/careers/job-search"},
    {"name": "Vanguard", "category": "Buy-side / trading", "type": "link",
     "url": "https://www.vanguardjobs.com/job-search-results/"},
    {"name": "Fidelity", "category": "Buy-side / trading", "type": "link",
     "url": "https://jobs.fidelity.com/search-jobs"},
    {"name": "Citadel", "category": "Buy-side / trading", "type": "link",
     "url": "https://www.citadel.com/careers/open-opportunities/"},
    {"name": "Two Sigma", "category": "Buy-side / trading", "type": "link",
     "url": "https://careers.twosigma.com/careers/OpenRoles"},
    {"name": "Bridgewater Associates", "category": "Buy-side / trading", "type": "link",
     "url": "https://www.bridgewater.com/working-at-bridgewater/career-openings"},
    {"name": "Millennium", "category": "Buy-side / trading", "type": "link",
     "url": "https://careers.mlp.com/job-search"},
    {"name": "Norges Bank Investment Management (oil fund)",
     "category": "Buy-side / trading", "type": "link",
     "url": "https://www.nbim.no/en/organisation/careers/available-positions/"},

    # --- Sell-side / banks --------------------------------------------------
    {"name": "Goldman Sachs", "category": "Sell-side / banks", "type": "link",
     "url": "https://www.goldmansachs.com/careers/our-firm/professionals/"},
    {"name": "J.P. Morgan", "category": "Sell-side / banks", "type": "link",
     "url": "https://careers.jpmorgan.com/global/en/students/programs?search=economist"},
    {"name": "Morgan Stanley", "category": "Sell-side / banks", "type": "link",
     "url": "https://www.morganstanley.com/careers/career-opportunities-search"},
    {"name": "Citi", "category": "Sell-side / banks", "type": "link",
     "url": "https://jobs.citi.com/search-jobs/economist"},
    {"name": "Barclays", "category": "Sell-side / banks", "type": "link",
     "url": "https://search.jobs.barclays/search-jobs/economist"},
    {"name": "UBS", "category": "Sell-side / banks", "type": "link",
     "url": "https://jobs.ubs.com/search"},
    {"name": "Deutsche Bank", "category": "Sell-side / banks", "type": "link",
     "url": "https://careers.db.com/professionals/search-roles/"},

    # --- Economic consultancies (manual) ------------------------------------
    {"name": "NERA Economic Consulting", "category": "Economic consultancies",
     "type": "link", "url": "https://www.nera.com/careers/find-a-role.html"},
    {"name": "Analysis Group", "category": "Economic consultancies",
     "type": "link", "url": "https://www.analysisgroup.com/careers/open-positions/"},
    {"name": "Cornerstone Research", "category": "Economic consultancies",
     "type": "link", "url": "https://www.cornerstone.com/careers/open-positions/"},
    {"name": "Compass Lexecon", "category": "Economic consultancies",
     "type": "link", "url": "https://www.compasslexecon.com/careers/open-positions/"},

    # --- Private sector -----------------------------------------------------
    {"name": "Amazon Economists", "category": "Private sector / tech",
     "type": "link", "url": "https://www.amazon.jobs/en/teams/economics"},
]

# -----------------------------------------------------------------------------
# 3. EMAIL  (optional — leave ENABLED=False for HTML dashboard only)
# -----------------------------------------------------------------------------
EMAIL = {
    "ENABLED": True,
    "SMTP_HOST": "smtp.gmail.com",
    "SMTP_PORT": 587,
    "FROM": "giovanni.borraccia7@gmail.com",
    # TO can be ONE address or several separated by commas (to share the digest):
    #   "TO": "giovanni.borraccia7@gmail.com, friend@example.com",
    "TO": "giovanni.borraccia7@gmail.com",
    # The password is NOT stored here anymore. In the cloud it comes from the
    # GitHub secret JOBRADAR_APP_PW; to test locally, run:
    #   JOBRADAR_APP_PW=yourapppassword python3 job_radar.py
    "APP_PASSWORD": "",
    "ONLY_WHEN_NEW": False,   # False = email daily even if nothing new, so the
                              # recipient always gets the full current dashboard
    "ATTACH_DASHBOARD": True, # attach the whole jobs.html (full listing) to the email
}
