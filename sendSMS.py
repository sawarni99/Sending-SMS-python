import os
from twilio.rest import Client

account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)

sms = ''
phono = ''
recno = ''

client.messages.create(to=phono, from_=rec_no, body=sms)

print("SMS sent: " + sms + " \nto: " + phono)
