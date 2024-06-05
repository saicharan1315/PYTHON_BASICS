from abc import ABC, abstractmethod

class Authenticator(ABC):
    def __init__(self, password):
        self._password = password
        self._attempts = 3

    @abstractmethod
    def verify_password(self, user_input):
        pass

    def authenticate(self):
        while self._attempts > 0:
            user_input = input("Enter the password: ")

            if self.verify_password(user_input):
                print("Welcome!")
                break
            else:
                self._attempts -= 1
                if self._attempts > 0:
                    print(f"Wrong password! You have {self._attempts} attempts left.")
                else:
                    print("Account blocked.")
                    break
