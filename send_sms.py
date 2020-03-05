# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACe1314d7c39d1767a1cb1f85599b4b3fb'
auth_token = '64856e36948f1d9082f200e2b55d6adf'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hey Man, this an auto generated message.",
                     from_='+12055393334',
                     to='+8801751072735'
                 )

print(message.sid)