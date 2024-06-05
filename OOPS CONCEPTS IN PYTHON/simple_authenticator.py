from authenticator import Authenticator

class SimpleAuthenticator(Authenticator):
    def verify_password(self, user_input):
        return user_input == self._password
