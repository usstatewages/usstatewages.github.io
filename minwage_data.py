"""
State minimum wage: current (2026) rate vs. the January 1, 2027 rate.

Baseline 2026 rates cross-checked 2026-08-22 against the U.S. Department of Labor's official
state minimum wage table (dol.gov/agencies/whd/minimum-wage/state, "Updated July 1, 2026") -
the primary source for every `current_2026` value below unless a `source_url` override says
otherwise.

Every state here has a January-1-cycle law (either a fixed legislated step or an annual
inflation/formula adjustment) that makes a 2027 increase highly likely. Two status values:

  "confirmed" - the state has already published or legislated an exact 2027 dollar figure.
  "pending"   - the state indexes its minimum wage to inflation (or a fixed formula) every
                January 1, so an increase is virtually certain, but the exact amount has not
                been calculated/announced yet. States typically publish the real number between
                September and December of the prior year.

NEVER invent a number for a "pending" state - leave new_2027 as None and let the page say
"pending" until a real source confirms it, then flip status to "confirmed" and fill new_2027.

Deliberately excluded: states whose minimum wage already reached the top of its legislated
schedule with no indexing after that (Delaware, Illinois, Maryland, Massachusetts) are not
expected to see a January 2027 increase under current law, so they're left out rather than
listed with a misleading "no change" row. Also excluded: Missouri and a few ballot-measure
states where secondary sources disagree on whether post-2026 indexing actually survived later
legislation - re-add only after confirming directly with the state's labor department.

FULL_TIME_HOURS - standard 40hr/week x 52 weeks, used to show annual gross at each rate.

Optional per-state fields:
  "announcement"   - (ISO date, short text) for the hub's "Latest announcements" list. Use the
                     date of the official release or law, never a news write-up's date.
  "expected"       - pending states only: when the state published last year / must publish by
                     statute. Only add it when that date was checked against the state's own site.
  "expected_short" - pending states with a hard statutory deadline, used in the page title.

DATA_CHECKED - the date every status below was last re-checked against each state's own labor
department / governor release. Bump it whenever you re-verify, not just when a number changes -
it's shown on every page as "Last checked".
"""

FULL_TIME_HOURS = 2080

DATA_CHECKED = "2026-09-22"

