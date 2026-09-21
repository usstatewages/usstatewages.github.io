"""
Static pages required for AdSense review (privacy policy / about / contact), plus shared
theme parts (style/header/footer/GA+AdSense snippet), mirroring the us-paycheck-calculator /
krcalctools project structure (see site-deployment-handoff.md).

GA4 is wired in (property "usstatewages" under the same GA account as the other sites,
measurement ID G-RGNKRT8FK4). AdSense is wired in too - same publisher account as
uspaycheckcalc/krcalctools (AdSense ca-pub- IDs are per-publisher, not per-site; this site
was added as a new site under the existing account, no new registration needed). Site is
pending AdSense's review after the code snippet went live.
"""

import html
import json

SITE_NAME = "US State Minimum Wage Tracker"
CONTACT_EMAIL = "usstatewages@gmail.com"
BASE_URL = "https://usstatewages.github.io"

ADSENSE_CLIENT = "ca-pub-5607384951754093"

GA_SNIPPET = f"""<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-RGNKRT8FK4"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-RGNKRT8FK4');
</script>
<!-- Google AdSense -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT}"
     crossorigin="anonymous"></script>"""


def page_url(filename):
    """The home page is canonical at the root URL, not /index.html (avoids a duplicate URL)."""
    return f"{BASE_URL}/" if filename == "index.html" else f"{BASE_URL}/{filename}"


def seo_meta(filename, title, desc, json_ld=None):
    """canonical + Open Graph/Twitter preview tags, plus optional JSON-LD structured data."""
    url = page_url(filename)
    t, d = html.escape(title), html.escape(desc)
    tags = f"""<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_US">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary">"""
    for block in json_ld or []:
        tags += f'\n<script type="application/ld+json">{json.dumps(block, ensure_ascii=False)}</script>'
    return tags


FOOTER_NAV = """
  <div class="footer-nav">
    <a href="index.html">Home</a>
    <a href="about.html">About</a>
    <a href="privacy.html">Privacy Policy</a>
    <a href="contact.html">Contact</a>
  </div>
"""

FAVICON = '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 100 100%27%3E%3Ctext y=%27.9em%27 font-size=%2790%27%3E%F0%9F%93%8A%3C/text%3E%3C/svg%3E">'

SITE_HEADER = """
  <header class="site-header">
    <a href="index.html" class="brand">\U0001F4CA US State Minimum Wage Tracker</a>
    <nav class="site-nav">
      <a href="index.html">Home</a>
      <a href="about.html">About</a>
    </nav>
  </header>
"""

