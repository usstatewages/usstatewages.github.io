"""
Generates all pages for the US State Minimum Wage Tracker site:
  - index.html                      hub: table of every tracked state's Jan 1, 2027 status
  - {state}-minimum-wage.html       per-state detail page
  - {state}-minimum-wage-2027.html  redirect stub for each launch-era URL (Aug 2026)

Detail URLs are evergreen (no year): the year lives in the title and content, so next cycle's
update keeps the same URL and whatever ranking it has built. The old "-2027" URLs were never
indexed, but they stay as instant redirects in case anyone linked them.

Scope: states with a January-1-cycle minimum wage law (legislated step or inflation/formula
index) that make a 2027 increase highly likely. See minwage_data.py for sourcing and the states
deliberately left out. "confirmed" states show a real 2027 number; "pending" states show the
mechanism and an honest "not yet announced" status - never a guessed number.
"""
import os
from datetime import date

from minwage_data import (STATES, STATE_ORDER, FULL_TIME_HOURS, HISTORY, HISTORY_CHART_MAX,
                          MAP_STATES, DATA_CHECKED)
from static_pages import (about_html, privacy_html, contact_html, SITE_NAME, BASE_URL,
                          page_shell, page_url)

OUTPUT_DIR = "docs"

EFFECTIVE_DATE = "January 1, 2027"


def fmt_money(n):
    return f"${n:,.2f}"


def fmt_annual(n):
    return f"${n:,.0f}"


def fmt_date(iso, short=False):
    d = date.fromisoformat(iso)
    return f"{d.strftime('%b' if short else '%B')} {d.day}, {d.year}"


def detail_slug(state_key):
    return f"{state_key}-minimum-wage.html"


def legacy_slug(state_key):
    """URL used at launch (Aug 2026), now a redirect stub to detail_slug()."""
    return f"{state_key}-minimum-wage-2027.html"


DISCLAIMER = """
  <div class="disclaimer">
    * Rates shown are the standard state minimum wage for non-tipped adult workers and may not
    reflect city/county minimums (which can be higher), tipped-worker rates, training wages, or
    small-business exemptions - see each state's note where relevant. "Pending" states are
    virtually certain to see an increase on January 1, 2027 based on standing law, but the exact
    dollar figure has not been officially calculated or published yet. This site does not publish
    estimated figures - check back or see the source link for the latest official number.
  </div>
"""


def status_badge(state):
    if state["status"] == "confirmed":
        return '<span class="badge confirmed">Confirmed</span>'
    return '<span class="badge pending">Pending</span>'


def new_rate_cell(state):
    if state["status"] == "confirmed":
        return fmt_money(state["new_2027"])
    return "Pending"


def confirmed_keys():
    return [k for k in STATE_ORDER if STATES[k]["status"] == "confirmed"]


def announcements():
    """(iso date, text, state key), newest first."""
    items = [(*STATES[k]["announcement"], k) for k in STATE_ORDER if STATES[k].get("announcement")]
    return sorted(items, reverse=True)


MAP_TILE = 40
MAP_GAP = 4
MAP_PITCH = MAP_TILE + MAP_GAP
MAP_CONFIRMED_COLOR = "#16a34a"
MAP_PENDING_COLOR = "#d97706"
MAP_UNTRACKED_COLOR = "#e2e5eb"


def us_map_svg():
    tiles = []
    for key, m in MAP_STATES.items():
        x, y = m["col"] * MAP_PITCH, m["row"] * MAP_PITCH
        state = STATES.get(key)
        if state:
            fill = MAP_CONFIRMED_COLOR if state["status"] == "confirmed" else MAP_PENDING_COLOR
            text_fill = "#ffffff"
            status_label = "confirmed 2027 rate" if state["status"] == "confirmed" else "increase expected, rate pending"
            open_tag, close_tag = f'<a href="{detail_slug(key)}">', "</a>"
        else:
            fill, text_fill = MAP_UNTRACKED_COLOR, "#6b7280"
            status_label = "no January 2027 increase expected"
            open_tag, close_tag = "", ""

        tiles.append(
            f'{open_tag}<g><title>{m["name"]}: {status_label}</title>'
            f'<rect x="{x}" y="{y}" width="{MAP_TILE}" height="{MAP_TILE}" rx="6" fill="{fill}"></rect>'
            f'<text x="{x + MAP_TILE / 2:.0f}" y="{y + MAP_TILE / 2 + 4:.0f}" text-anchor="middle" '
            f'font-size="11" font-weight="700" fill="{text_fill}">{m["abbr"]}</text></g>{close_tag}'
        )

    width = (max(m["col"] for m in MAP_STATES.values()) + 1) * MAP_PITCH - MAP_GAP
    height = (max(m["row"] for m in MAP_STATES.values()) + 1) * MAP_PITCH - MAP_GAP

    return f"""
  <div class="us-map-wrap">
    <svg viewBox="0 0 {width} {height}" class="us-map" xmlns="http://www.w3.org/2000/svg">
      {''.join(tiles)}
    </svg>
    <div class="map-legend">
      <span><i class="map-swatch" style="background:{MAP_CONFIRMED_COLOR}"></i> Confirmed 2027 rate</span>
      <span><i class="map-swatch" style="background:{MAP_PENDING_COLOR}"></i> Increase expected, rate pending</span>
      <span><i class="map-swatch" style="background:{MAP_UNTRACKED_COLOR}"></i> No Jan 2027 increase expected</span>
    </div>
  </div>
"""


