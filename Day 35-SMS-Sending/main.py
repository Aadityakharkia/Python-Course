from twilio.rest import Client

#----------------------------------Defining Twilio Account and learning about sending SMS --------------------

account_sid = "Your ID"
auth_token = "Your Password"
Twilio_number = "Your Twilio Number"
Number = "Your Number"


client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="It's Going to rain today. ",
                     from_=Twilio_number,   # Twilio Number
                     to=Number      # Your Number
                 )

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        from_=Twilio_number,  # Twilio Number
                        to=Number     # Your Number
                    )

print(message.sid)


#----------------------------------Future Work ------------------------------------------------------------------

# Automating it 
# Implementing different programmes with it