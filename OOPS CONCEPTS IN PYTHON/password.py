def authenticate():
    password = "sai123"
    attempts = 3

    while attempts > 0:
        user_input = input("Enter the password: ")

        if user_input == password:
            print("WELCOME")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong password! Ypu have {attempts} attempts left.")
            else:
                print("Account Blocked")
                break

authenticate()