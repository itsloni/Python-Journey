# ==============================================================================
# FUNCTION TEST 1: THE AUTOMATED IP SANITIZER
# ------------------------------------------------------------------------------
# SCENARIO: Clean messy network logs by stripping trailing/leading whitespaces.
#
# TASKS:
# 1. Define a function named 'clean_ip_address' that accepts a single parameter
#    named 'raw_ip'.
# 2. Inside the function, strip the whitespace from the string.
# 3. Use 'return' to send the cleaned IP string back out.
# ==============================================================================

# [WRITE YOUR TEST 1 FUNCTION HERE]
def clean_ip_address(raw_ip):
    cleaned_ip = raw_ip.strip(" ")
    return cleaned_ip

# Pipeline Execution:
messy_input = "   192.168.1.105   "
sanitized_result = clean_ip_address(messy_input)

print(f"Sanitized IP Output: '{sanitized_result}'\n\n")



# ==============================================================================
# FUNCTION TEST 2: THE THREAT MULTIPLIER CALCULATOR
# ------------------------------------------------------------------------------
# SCENARIO: You are writing a calculator that scores vulnerability risks.
#           It accepts multiple numeric values and calculates an exploit score.
#
# TASKS:
# 1. Define a function named 'calculate_exploit_score' that accepts exactly
#    two parameters: 'base_severity' and 'multiplier'.
# 2. Inside the function, multiply 'base_severity' by 'multiplier'.
# 3. Return the final product integer back to the pipeline.
# ==============================================================================

# [WRITE YOUR TEST 2 FUNCTION HERE]




# Pipeline Execution:
score_1 = calculate_exploit_score(8, 3)
score_2 = calculate_exploit_score(5, 4)

print(f"Calculated Score 1: {score_1}")
print(f"Calculated Score 2: {score_2}")