STATES = {
    "california": {
        "name": "California",
        "current_2026": 16.90,
        "status": "confirmed",
        "new_2027": 17.40,
        "mechanism": "Annual inflation adjustment (CPI, July-June fiscal-year window)",
        "source_name": "California Dept. of Industrial Relations",
        "source_url": "https://www.dir.ca.gov/DIRNews/2026/2026-66.html",
        "announcement": ("2026-07-31", "California announced $17.40"),
    },
    "michigan": {
        "name": "Michigan",
        "current_2026": 13.73,
        "status": "confirmed",
        "new_2027": 15.00,
        "mechanism": "Legislated step increase (Improved Workforce Opportunity Wage Act schedule), then annual inflation adjustment from 2028",
        "source_name": "U.S. Dept. of Labor state minimum wage table",
        "source_url": "https://www.dol.gov/agencies/whd/minimum-wage/state",
    },
    "rhode-island": {
        "name": "Rhode Island",
        "current_2026": 16.00,
        "status": "confirmed",
        "new_2027": 17.00,
        "mechanism": "Legislated step increase (HB 5029)",
        "source_name": "U.S. Dept. of Labor state minimum wage table",
        "source_url": "https://www.dol.gov/agencies/whd/minimum-wage/state",
    },
    "arizona": {
        "name": "Arizona",
        "current_2026": 15.15,
        "status": "pending",
        "new_2027": None,
        "mechanism": "Annual inflation adjustment (Proposition 206, 2016)",
        "source_name": "U.S. Dept. of Labor state minimum wage table",
        "source_url": "https://www.dol.gov/agencies/whd/minimum-wage/state",
        "expected": 'Last year the Industrial Commission of Arizona announced the new rate in October.',
    },
    "colorado": {
        "name": "Colorado",
        "current_2026": 15.16,
        "status": "confirmed",
        "new_2027": 15.71,
        "mechanism": "Annual inflation adjustment required by the Colorado constitution, based on the CPI-W",
        "source_name": "Colorado Department of Labor and Employment",
        "source_url": "https://cdle.colorado.gov/press-releases/press-release-colorado-minimum-wage-will-increase-to-1571/hour-in-2027",
        "note": "Tipped workers: $12.69/hr. Denver's local minimum wage will be $19.84 in 2027; other cities with their own minimum wage set it by local ordinance.",
        "announcement": ("2026-08-13", "Colorado announced $15.71"),
    },
    "connecticut": {
        "name": "Connecticut",
        "current_2026": 16.94,
        "status": "confirmed",
        "new_2027": 17.48,
        "mechanism": "Annual adjustment tied to the U.S. employment cost index for the 12 months ending June 30",
        "source_name": "Office of the Governor of Connecticut",
        "source_url": "https://portal.ct.gov/governor/news/press-releases/2026/08-2026/governor-lamont-announces-minimum-wage-will-increase",
        "announcement": ("2026-08-05", "Connecticut announced $17.48"),
    },
    "maine": {
        "name": "Maine",
        "current_2026": 15.10,
        "status": "confirmed",
        "new_2027": 15.70,
        "mechanism": "Annual cost-of-living adjustment based on the change in the CPI-W from August to August",
        "source_name": "Maine Department of Labor",
        "source_url": "https://www.maine.gov/labor/news_events/article.shtml?id=13362373",
        "note": "Tipped service employees must be paid a direct wage of at least $7.85/hr in 2027.",
        "announcement": ("2026-09-18", "Maine announced $15.70"),
    },
    "minnesota": {
        "name": "Minnesota",
        "current_2026": 11.41,
        "status": "confirmed",
        "new_2027": 11.87,
        "mechanism": "Annual inflation adjustment calculated by the Minnesota Department of Labor and Industry",
        "source_name": "Minnesota Department of Labor and Industry",
        "source_url": "https://dli.mn.gov/news/minimum-wage-rate-adjusted-inflation-jan-1-2027",
        "note": "The 90-day training wage for workers under age 20 rises to $9.68/hr.",
        "announcement": ("2026-08-19", "Minnesota announced $11.87"),
    },
    "montana": {
        "name": "Montana",
        "current_2026": 10.85,
        "status": "pending",
        "new_2027": None,
        "mechanism": "Annual inflation adjustment (set formula)",
        "source_name": "U.S. Dept. of Labor state minimum wage table",
        "source_url": "https://www.dol.gov/agencies/whd/minimum-wage/state",
        "note": "Rate shown is for businesses with gross annual sales above $110,000; smaller non-FLSA-covered businesses have a separate, lower rate.",
        "expected": 'The Department of Labor & Industry sets the new rate no later than September 30 each year.',
        "expected_short": 'by September 30',
    },
    "nebraska": {
        "name": "Nebraska",
        "current_2026": 15.00,
        "status": "confirmed",
        "new_2027": 15.26,
        "mechanism": "Fixed 1.75% increase every January 1 starting in 2027, under LB 258 (in effect since July 17, 2026), which replaced the 2022 ballot measure's inflation formula ($15.00 x 1.0175 = $15.2625, rounded to $15.26)",
        "source_name": "Nebraska Department of Labor",
        "source_url": "https://dol.nebraska.gov/webdocs/getfile/18bc2309-85ed-4957-b072-e899caeaca99",
        "announcement": ("2026-07-17", "Nebraska's LB 258 took effect, fixing 2027 at $15.26"),
    },
    "new-jersey": {
        "name": "New Jersey",
        "current_2026": 15.92,
        "status": "pending",
        "new_2027": None,
        "mechanism": "Annual inflation adjustment (set formula)",
        "source_name": "U.S. Dept. of Labor state minimum wage table",
        "source_url": "https://www.dol.gov/agencies/whd/minimum-wage/state",
        "expected": 'Last year New Jersey announced the new rate on October 1.',
    },
    "new-york": {
        "name": "New York",
        "current_2026": 17.00,
        "status": "pending",
        "new_2027": None,
        "mechanism": "Switches from a legislated schedule to annual CPI-W (Northeast) indexing starting January 2027",
        "source_name": "Office of the Governor of New York",
        "source_url": "https://www.governor.ny.gov/news/money-your-pockets-governor-hochul-reminds-new-yorkers-minimum-wage-increase-january-1",
        "note": "$17.00 applies to New York City, Long Island, and Westchester County; the rest of the state is at $16.00 and rises on the same schedule.",
    },
    "ohio": {
        "name": "Ohio",
        "current_2026": 11.00,
        "status": "pending",
        "new_2027": None,
        "mechanism": "Annual inflation adjustment (set formula)",
        "source_name": "U.S. Dept. of Labor state minimum wage table",
        "source_url": "https://www.dol.gov/agencies/whd/minimum-wage/state",
        "note": "Rate shown is for employers with annual gross receipts of $405,000 or more; smaller employers follow the $7.25 federal rate.",
    },
    "south-dakota": {
        "name": "South Dakota",
        "current_2026": 11.85,
        "status": "pending",
        "new_2027": None,
        "mechanism": "Annual inflation adjustment (set formula)",
        "source_name": "U.S. Dept. of Labor state minimum wage table",
        "source_url": "https://www.dol.gov/agencies/whd/minimum-wage/state",
        "expected": 'Last year South Dakota announced the new rate on October 23.',
    },
    "vermont": {
        "name": "Vermont",
        "current_2026": 14.42,
        "status": "pending",
        "new_2027": None,
        "mechanism": "Annual inflation adjustment (set formula)",
        "source_name": "U.S. Dept. of Labor state minimum wage table",
        "source_url": "https://www.dol.gov/agencies/whd/minimum-wage/state",
    },
    "virginia": {
        "name": "Virginia",
        "current_2026": 12.77,
        "status": "confirmed",
        "new_2027": 13.75,
        "mechanism": "Legislated step increase (HB 1 / SB 1, signed April 9, 2026)",
        "source_name": "Office of the Governor of Virginia",
        "source_url": "https://www.governor.virginia.gov/newsroom/news-releases/2026/april-releases/name-1116004-en.html",
        "note": "The same law raises Virginia's minimum wage to $15.00 on January 1, 2028, with annual inflation adjustments starting in 2029.",
        "announcement": ("2026-04-09", "Virginia's governor signed a law setting $13.75"),
    },
    "washington": {
        "name": "Washington",
        "current_2026": 17.13,
        "status": "pending",
        "new_2027": None,
        "mechanism": "Annual inflation adjustment (set formula)",
        "source_name": "U.S. Dept. of Labor state minimum wage table",
        "source_url": "https://www.dol.gov/agencies/whd/minimum-wage/state",
        "expected": 'L&I publishes the new rate by September 30 each year.',
        "expected_short": 'by September 30',
    },
}

