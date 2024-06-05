from simple_authenticator import SimpleAuthenticator

def main():
    password = "password123"
    authenticator = SimpleAuthenticator(password)
    authenticator.authenticate()

if __name__ == "__main__":
    main()
