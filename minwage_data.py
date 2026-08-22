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