SITE_STYLE = """
  :root {
    --primary: #2563eb; --primary-dark: #1d4ed8; --bg: #f8f9fc; --card-bg: #ffffff;
    --text: #111827; --muted: #6b7280; --border: #e5e7eb;
    --warn-bg: #fff7ed; --warn-text: #9a3412;
  }
  * { box-sizing: border-box; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    max-width: 680px; margin: 0 auto; padding: 0 20px 60px; color: var(--text);
    line-height: 1.7; background: var(--bg);
  }
  a { color: var(--primary); }
  .site-header {
    display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap;
    gap: 10px; padding: 18px 0; border-bottom: 1px solid var(--border); margin-bottom: 28px;
  }
  .site-header .brand { font-weight: 800; font-size: 17px; color: var(--text); text-decoration: none; }
  .site-nav { display: flex; gap: 2px; flex-wrap: wrap; }
  .site-nav a { font-size: 13px; color: var(--muted); text-decoration: none; padding: 6px 10px; border-radius: 999px; }
  .site-nav a:hover { background: #eef2ff; color: var(--primary); }

  h1 { font-size: 23px; margin-bottom: 8px; }
  h2 { font-size: 16px; margin-top: 28px; }

  .headline {
    background: linear-gradient(135deg,#eef2ff,#f5f3ff); border-radius: 16px;
    padding: 26px; text-align: center; margin: 20px 0;
  }
  .headline .amount { font-size: 34px; font-weight: 800; color: var(--primary); }
  .headline .pending { font-size: 22px; font-weight: 800; color: var(--warn-text); }

  .badge { display: inline-block; font-size: 12px; font-weight: 700; padding: 3px 10px; border-radius: 999px; }
  .badge.confirmed { background: #dcfce7; color: #166534; }
  .badge.pending { background: var(--warn-bg); color: var(--warn-text); }

  .us-map-wrap { margin: 20px 0; }
  .us-map { width: 100%; height: auto; display: block; }
  .us-map a rect { transition: opacity 0.15s; }
  .us-map a:hover rect { opacity: 0.8; }
  .map-legend {
    display: flex; flex-wrap: wrap; gap: 6px 16px; margin-top: 10px;
    font-size: 12px; color: var(--muted);
  }
  .map-legend span { display: inline-flex; align-items: center; gap: 6px; }
  .map-swatch { width: 11px; height: 11px; border-radius: 3px; display: inline-block; }

  table.rule, table { width: 100%; border-collapse: collapse; margin: 14px 0; font-size: 13px; }
  table.rule th, table.rule td, table th, table td { border: 1px solid var(--border); padding: 9px 10px; text-align: left; }
  table.rule td.num, table td.num { text-align: right; }
  th { color: var(--muted); font-weight: 600; background: #fafafa; }

  .source { font-size: 12px; color: var(--muted); }
  .source a { color: var(--muted); }
  .disclaimer {
    margin-top: 32px; padding: 14px 16px; background: #fafafa; border-radius: 10px;
    font-size: 12px; color: var(--muted); line-height: 1.6;
  }

  .explain { margin-top: 26px; font-size: 14px; color: #374151; }
  .explain h2 { font-size: 15px; }
  .steps { margin: 12px 0 0; padding-left: 20px; }
  .steps li { margin-bottom: 8px; }

  .history-chart { margin: 14px 0; }
  .history-row { display: flex; align-items: center; gap: 10px; padding: 5px 0; font-size: 13px; }
  .history-year { width: 36px; color: var(--muted); flex-shrink: 0; }
  .history-bar-track { flex: 1; background: #eef0f4; border-radius: 6px; height: 16px; overflow: hidden; }
  .history-bar { background: var(--primary); height: 100%; border-radius: 6px; opacity: 0.55; }
  .history-row.current .history-bar { opacity: 1; }
  .history-value { width: 56px; text-align: right; flex-shrink: 0; }
  .history-row.current .history-value { font-weight: 700; color: var(--primary); }

  .faq { margin-top: 26px; }
  .faq h2 { font-size: 15px; margin-bottom: 10px; }
  .faq details {
    border: 1px solid var(--border); border-radius: 10px; padding: 12px 16px;
    margin-bottom: 8px; background: var(--card-bg);
  }
  .faq summary { cursor: pointer; font-weight: 600; font-size: 14px; }
  .faq details p { margin: 10px 0 0; font-size: 13px; color: #374151; line-height: 1.6; }

  .nav { margin-top: 24px; font-size: 14px; }
  .nav a { text-decoration: none; }

  .division-list { list-style: none; padding: 0; margin: 18px 0; display: grid; gap: 8px; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); }
  .division-list li a {
    display: block; padding: 12px 16px; background: var(--card-bg); border: 1px solid var(--border);
    border-radius: 10px; text-decoration: none; color: var(--text); font-size: 14px; text-align: center;
  }
  .division-list li a:hover { border-color: var(--primary); color: var(--primary); }

  .updated { font-size: 12px; color: var(--muted); margin: 0 0 14px; }
  .news-list { list-style: none; padding: 0; margin: 10px 0 18px; font-size: 14px; }
  .news-list li { padding: 7px 0; border-bottom: 1px solid var(--border); }
  .news-date { display: inline-block; min-width: 92px; color: var(--muted); font-size: 12px; }
  .division-list li a small { display: block; color: var(--muted); font-size: 12px; }

  .footer-nav {
    margin-top: 40px; padding-top: 18px; border-top: 1px solid var(--border);
    font-size: 13px; color: var(--muted); display: flex; flex-wrap: wrap; gap: 4px 14px;
  }
  .footer-nav a { color: var(--muted); text-decoration: none; }
  .footer-nav a:hover { color: var(--primary); }
"""


