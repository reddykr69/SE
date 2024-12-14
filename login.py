def login(username, password):
    """
    Simple login function to authenticate a user.
    """
    if username == "admin" and password == "password123":
        return "Login successful"
    return "Invalid credentials"


if __name__ == "__main__":
    # Simulate user input for testing
    print("Enter username:")
    user = input("> ")  # Accept input from the user
    print("Enter password:")
    passwd = input("> ")  # Accept input from the user

    # Call the login function
    result = login(user, passwd)
    print(result)  # Output the result
