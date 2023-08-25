# AC61b96237e01474420a315420adbe912b
# d02ed89d3390d9a433c652ff0d27c063
# +15187506420

import twilio
from twilio.rest import Client
import random

OTP = random.randint(1000,9999)
print(OTP)
account_sid = 'AC61b96237e01474420a315420adbe912b'
auth_token = 'd02ed89d3390d9a433c652ff0d27c063'
client = Client(account_sid, auth_token)

message = client.messages.create(
                     body="Your OTP is" +str(OTP),
                     from_='+15187506420',
                     to='+919718473907'
                 )

print(message.sid)