# sends email using gmail
# uses address: my.dummy.python.email@gmail.com
import smtplib, ssl
import PIL.Image

# send_email arguments:
# recipient - str - recipient's email address
# subject - str - subject line of email
# body - str - body of email
def send_email(recipient, subject, body):

  port = 465  # For SSL
  smtp_server = "smtp.gmail.com"
  sender_email = "my.dummy.python.email@gmail.com"
  img = PIL.Image.open('./Colab-Utils/mac.jpg')
  exif_data = img._getexif()

  msg = f"From: {sender_email}\nTo: {recipient}\nSubject: {subject}\n\n{body}"

  context = ssl.create_default_context()
  with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.ehlo()
    server.login(sender_email, exif_data[33432])
    server.sendmail(sender_email, recipient, msg)
