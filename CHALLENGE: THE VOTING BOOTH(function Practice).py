# =====================================================================
# CHALLENGE: THE VOTING BOOTH
# =====================================================================
#
# THE GOAL:
# Create a reusable function that tallies up votes for a class captain
# election and prints the final winner.
#
# THE NOMINEES:
# Use this exact starting dictionary inside your function to hold
# the scoreboard:
#
# THE RULES:
# 1. Create a custom function named 'tally_votes' that accepts exactly
#    ONE parameter (a string of votes).
# 2. The user will type all the votes as a single sentence separated
#    by spaces (example: "alex sarah alex john alex").
# 3. Your function must break that sentence down to count each vote.
# 4. If a name matches a nominee in the scoreboard, increment their
#    score by 1.
# 5. If someone votes for an invalid name (like "batman"), ignore it
#    completely (do not add it to the scoreboard or crash!).
# 6. Print the final scoreboard dictionary on the screen.
#
# EXPECTED TEST:
# If the input typed is: alex sarah alex batman john alex
# The output printed must be: {'alex': 3, 'sarah': 1, 'john': 1}
# =====================================================================

def tally_votes(votes):
    scoreboard = {
        "alex": 0,
        "sarah": 0,
        "john": 0
    }
    total_votes = {}

    words = votes.split()
    for word in words:
        if word in scoreboard:
            if word not in total_votes:
                total_votes[word] = scoreboard.get(word, 0)
            total_votes[word] += 1
    print(total_votes)

voter = input("What do you want to vote for? ")
tally_votes(voter)