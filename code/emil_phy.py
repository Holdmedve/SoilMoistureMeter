#e1.1 with picture
##################
import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def emailsender(ImgFileName):
    sender_email = "berrypiraspPHY@gmail.com"
    receiver_email = "berrypiraspPHY@gmail.com"
    password = "WASD1234"

    img_data = open(ImgFileName, 'rb').read()
    message = MIMEMultipart("alternative")
    message["Subject"] = "üzenet a földnedvesség-mérőtől"
    message["From"] = sender_email
    message["To"] = receiver_email


    html = """\
    <html>
    <h1 align="center">Kedves felhasználó!</h1>
    <font size="4">Az Ön által gondozott növény földjének nedvesség<br>
    tartalma a kritikus érték alá sülyedt.<br>
    Öntözze meg a növényét!<br>
    A lenti képen látható grafikon a föld nedveségtartalmának alakulását <br>
    mutatja.</font>
    </html>
    """


    part2 = MIMEText(html, "html")
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))

    message.attach(image)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
#ImgFileName tartalmazza a kép tipusát is pl.:emailsender("kep.png")
emailsender("kep.png")
print('Hello ! I sent an email')