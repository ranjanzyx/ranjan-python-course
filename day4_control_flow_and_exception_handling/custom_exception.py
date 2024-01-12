# Define the custom exception
class InvalidPasswordException(Exception):
    def __init__(self, message="Invalid password provided"):
        self.message = message
        super().__init__(self.message)


# Stored password for comparison
correct_password = "abc"

user_password = input("Enter your password: ")

try:
    if user_password != correct_password:
        raise InvalidPasswordException("The entered password is incorrect.")
    else:
        print("Login successful.")
except InvalidPasswordException as e:
    print(f"Login failed: {e}")