STATE_ORDER = [
    "california", "washington", "new-york", "new-jersey", "connecticut", "michigan",
    "rhode-island", "colorado", "virginia", "arizona", "ohio", "maine", "vermont",
    "nebraska", "minnesota", "montana", "south-dakota",
]

"""
5-year rate history (2022-2026), January 1 rate each year, main/standard tier.
2022-2024 from DOL's historical table (dol.gov/agencies/whd/state/minimum-wage/history,
"Minimum changes by state for 2020 to 2024"). 2025 from EPI's "workers will get a raise on
January 1" report (Dec 2024, epi.org). 2026 matches current_2026 above (DOL current table).
Used only for the trend chart on detail pages - never for the 2027 figure itself.
"""
HISTORY = {
    "california": [(2022, 14.00), (2023, 15.50), (2024, 16.00), (2025, 16.50), (2026, 16.90)],
    "washington": [(2022, 14.49), (2023, 15.74), (2024, 16.28), (2025, 16.66), (2026, 17.13)],
    "new-york": [(2022, 13.20), (2023, 14.20), (2024, 15.00), (2025, 15.50), (2026, 17.00)],
    "new-jersey": [(2022, 13.00), (2023, 14.13), (2024, 15.13), (2025, 15.49), (2026, 15.92)],
    "connecticut": [(2022, 14.00), (2023, 15.00), (2024, 15.69), (2025, 16.35), (2026, 16.94)],
    "michigan": [(2022, 9.87), (2023, 10.10), (2024, 10.33), (2025, 10.56), (2026, 13.73)],
    "rhode-island": [(2022, 12.25), (2023, 13.00), (2024, 14.00), (2025, 15.00), (2026, 16.00)],
    "colorado": [(2022, 12.56), (2023, 13.65), (2024, 14.42), (2025, 14.81), (2026, 15.16)],
    "virginia": [(2022, 11.00), (2023, 12.00), (2024, 12.00), (2025, 12.41), (2026, 12.77)],
    "arizona": [(2022, 12.80), (2023, 13.85), (2024, 14.35), (2025, 14.70), (2026, 15.15)],
    "ohio": [(2022, 9.30), (2023, 10.10), (2024, 10.45), (2025, 10.70), (2026, 11.00)],
    "maine": [(2022, 12.75), (2023, 13.80), (2024, 14.15), (2025, 14.65), (2026, 15.10)],
    "vermont": [(2022, 12.55), (2023, 13.18), (2024, 13.67), (2025, 14.01), (2026, 14.42)],
    "nebraska": [(2022, 9.00), (2023, 10.50), (2024, 12.00), (2025, 13.50), (2026, 15.00)],
    "minnesota": [(2022, 10.33), (2023, 10.59), (2024, 10.85), (2025, 11.13), (2026, 11.41)],
    "montana": [(2022, 9.20), (2023, 9.95), (2024, 10.30), (2025, 10.55), (2026, 10.85)],
    "south-dakota": [(2022, 9.95), (2023, 10.80), (2024, 11.20), (2025, 11.50), (2026, 11.85)],
}

