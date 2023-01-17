# port-scanner
A simple Python script that scans open host ports. The script compares the newly made scan with the reference set. When differences are detected, it sends an e-mail notification.

## Application launch instructions
**Step 1:** Make sure you have Python installed on your computer. You can check this by typing `python --version` in the console or command prompt. \
**Step 2:** Download the contents of the repository. \
**Step 3:** Open the console or command prompt and navigate to the folder you just created `cd [path_to_folder]`. \
**Step 4:** Create a virtual environment to isolate the installed libraries from other interpreter instances. \
**Step 5:** Install the required libraries `pip install -r requirements.txt` \
**Step 6:** Generate your "App password" for Gmail. For full instruction go to: [Support Google -> Sign in with App Passwords](https://support.google.com/mail/answer/185833?hl=en) \
**Step 7:** Navigate to the project folder and create your template file using command 'nmap -oX template.xml ip_address' \
**Step 8:** After installing all the libraries, you can run the script using the `python main.py` \
