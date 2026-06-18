CRITIQUE_PROMPT = """
You are a senior research reviewer.

Review the following reports.

WEB REPORT:
{web_report}

FINANCIAL REPORT:
{financial_report}

PRODUCT REPORT:
{product_report}

Evaluate:

1. Missing information
2. Unsupported claims
3. Low quality analysis
4. Sections that are too short
5. Contradictions between reports

If a report needs improvement, identify the SINGLE worker that should be rerun.

Valid workers:

- WEB
- FINANCIAL
- PRODUCT

Return EXACTLY in one of these formats:

DECISION: APPROVE
WORKER: NONE

REASON:
All reports are sufficiently complete and supported.

OR

DECISION: RETRY
WORKER: WEB

REASON:
Explain what is missing.

OR

DECISION: RETRY
WORKER: FINANCIAL

REASON:
Explain what is missing.

OR

DECISION: RETRY
WORKER: PRODUCT

REASON:
Explain what is missing.

Do not return any other format.
"""