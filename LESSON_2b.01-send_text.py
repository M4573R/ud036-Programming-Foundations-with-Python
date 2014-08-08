from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC403a715ace1561df11651986bf690aab"
auth_token = "b7c8d596f4cdcf2cf827d679779a8e75"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
  body="Jenny please?! I love you <3",
  to="+358444444444", # Replace with your phone number
  from_="+358751151579") # Replace with your Twilio number

print message.sid

# Twilio does not work in Finland and testing it cost me $2, grrrrr