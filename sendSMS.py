import os
from twilio.rest import Client

account_sid = ACOUNT_SID
auth_token = TOKE_ID

client = Client(account_sid, auth_token)

sms = 'SMS'
phono = 'PHONE_NO'

client.messages.create(to=phono, from_='+19045483041', body=sms)

print("SMS sent: " + sms + " \nto: " + phono)
