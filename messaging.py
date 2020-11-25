import twilio
import twilio.rest

from twilio.rest import Client 
 
account_sid = 'AC6dc095b0aeb6ad791e0c4185af04e920' 
auth_token = 'beba3a413ae721636708b92acef90d68' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+33684089265',  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to='whatsapp:+33684089267' 
                          ) 
 
print(message.sid)