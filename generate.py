"""
Generates all pages for the US State Minimum Wage Tracker site:
  - index.html                         hub: table of every tracked state's Jan 1, 2027 status
  - {state}-minimum-wage-2027.html      per-state detail page

Scope: states with a January-1-cycle minimum wage law (legislated step or inflation/formula
index) that make a 2027 increase highly likely. See minwage_data.py for sourcing and the states
deliberately left out. "confirmed" states show a real 2027 number; "pending" states show the
mechanism and an honest "not yet announced" status - never a guessed number.
"""
import os

from minwage_data import STATES, STATE_ORDER, FULL_TIME_HOURS, HISTORY, HISTORY_CHART_MAX, MAP_STATES
from static_pages import about_html, privacy_html, contact_html, SITE_NAME, page_shell

OUTPUT_DIR = "docs"
BASE_URL = "https://usstatewages.github.io"

EFFECTIVE_DATE = "January 1, 2027"


def fmt_money(n):
    return f"${n:,.2f}"


def fmt_annual(n):
    return f"${n:,.0f}"


def detail_slug(state_key):
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

    confirmed_count = sum(1 for k in STATE_ORDER if STATES[k]["status"] == "confirmed")

    body = f"""
  <h1>State Minimum Wage Increases: January 1, 2027</h1>
  <p>{len(STATE_ORDER)} states have a minimum wage law on a January 1 cycle - either a legislated
  step increase or an automatic inflation/formula adjustment - that makes a wage floor increase on
  {EFFECTIVE_DATE} highly likely. As of today, {confirmed_count} of them have a confirmed dollar
  figure; the rest calculate and publish their exact 2027 rate later in the year (typically
  September through December).</p>
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
    a January 2027 increase under current law, so they're left off this list.</p>
  </div>
{DISCLAIMER}
"""
    return page_shell(
        f"{SITE_NAME} - State Minimum Wage Increases for January 1, 2027",
        f"Track which US states are raising their minimum wage on January 1, 2027, with confirmed rates where announced and honest pending status where not.",
        body,
    )


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


def faq_html(state_key):
    state = STATES[state_key]
    if state["status"] == "confirmed":
        rate_q = f"How was {state['name']}'s 2027 rate calculated?"
        rate_a = f"{state['mechanism']}. {state['name']}'s minimum wage is rising from {fmt_money(state['current_2026'])} to {fmt_money(state['new_2027'])} per hour."
    else:
        rate_q = f"Why isn't {state['name']}'s exact 2027 rate available yet?"
        rate_a = f"{state['mechanism']}. States using this kind of formula typically calculate and publish the exact next-year figure between September and December of the prior year - {state['name']} hasn't published it yet, so this page shows the mechanism instead of a guessed number."

    items = [
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
    items_html = "\n".join(
        f"""<details>
      <summary>{q}</summary>
      <p>{a}</p>
    </details>"""
        for q, a in items
    )
    return f"""
  <div class="faq">
    <h2>Frequently asked questions</h2>
    {items_html}
  </div>"""


def detail_html(state_key):
    state = STATES[state_key]
    current = state["current_2026"]
    current_annual = current * FULL_TIME_HOURS

    note_html = f'<p class="source">{state["note"]}</p>' if state.get("note") else ""

    if state["status"] == "confirmed":
        new_rate = state["new_2027"]
        new_annual = new_rate * FULL_TIME_HOURS
        change = new_rate - current
        pct = (change / current) * 100
        title = f"{state['name']} Minimum Wage 2027: {fmt_money(new_rate)}/hr Confirmed"
        desc = f"{state['name']}'s minimum wage rises from {fmt_money(current)} to {fmt_money(new_rate)} per hour on January 1, 2027 ({state['mechanism']})."
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
        title = f"{state['name']} Minimum Wage 2027: Increase Expected, Rate Pending"
        desc = f"{state['name']}'s minimum wage is expected to rise on January 1, 2027 via {state['mechanism'].lower()}, but the exact rate hasn't been published yet."
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
        explain_extra = f"<p>At the current {fmt_money(current)}/hr rate, a full-time worker (2,080 hours/year) earns about <b>{fmt_annual(current_annual)}/year</b> gross. This page will be updated with the 2027 rate and updated annual figure as soon as {state['name']} publishes it.</p>"

    body = f"""
  <h1>{state['name']} Minimum Wage 2027</h1>
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

  <div class="nav"><a href="index.html">&larr; All states</a></div>
{DISCLAIMER}
"""
    return page_shell(title, desc, body)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    valid_filenames = {"index.html", "about.html", "privacy.html", "contact.html", "sitemap.xml", "ads.txt"}
    for key in STATE_ORDER:
        valid_filenames.add(detail_slug(key))
    for fname in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, fname)
        if os.path.isfile(path) and fname.endswith(".html") and fname not in valid_filenames:
            os.remove(path)

    urls = []

    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html())
    urls.append(f"{BASE_URL}/index.html")

    for key in STATE_ORDER:
        with open(os.path.join(OUTPUT_DIR, detail_slug(key)), "w", encoding="utf-8") as f:
            f.write(detail_html(key))
        urls.append(f"{BASE_URL}/{detail_slug(key)}")

    static_files = {"about.html": about_html(), "privacy.html": privacy_html(), "contact.html": contact_html()}
    for filename, html in static_files.items():
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(html)
        urls.append(f"{BASE_URL}/{filename}")

    print(f"Generated {len(urls)} pages -> {OUTPUT_DIR}/")
    return urls


if __name__ == "__main__":
    main()
