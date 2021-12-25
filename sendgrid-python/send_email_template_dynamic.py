import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, template_id

message = Mail(
    from_email="notify@developersindustry.com", to_emails="mgalindo@devinhn.com"
)

message.template_id = "d-1ede0b26870e4be89b88515f214517fc"
message.dynamic_template_data = {
    "subject": "Playing with templates!",
    "name": "Mario Galindo",
}

try:
    sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
