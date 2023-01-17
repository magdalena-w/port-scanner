import subprocess
import pyndiff
import smtplib
import ssl
from mail_token import my_app_token


def send_email():
    port = 465  # SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "example1@gmail.com"
    receivers = ['example2@gmail.com', 'example3@gmail.com']
    password = my_app_token
    message = """Subject: Differences in the configuration!
    The port scanner detected differences in the configuration of open ports. """

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receivers, message)


def check_open_ports():
    try:
        ip_addr = 'scanme.nmap.org'
        print(f"Checking host {ip_addr}")
        subprocess.call(['nmap', '-oX', 'new_scan.xml', ip_addr])
        diff = pyndiff.generate_diff("template.xml", "new_scan.xml")
        if "No scan diff detected between scans." not in diff:
            send_email()
    except FileNotFoundError:
        print("There is no template file! Try make one first.")


if __name__ == "__main__":
    check_open_ports()