def page_shell(title, description, body, extra_head="", filename=None, json_ld=None):
    """filename: the page's output file - adds canonical/OG tags pointing at its public URL."""
    seo = seo_meta(filename, title, description, json_ld) if filename else ""
    return f"""<!doctype html>
<html lang="en">
<head>
{GA_SNIPPET}
<meta charset="utf-8">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<meta name="viewport" content="width=device-width, initial-scale=1">
{FAVICON}
{seo}
{extra_head}
<style>{SITE_STYLE}</style>
</head>
<body>
{SITE_HEADER}
{body}
{FOOTER_NAV}
</body>
</html>"""


def about_html():
    return page_shell(
        f"About - {SITE_NAME}",
        f"{SITE_NAME} tracks confirmed and expected state minimum wage increases across the US.",
        f"""
  <h1>About This Site</h1>
  <p>{SITE_NAME} tracks state minimum wage increases as they're legislated, calculated, and
  officially announced - starting with the wave of increases taking effect January 1, 2027.</p>

  <h2>Confirmed vs. pending</h2>
  <p>Some states have already published or legislated an exact 2027 dollar figure. Many others
  raise their minimum wage every January 1 through an automatic inflation or formula adjustment,
  but don't calculate and publish the exact new number until later in the year (typically
  September through December). This site labels each state <span class="badge confirmed">confirmed</span>
  once a real figure is published, and <span class="badge pending">pending</span> until then -
  we don't publish estimated or guessed dollar amounts.</p>

  <h2>Sources</h2>
  <p>Baseline current-year rates are cross-checked against the U.S. Department of Labor's official
  state minimum wage table. Confirmed 2027 figures are sourced to the relevant state agency or
  legislation. Each page links its source.</p>

  <h2>Need an exact number for payroll?</h2>
  <p>This site is for general information and planning purposes only. For payroll compliance,
  confirm the exact current rate with your state's labor department or a licensed professional.</p>
""",
        filename="about.html",
    )


def privacy_html():
    return page_shell(
        f"Privacy Policy - {SITE_NAME}",
        f"Privacy policy for {SITE_NAME}.",
        f"""
  <h1>Privacy Policy</h1>
  <p>{SITE_NAME} ("the site") respects your privacy. This policy explains what information is
  collected when you visit.</p>

  <h2>1. Information We Collect</h2>
  <p>This site has no account system or login and does not collect any personal information that
  you submit through a form. Third-party services such as Google AdSense and Google Analytics may
  automatically collect cookie-based data (pages visited, device type, approximate location) for
  advertising and analytics purposes.</p>

  <h2>2. Cookies</h2>
  <p>This site uses cookies served by Google and its partners to serve ads. You can opt out of
  personalized advertising via <a href="https://adssettings.google.com" target="_blank" rel="noopener">Google Ads Settings</a>,
  or block cookies entirely in your browser settings.</p>

  <h2>3. Third-Party Advertising</h2>
  <p>This site displays ads served by Google AdSense. Google may use cookies to serve ads based on
  your prior visits to this or other websites. See Google's advertising policies for details.</p>

  <h2>4. Contact</h2>
  <p>Questions about this privacy policy can be sent to <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.</p>

  <h2>5. Effective Date</h2>
  <p>This policy is effective as of August 22, 2026.</p>
""",
        filename="privacy.html",
    )


def contact_html():
    return page_shell(
        f"Contact - {SITE_NAME}",
        f"Contact page for {SITE_NAME}.",
        f"""
  <h1>Contact</h1>
  <p>Questions, corrections, or advertising/partnership inquiries can be sent to the email below.</p>
  <p><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></p>
""",
        filename="contact.html",
    )
