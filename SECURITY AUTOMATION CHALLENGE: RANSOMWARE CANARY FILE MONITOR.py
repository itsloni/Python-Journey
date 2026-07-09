# SECURITY AUTOMATION CHALLENGE: RANSOMWARE CANARY FILE MONITOR
#
# CONTEXT: Ransomware attacks encrypt user files and often append a weird extension
# to them (like ".locked"). Security engineers place hidden "Canary Files" on servers.
# If a canary file changes or changes sizes drastically, an automated alert fires.
#
# INSTRUCTIONS:
# 1. Create a function named monitor_file_integrity that takes three parameters:
#    filename (string), original_size (integer), and current_size (integer).
#
# 2. Inside the function, define a list named critical_extensions containing: ".locked", ".crypto", ".enc"
#
# 3. Create a boolean variable named has_bad_extension. Check if ANY of the extensions inside
#    critical_extensions exist at the end of your filename string.
#    (Hint: Python has a built-in string method called .endswith() that returns True or False!)
#
# 4. Create an integer variable named size_difference. Calculate the absolute difference between
#    the original_size and current_size.
#    (Hint: Use Python's built-in abs() function so the result is always a positive number, e.g., abs(A - B))
#
# 5. Create a boolean variable named is_massive_shrinkage. Set it to True if the current_size
#    is less than exactly 50% of the original_size. Otherwise, set it to False.
#
# 6. Determine a final security action string named response_trigger:
#    - If it has a bad extension OR has massive shrinkage, set it to "ISOLATE_ENDPOINT_NOW".
#    - If the size_difference is strictly greater than 5000 bytes (but conditions above aren't met), set it to "FLAG_FOR_MANUAL_AUDIT".
#    - For any other situation, set it to "STATUS_NORMAL".
#
# 7. Return all THREE results simultaneously: has_bad_extension, is_massive_shrinkage, and response_trigger.
#
# 8. Outside the function, test your code by calling monitor_file_integrity with these arguments:
#    filename: "canary_document.docx.locked"
#    original_size: 10000
#    current_size: 2000
#
# 9. Unpack the three returned values into separate variables and print them out.


def monitor_file_integrity(filename, original_size, current_size):
    critical_extensions = [".locked", ".crypto", ".enc"]
    has_bad_extension = filename.endswith(tuple(critical_extensions))

    size_difference = abs(original_size - current_size)

    is_massive_shrinkage = float(current_size) < 0.5 * float(original_size)

    if has_bad_extension or is_massive_shrinkage:
        response_trigger = "ISOLATE_ENDPOINT_NOW"
    elif size_difference > 5000:
        response_trigger = "FLAG_FOR_MANUAL_AUDIT"
    else:
        response_trigger = "STATUS_NORMAL"

    return has_bad_extension, is_massive_shrinkage, response_trigger

bad_extension, massive_shrinkage, response = monitor_file_integrity(
    "canary_document.docx.locked", 10000, 2000)
print(bad_extension, end=" ")
print(massive_shrinkage, end=" ")
print(response)