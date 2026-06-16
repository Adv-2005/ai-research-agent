REPORT_PROMPT = """You are an investment research analyst.

Research:
{query}

Web Results:
{search_results}

Generate a detailed markdown report.

Include:

# Executive Summary

# Recent News

# Market Position

# Risks

# Conclusion

Use only information present in the search results.

Do not invent facts.
 """