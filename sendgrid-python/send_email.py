import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, template_id

message = Mail(
    from_email="notificaciones@devinhn.com",
    to_emails="mgalindo@devinhn.com",
    subject="Sending with Twilio SendGrid!",
    html_content="<strong>Sent with Python</strong>",
)

try:
    sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
