import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# List of people with their birthdays
people = [
    {"name": "ABC", "email": "XYZ@gmail.com", "birthday": "08-08"},
]

# Email credentials
sender_email = "senders email"
sender_password = "valid password"

# Function to send email
def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.outlook.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, to_email, text)
            print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Checking Date
today = datetime.today().strftime("%m-%d")

# Check birthdays and send email if today is someone's birthday
for person in people:
    if person["birthday"] == today:
        subject = f"All the best, {person['name']}!"
        body = f"Dear {person['name']},\n\nWishing you all the best for the Linux Club interview!\n\nBest regards,\nYour CHaCha"
        send_email(person["email"], subject, body)
