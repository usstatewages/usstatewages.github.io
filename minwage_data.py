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
"""

FULL_TIME_HOURS = 2080

STATES = {
    "california": {
        "name": "California",
        "current_2026": 16.90,
        "status": "confirmed",
        "new_2027": 17.40,
        "mechanism": "Annual inflation adjustment (CPI, July-June fiscal-year window)",
        "source_name": "California Dept. of Industrial Relations",
        "source_url": "https://www.dir.ca.gov/DIRNews/2026/2026-66.html",
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
    },
    "colorado": {
        "name": "Colorado",
        "current_2026": 15.16,
        "status": "pending",
        "new_2027": None,
        "mechanism": "Annual inflation adjustment (Amendment 70, 2016)",
        "source_name": "U.S. Dept. of Labor state minimum wage table",
        "source_url": "https://www.dol.gov/agencies/whd/minimum-wage/state",
    },
    "connecticut": {
        "name": "Connecticut",
        "current_2026": 16.94,
        "status": "pending",
        "new_2027": None,
        "mechanism": "Annual inflation adjustment (employment cost index)",
        "source_name": "U.S. Dept. of Labor state minimum wage table",
        "source_url": "https://www.dol.gov/agencies/whd/minimum-wage/state",
    },
    "maine": {
        "name": "Maine",
        "current_2026": 15.10,
        "status": "pending",
        "new_2027": None,
        "mechanism": "Annual inflation adjustment (set formula)",
        "source_name": "U.S. Dept. of Labor state minimum wage table",
        "source_url": "https://www.dol.gov/agencies/whd/minimum-wage/state",
    },
    "minnesota": {
        "name": "Minnesota",
        "current_2026": 11.41,
        "status": "pending",
        "new_2027": None,
        "mechanism": "Annual inflation adjustment (set formula)",
        "source_name": "U.S. Dept. of Labor state minimum wage table",
        "source_url": "https://www.dol.gov/agencies/whd/minimum-wage/state",
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
    },
    "nebraska": {
        "name": "Nebraska",
        "current_2026": 15.00,
        "status": "pending",
        "new_2027": None,
        "mechanism": "Inflation-indexed formula begins in 2027 (2022 ballot measure, final fixed step reached in 2026)",
        "source_name": "U.S. Dept. of Labor state minimum wage table",
        "source_url": "https://www.dol.gov/agencies/whd/minimum-wage/state",
    },
    "new-jersey": {
        "name": "New Jersey",
        "current_2026": 15.92,
        "status": "pending",
        "new_2027": None,
        "mechanism": "Annual inflation adjustment (set formula)",
        "source_name": "U.S. Dept. of Labor state minimum wage table",
        "source_url": "https://www.dol.gov/agencies/whd/minimum-wage/state",
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
        "status": "pending",
        "new_2027": None,
        "mechanism": "Annual inflation adjustment (set formula)",
        "source_name": "U.S. Dept. of Labor state minimum wage table",
        "source_url": "https://www.dol.gov/agencies/whd/minimum-wage/state",
    },
    "washington": {
        "name": "Washington",
        "current_2026": 17.13,
        "status": "pending",
        "new_2027": None,
        "mechanism": "Annual inflation adjustment (set formula)",
        "source_name": "U.S. Dept. of Labor state minimum wage table",
        "source_url": "https://www.dol.gov/agencies/whd/minimum-wage/state",
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
