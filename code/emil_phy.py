import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "radvanszkyij@gmail.com"
receiver_email = "radvanszkyij@gmail.com"
password = "Bocs10eves"

message = MIMEMultipart("alternative")
message["Subject"] = "üzenet a földnedvesség-mérőtől"
message["From"] = sender_email
message["To"] = receiver_email


html = """\
<html>
<h1 align="center">Kedves felhasználó!</h1>
<font size="4">Az Ön által gondozott növény földjének nedvesség<br>
tartalma a kritikus érték alá sülyedt.<br>
Öntözze meg a növényét!</font>
<img src="C:/Users/rijon/28767881_2038175236467148_221478428_o.png">
</html>
"""

htmlPart = MIMEText(html, "html")
message.attach(htmlPart)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )

    print('Hello ! I am finished')