HISTORY_CHART_MAX = 20.00

"""
Tile-grid layout for the US map on the hub page: every state gets a same-size square tile
positioned by approximate region (col, row) rather than exact geographic coordinates - the same
simplified-cartogram approach used by NPR/538-style "square state" maps, chosen because several
states this site tracks (RI, CT, NJ, DE) are geographically tiny and unreadable on a true map.
Not all 50 states are in STATES/HISTORY above (only the 17 with a Jan-2027-cycle law) - MAP_STATES
covers all 50 so the map reads as the whole country, with untracked states shown in neutral gray.
"""
MAP_STATES = {
    "alabama": {"abbr": "AL", "name": "Alabama", "col": 7, "row": 6},
    "alaska": {"abbr": "AK", "name": "Alaska", "col": 0, "row": 0},
    "arizona": {"abbr": "AZ", "name": "Arizona", "col": 2, "row": 4},
    "arkansas": {"abbr": "AR", "name": "Arkansas", "col": 5, "row": 5},
    "california": {"abbr": "CA", "name": "California", "col": 1, "row": 3},
    "colorado": {"abbr": "CO", "name": "Colorado", "col": 3, "row": 3},
    "connecticut": {"abbr": "CT", "name": "Connecticut", "col": 11, "row": 3},
    "delaware": {"abbr": "DE", "name": "Delaware", "col": 10, "row": 4},
    "florida": {"abbr": "FL", "name": "Florida", "col": 8, "row": 7},
    "georgia": {"abbr": "GA", "name": "Georgia", "col": 8, "row": 6},
    "hawaii": {"abbr": "HI", "name": "Hawaii", "col": 0, "row": 4},
    "idaho": {"abbr": "ID", "name": "Idaho", "col": 2, "row": 1},
    "illinois": {"abbr": "IL", "name": "Illinois", "col": 6, "row": 3},
    "indiana": {"abbr": "IN", "name": "Indiana", "col": 7, "row": 3},
    "iowa": {"abbr": "IA", "name": "Iowa", "col": 5, "row": 3},
    "kansas": {"abbr": "KS", "name": "Kansas", "col": 4, "row": 4},
    "kentucky": {"abbr": "KY", "name": "Kentucky", "col": 6, "row": 4},
    "louisiana": {"abbr": "LA", "name": "Louisiana", "col": 5, "row": 6},
    "maine": {"abbr": "ME", "name": "Maine", "col": 11, "row": 0},
    "maryland": {"abbr": "MD", "name": "Maryland", "col": 9, "row": 4},
    "massachusetts": {"abbr": "MA", "name": "Massachusetts", "col": 10, "row": 2},
    "michigan": {"abbr": "MI", "name": "Michigan", "col": 6, "row": 2},
    "minnesota": {"abbr": "MN", "name": "Minnesota", "col": 5, "row": 1},
    "mississippi": {"abbr": "MS", "name": "Mississippi", "col": 6, "row": 6},
    "missouri": {"abbr": "MO", "name": "Missouri", "col": 5, "row": 4},
    "montana": {"abbr": "MT", "name": "Montana", "col": 3, "row": 1},
    "nebraska": {"abbr": "NE", "name": "Nebraska", "col": 4, "row": 3},
    "nevada": {"abbr": "NV", "name": "Nevada", "col": 2, "row": 2},
    "new-hampshire": {"abbr": "NH", "name": "New Hampshire", "col": 10, "row": 1},
    "new-jersey": {"abbr": "NJ", "name": "New Jersey", "col": 10, "row": 3},
    "new-mexico": {"abbr": "NM", "name": "New Mexico", "col": 3, "row": 4},
    "new-york": {"abbr": "NY", "name": "New York", "col": 9, "row": 2},
    "north-carolina": {"abbr": "NC", "name": "North Carolina", "col": 7, "row": 5},
    "north-dakota": {"abbr": "ND", "name": "North Dakota", "col": 4, "row": 1},
    "ohio": {"abbr": "OH", "name": "Ohio", "col": 8, "row": 3},
    "oklahoma": {"abbr": "OK", "name": "Oklahoma", "col": 4, "row": 5},
    "oregon": {"abbr": "OR", "name": "Oregon", "col": 1, "row": 2},
    "pennsylvania": {"abbr": "PA", "name": "Pennsylvania", "col": 9, "row": 3},
    "rhode-island": {"abbr": "RI", "name": "Rhode Island", "col": 11, "row": 4},
    "south-carolina": {"abbr": "SC", "name": "South Carolina", "col": 8, "row": 5},
    "south-dakota": {"abbr": "SD", "name": "South Dakota", "col": 4, "row": 2},
    "tennessee": {"abbr": "TN", "name": "Tennessee", "col": 6, "row": 5},
    "texas": {"abbr": "TX", "name": "Texas", "col": 4, "row": 6},
    "utah": {"abbr": "UT", "name": "Utah", "col": 2, "row": 3},
    "vermont": {"abbr": "VT", "name": "Vermont", "col": 9, "row": 1},
    "virginia": {"abbr": "VA", "name": "Virginia", "col": 8, "row": 4},
    "washington": {"abbr": "WA", "name": "Washington", "col": 1, "row": 1},
    "west-virginia": {"abbr": "WV", "name": "West Virginia", "col": 7, "row": 4},
    "wisconsin": {"abbr": "WI", "name": "Wisconsin", "col": 5, "row": 2},
    "wyoming": {"abbr": "WY", "name": "Wyoming", "col": 3, "row": 2},
}
