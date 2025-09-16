from twilio.rest import Client
import smtplib

def send_sms(body, config):
    client = Client(config['twilio_sid'], config['twilio_token'])
    client.messages.create(
        body=body,
        from_=config['from'],
        to=config['to']
    )

def send_email(subject, body, config):
    with smtplib.SMTP(config['smtp_server'], config['smtp_port']) as server:
        server.starttls()
        server.login(config['smtp_user'], config['smtp_password'])
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(config['from'], config['to'], message)