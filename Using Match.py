status_code = 400

# if status_code == 200:
#     print("SUCCESS")
# elif status_code == 404:
#     print("Not Found")
# elif status_code == 400:
#     print("Bad Request")
# else:
#     print("Something else went wrong")
match status_code:
    case 200:
        print("SUCCESS")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case _:
        print("Something else went wrong")