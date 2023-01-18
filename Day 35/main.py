
from twilio.rest import Client
account_sid = "AC3cc0660bec8ec35159d570a1e4237a04"
auth_token = "edc4b778124cf0e9d7f9398d7658e5a0"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="It's Going to rain today. ",
                     from_='+13607806746',
                     to='+918092338438'
                 )

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        from_='+13607806746',
                        to='+918092338438'
                    )

print(message.sid)