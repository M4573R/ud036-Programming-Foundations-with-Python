THIS IS NOT TO BE RUN !!!!

from twilio.rest import TwilioRestClient
# inside twillio is a folder rest
# from rest we want class TwilioRestClient
# this line can also be:
#
# from twilio import rest
# now access via rest.TwilioRestClient

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

OOP EXPLANATION

Inside twillio is a folder rest
inside is a python file with a class TwilioRestClient
we are calling a function __init__ in class TwilioRestClient
we create an object (instance) of the class TwilioRestClient
the object can do all the things defined in the TwilioRestClient class

Class is blueprint with basic information. It can be used to create a lot of instances like row houses in suburbs. They are all made on the same blueprint.



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
Here are the questions:
1. What is a class?
2. What is an instance of a class?
3. Thus far we have compared the class to a blueprint. Can you think of another analogy to explain classes and their instances?

1. Class is an instruction holder
2. Instance of a class is a thing made with some or all of the instructions
3. Since we talked about blueprint, I would stay in the same area.
=> Building materials store could be a Class.
=> The land we have for our house is initialized object
=> Everything we build with the elements from the store are functions we take from the class
