# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'Your_Twilio_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hey Man, this an auto generated message.",
                     from_='+1205539000',
                     to='+8801751075454'
                 )

print(message.sid)
