# THE CODE BELOW WAS A ROUGH CREATION BUT THEN I OPTIMIZED IT AFTER GETTING THE CORE RESPONSE!
#THIS FIRST ONE IS HOWEVER FLAWED BECAUSE OF THE ELIF ENTRIES WHICH FLAGS IF
# ATTEMPTS EQUALS 3 EVEN WHEN THERE COULD HAVE BEEN FAILED ATTEMPTS TOO

login_attempts = ["Success", "Success", "Failed", "Success", "Failed" ]
#login_attempts = ["Success", "Failed", "Failed", "Failed", "Success"] #TO use check scenarios
number_attempts = 0
for entries in login_attempts:
    if entries == "Failed":
        number_attempts += 1
        if number_attempts == 3:
            print("[ALERT] Account locked! Bruteforce attack detected!")
            break
    elif entries == "Success":
        number_attempts += 1
        if number_attempts == 3:
            print("[INFO] System secure.")
            break
        else:
            number_attempts = 0
else:
    print("[INFO] System secure.")

#THIS IS THE FLAWLESS OPTIMIZED VERSION .A SHORTER VERSION AND MORE CONCISE

#login_attempts = ["Success", "Success", "Failed", "Success", "Failed" ] #TO use check scenarios
login_attempts = ["Success", "Failed", "Failed", "Failed", "Success"]
number_attempts = 0
for entries in login_attempts:
    if entries == "Failed":
        number_attempts += 1
        if number_attempts == 3:
            print("[ALERT] Account locked! Bruteforce attack detected!")
            break
    else:
        number_attempts = 0
else:
    print("[INFO] System secure.")












