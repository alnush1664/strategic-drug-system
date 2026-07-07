class AuthenticationService:

    _instance = None   # faghat yek object az in class sakhte mishe

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def login(self, username, password):
        print("Dar hale check kardan etelaat karbar:", username)

    def logout(self, username):
        print("Karbar", username, "az system kharej shod")


# test kardane singleton

auth1 = AuthenticationService()
auth2 = AuthenticationService()

print("Aya har do object yeki hastan?", auth1 is auth2)

auth1.login("admin", "1234")