def index_html():
    rows = "\n".join(
        f"""<tr>
      <td><a href="{detail_slug(key)}">{STATES[key]['name']}</a></td>
      <td class="num">{fmt_money(STATES[key]['current_2026'])}</td>
      <td class="num">{new_rate_cell(STATES[key])}</td>
      <td>{status_badge(STATES[key])}</td>
    </tr>"""
        for key in STATE_ORDER
    )

    confirmed_count = len(confirmed_keys())
    pending_count = len(STATE_ORDER) - confirmed_count
    checked = fmt_date(DATA_CHECKED)

    news = "\n".join(
        f'<li><span class="news-date">{fmt_date(d, short=True)}</span> <a href="{detail_slug(k)}">{text}</a></li>'
        for d, text, k in announcements()
    )

    body = f"""
  <h1>State Minimum Wage Increases: January 1, 2027</h1>
  <p class="updated">Updated {checked} &middot; {confirmed_count} of {len(STATE_ORDER)} states confirmed</p>
  <p>{len(STATE_ORDER)} states have a minimum wage law on a January 1 cycle - either a legislated
  step increase or an automatic inflation/formula adjustment - that makes a wage floor increase on
  {EFFECTIVE_DATE} highly likely. As of {checked}, {confirmed_count} of them have a confirmed
  dollar figure; the other {pending_count} publish their exact 2027 rate later this fall.</p>

  <h2>Latest announcements</h2>
  <ul class="news-list">
    {news}
  </ul>

  <h2>2027 minimum wage by state</h2>
  <table>
    <tr><th>State</th><th>2026 rate</th><th>2027 rate</th><th>Status</th></tr>
    {rows}
  </table>
  {us_map_svg()}
  <div class="explain">
    <h2>Why some states show "Pending"</h2>
    <p>Most states with inflation-indexed minimum wages calculate the new rate from a 12-month
    Consumer Price Index window that doesn't close until partway through the year, so the exact
    number isn't known until each state's labor department publishes it - even though the increase
    itself is essentially certain under standing law. This page is updated as each state
    announces its real 2027 figure, rather than publishing a guess.</p>

    <h2>States not on this list</h2>
    <p>States whose minimum wage already reached the top of a legislated schedule with no indexing
    afterward - including Delaware, Illinois, Maryland, and Massachusetts - are not expected to see
    a January 2027 increase under current law, so they're left off this list. A few states change
    their rate on other dates instead: Florida on September 30 (it reached $15.00 on September 30,
    2026), and Oregon, Alaska, and Washington, D.C. on July 1.</p>
  </div>
{DISCLAIMER}
"""
    title = "2027 Minimum Wage by State: January 1, 2027 Increases"
    desc = (f"{confirmed_count} of the {len(STATE_ORDER)} states raising their minimum wage on January 1, 2027 "
            f"have announced the new rate. See each state's 2027 rate, the increase, and which are still pending. "
            f"Updated {checked}.")
    json_ld = [
        {"@context": "https://schema.org", "@type": "WebSite", "name": SITE_NAME, "url": page_url("index.html")},
        {"@context": "https://schema.org", "@type": "WebPage", "name": title, "description": desc,
         "url": page_url("index.html"), "dateModified": DATA_CHECKED, "inLanguage": "en-US"},
    ]
    return page_shell(title, desc, body, filename="index.html", json_ld=json_ld)


