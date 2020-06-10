# sends email using gmail
# uses address: my.dummy.python.email@gmail.com
import smtplib, ssl

# send_email arguments:
# recipient - str - recipient's email address
# subject - str - subject line of email
# body - str - body of email
def send_email(recipient, subject, body):

  port = 465  # For SSL
  smtp_server = "smtp.gmail.com"
  sender_email = "my.dummy.python.email@gmail.com"

  msg = f"Subject: {subject}\n{body}"

  context = ssl.create_default_context()
  with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, GMAIL_PASSWORD)
      server.sendmail(sender_email, recipient, msg)
