# ==============================================================================
# CHALLENGE 4: THE AUTOMATED NETWORK PORT TRACKER
# ==============================================================================
# PROMPT: Design an automated system to track an active network port profile.
#         The system must register a port by its integer number when created,
#         and automatically track its data transfer volume starting at 0 Megabytes.
#         The profile needs an action to record when data passes through it,
#         adding the specific number of transferred Megabytes to its total volume.
#         If the port's total volume ever exceeds 10,000 Megabytes, it must
#         automatically shift its network priority status to "THROTTLED".
#
# PIPELINE REQUIREMENT:
# Simulate a massive file transfer that pushes a port over the limit and
# verify its state updates completely autonomously below your class!
# ==============================================================================

# [ARCHITECT YOUR CLASS AND CALLING PIPELINE COMPLETELY BELOW]