def history_html(state_key):
    state = STATES[state_key]
    rows = "\n".join(
        f"""<div class="history-row{' current' if year == 2026 else ''}">
      <span class="history-year">{year}</span>
      <div class="history-bar-track"><div class="history-bar" style="width: {rate / HISTORY_CHART_MAX * 100:.1f}%"></div></div>
      <span class="history-value">{fmt_money(rate)}</span>
    </div>"""
        for year, rate in HISTORY[state_key]
    )
    return f"""
  <div class="explain">
    <h2>{state['name']}'s minimum wage, last 5 years</h2>
    <div class="history-chart">
    {rows}
    </div>
    <p class="source">January 1 rate each year. Sources: U.S. Dept. of Labor historical minimum wage table (2022-2024), Economic Policy Institute (2025), U.S. Dept. of Labor current table (2026).</p>
  </div>"""


def faq_items(state_key):
    state = STATES[state_key]
    if state["status"] == "confirmed":
        rate_q = f"How was {state['name']}'s 2027 rate calculated?"
        rate_a = f"{state['mechanism']}. {state['name']}'s minimum wage is rising from {fmt_money(state['current_2026'])} to {fmt_money(state['new_2027'])} per hour."
    else:
        rate_q = f"Why isn't {state['name']}'s exact 2027 rate available yet?"
        timing = state.get("expected", "States using this kind of formula typically publish the next-year figure between September and December.")
        rate_a = f"{state['mechanism']}. {timing} {state['name']} hasn't published its 2027 figure yet, so this page shows the mechanism instead of a guessed number."

    return [
        (rate_q, rate_a),
        (
            "Does this apply to tipped workers?",
            f"Not necessarily. Many states, including {state['name']}, let employers pay tipped workers a lower direct cash wage as long as tips bring total pay up to at least the full minimum wage. The rate on this page is the standard rate for non-tipped workers - check your state labor department for the tipped cash wage.",
        ),
        (
            "Is this different from the federal minimum wage?",
            f"Yes. The federal minimum wage has been $7.25/hour since 2009. {state['name']}'s minimum wage is higher, and employers covered by both laws must pay the higher of the two.",
        ),
        (
            "When does the new rate take effect?",
            f"{EFFECTIVE_DATE}, alongside minimum wage increases in the other states tracked on this site.",
        ),
    ]


def faq_html(state_key):
    items_html = "\n".join(
        f"""<details>
      <summary>{q}</summary>
      <p>{a}</p>
    </details>"""
        for q, a in faq_items(state_key)
    )
    return f"""
  <div class="faq">
    <h2>Frequently asked questions</h2>
    {items_html}
  </div>"""


def other_states_html(state_key):
    items = "\n".join(
        f'<li><a href="{detail_slug(k)}">{STATES[k]["name"]}<small>{new_rate_cell(STATES[k])}</small></a></li>'
        for k in STATE_ORDER
        if k != state_key
    )
    return f"""
  <div class="explain">
    <h2>Other states raising their minimum wage on {EFFECTIVE_DATE}</h2>
    <ul class="division-list">
    {items}
    </ul>
  </div>"""


