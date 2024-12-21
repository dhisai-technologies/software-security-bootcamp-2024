
# 9. question======================
# Create a parser that identifies injection risks in dynamic query construction. Your parser should detect:
#     - String joining operations
#     - List comprehension in queries
#     - Dynamic WHERe usage

#program===============
def detect_injection_risks(code):
    risks = []

    # Check for string joining operations in query construction
    # Example: "SELECT * FROM table WHERE column = '" + user_input
    if " + " in code or "f" in code and "{" in code:
        risks.append("String joining operation detected")

    # Check for list comprehensions used in query construction
    # Example: [f"SELECT * FROM {table}" for table in tables]
    if "[" in code and "]" in code and "for" in code:
        risks.append("List comprehension detected in query")

    # Check for dynamic WHERE clause construction in queries
    # Example: "SELECT * FROM data WHERE " + dynamic_where
    if "WHERE" in code and " + " in code:
        risks.append("Dynamic WHERE clause detected")

    return risks


# Example usage
if __name__ == "__main__":
    sample_code = """
    filters = []
    if user_input:
        filters.append(f"column = '{user_input}'")
    query = f"SELECT * FROM table WHERE {' AND '.join(filters)}"
    query_list = [f"SELECT * FROM {table}" for table in tables]
    dynamic_query = "SELECT * FROM data WHERE " + dynamic_where
    """

    # Detect and print potential injection risks in the sample code
    risks = detect_injection_risks(sample_code)
    for risk in risks:
        print(risk)

