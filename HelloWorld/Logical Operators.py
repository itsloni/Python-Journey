# if an applicant has high income AND good credit
#     Eligible for loan
# has_high_income = False
# has_good_credit = True
# has_criminal_record = False

# if has_high_income and has_good_credit: #This is the Logical AND operator. Both Conditions Should be True
#     print("You're Eligible for Loan!.. Yay!")
# else:
#     print("You're NOT Eligible for Loan...Sorry.")

# if has_high_income or has_good_credit: #This is the Logical or operator. At least One Conditions Should be True
#     print("You're Eligible for Loan... Yay!")
# else:
#     print("You're NOT Eligible for Loan...Sorry.")

# to make use of Not Logical Operator, if an applicant has good credit  And doesn't have a criminal record
#  then they are eligible for a LOAN.

has_good_credit = True
has_criminal_record = False


if has_good_credit and not has_criminal_record:
    print("You're Eligible for Loan... Yay!")
