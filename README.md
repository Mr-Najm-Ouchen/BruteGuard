# BruteGuard
 BruteGuard is a password brute-forcing tool for security testing. By specifying a URL, username, and wordlist, it systematically tests each password until the correct one is found. Once identified, it displays the successful password. BruteGuard is intended solely for ethical use in authorized environments

Downloading BruteGuard

For Windows, macOS, and Linux
Open Terminal or Command Prompt:

Windows: Search for "Command Prompt" in the Start menu.
macOS: Open "Terminal" from Applications > Utilities.
Linux: Open "Terminal" from your application menu.
Ensure Git is Installed:

If Git is not installed, download it from Git Downloads and follow the installation instructions.
Clone the Repository: Run the following command to clone the BruteGuard repository:

bash
Copier le code
git clone https://github.com/Mr-Najm-Ouchen/BruteGuard.git
Navigate to the Directory: Change to the directory where BruteGuard was cloned:

bash
Copier le code
cd BruteGuard
Usage Instructions
Prepare Your Wordlist:

Create a text file with potential passwords, each on a new line. Name it, for example, passwords.txt.
Run the Tool:

Execute the Python script to start using BruteGuard. You will need to have Python installed on your system. Run the following command:
bash
Copier le code
python brute_guard.py
Provide Input:

When prompted, enter the login URL, the username, and the path to your wordlist file. For example:
mathematica
Copier le code
Enter the login URL: http://example.com/login
Enter the username to test: your_username
Enter the path to the password file: passwords.txt
View Results:

The tool will systematically test each password and will display the correct password if found.
Important Notes
Ethical Use Only: Ensure you have permission to test the security of the target system.
Testing Environment: It is recommended to use this tool in controlled environments such as labs or authorized testing scenarios.