def detail_html(state_key):
    state = STATES[state_key]
    slug = detail_slug(state_key)
    current = state["current_2026"]
    current_annual = current * FULL_TIME_HOURS

    note_html = f'<p class="source">{state["note"]}</p>' if state.get("note") else ""

    updated = f"Last checked against official sources: {fmt_date(DATA_CHECKED)}"
    if state.get("announcement"):
        updated = f"Announced {fmt_date(state['announcement'][0])} &middot; {updated}"

    if state["status"] == "confirmed":
        new_rate = state["new_2027"]
        new_annual = new_rate * FULL_TIME_HOURS
        change = new_rate - current
        pct = (change / current) * 100
        title = f"{state['name']} Minimum Wage 2027: {fmt_money(new_rate)}/hr, Up From {fmt_money(current)}"
        desc = (f"{state['name']}'s minimum wage rises from {fmt_money(current)} to {fmt_money(new_rate)} per hour "
                f"on January 1, 2027 (+{pct:.1f}%). Official source: {state['source_name']}.")
        headline = f"""
  <div class="headline">
    <div>{state['name']} minimum wage, effective {EFFECTIVE_DATE}</div>
    <div class="amount">{fmt_money(new_rate)}/hr</div>
    <div>up from {fmt_money(current)}/hr in 2026 (+{fmt_money(change)}, +{pct:.1f}%)</div>
  </div>"""
        table = f"""
  <table>
    <tr><th></th><th>Hourly</th><th>Annual (full-time, {FULL_TIME_HOURS:,} hrs/yr)</th></tr>
    <tr><td>2026 rate</td><td class="num">{fmt_money(current)}</td><td class="num">{fmt_annual(current_annual)}</td></tr>
    <tr><td>2027 rate</td><td class="num">{fmt_money(new_rate)}</td><td class="num">{fmt_annual(new_annual)}</td></tr>
  </table>"""
        explain_extra = f"<p>A full-time worker (2,080 hours/year) at the new {state['name']} minimum wage would earn about <b>{fmt_annual(new_annual)}/year</b> gross, up from about {fmt_annual(current_annual)}/year in 2026.</p>"
    else:
        expected = state.get("expected", "")
        if state.get("expected_short"):
            title = f"{state['name']} Minimum Wage 2027: New Rate Due {state['expected_short']}"
        else:
            title = f"{state['name']} Minimum Wage 2027: Increase Expected, Rate Pending"
        desc = (f"{state['name']}'s minimum wage is expected to rise on January 1, 2027, but the exact rate "
                f"hasn't been published yet. {expected or 'How it is set: ' + state['mechanism'] + '.'}").strip()
        headline = f"""
  <div class="headline">
    <div>{state['name']} minimum wage, effective {EFFECTIVE_DATE}</div>
    <div class="pending">Pending</div>
    <div>currently {fmt_money(current)}/hr in 2026 - a 2027 increase is expected but not yet calculated</div>
  </div>"""
        table = f"""
  <table>
    <tr><th></th><th>Hourly</th><th>Annual (full-time, {FULL_TIME_HOURS:,} hrs/yr)</th></tr>
    <tr><td>2026 rate</td><td class="num">{fmt_money(current)}</td><td class="num">{fmt_annual(current_annual)}</td></tr>
    <tr><td>2027 rate</td><td class="num">Pending</td><td class="num">Pending</td></tr>
  </table>"""
        timing = f" {expected}" if expected else ""
        explain_extra = f"<p>At the current {fmt_money(current)}/hr rate, a full-time worker (2,080 hours/year) earns about <b>{fmt_annual(current_annual)}/year</b> gross.{timing} This page will be updated with the 2027 rate and annual figure as soon as {state['name']} publishes it.</p>"

    body = f"""
  <h1>{state['name']} Minimum Wage 2027</h1>
  <p class="updated">{updated}</p>
  {headline}
  {note_html}

  {table}

  <div class="explain">
    <h2>How the 2027 rate is set</h2>
    <p>{state['mechanism']}.</p>
    {explain_extra}
  </div>

  <p class="source">Source: <a href="{state['source_url']}" target="_blank" rel="noopener">{state['source_name']}</a></p>
  {history_html(state_key)}
  {faq_html(state_key)}
  {other_states_html(state_key)}

  <div class="nav"><a href="index.html">&larr; All states</a></div>
{DISCLAIMER}
"""
    json_ld = [
        {"@context": "https://schema.org", "@type": "WebPage", "name": title, "description": desc,
         "url": page_url(slug), "dateModified": DATA_CHECKED, "inLanguage": "en-US",
         "isPartOf": {"@type": "WebSite", "name": SITE_NAME, "url": page_url("index.html")}},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "2027 minimum wage by state", "item": page_url("index.html")},
            {"@type": "ListItem", "position": 2, "name": f"{state['name']} minimum wage 2027", "item": page_url(slug)},
        ]},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faq_items(state_key)
        ]},
    ]
    return page_shell(title, desc, body, filename=slug, json_ld=json_ld)


def redirect_stub_html(state_key):
    target = detail_slug(state_key)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{STATES[state_key]['name']} Minimum Wage 2027 - moved</title>
<link rel="canonical" href="{page_url(target)}">
<meta http-equiv="refresh" content="0; url={target}">
<script>location.replace("{target}");</script>
</head>
<body>
<p>This page has moved to <a href="{target}">{page_url(target)}</a>.</p>
</body>
</html>"""


def main():
    """Writes every page and returns the filenames of the real (non-redirect) pages."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    pages = {"index.html": index_html()}
    for key in STATE_ORDER:
        pages[detail_slug(key)] = detail_html(key)
    pages.update({"about.html": about_html(), "privacy.html": privacy_html(), "contact.html": contact_html()})
    stubs = {legacy_slug(key): redirect_stub_html(key) for key in STATE_ORDER}

    keep = set(pages) | set(stubs)
    for fname in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, fname)
        if os.path.isfile(path) and fname.endswith(".html") and fname not in keep:
            os.remove(path)

    for fname, content in {**pages, **stubs}.items():
        with open(os.path.join(OUTPUT_DIR, fname), "w", encoding="utf-8") as f:
            f.write(content)

    print(f"Generated {len(pages)} pages + {len(stubs)} redirect stubs -> {OUTPUT_DIR}/")
    return list(pages)


if __name__ == "__main__":
    main()
