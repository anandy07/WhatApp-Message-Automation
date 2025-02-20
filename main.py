# step-1 install required libraries

from twilio.rest import Client
from datetime import datetime, timedelta
import time

# step-2 twilio credentals

account_sid = '.....'
auth_token = '.........'
client = Client(account_sid, auth_token)


# step-3 degine send message function

def send_whatsapp_message(recipient_number , message_body):
    try:
        message = client.messages.create(
        from_='whatsapp:......',                  # Twilio's WhatsApp sandbox number
        body=message_body,
        to=f'whatsapp:{recipient_number}'  # Recipient's number
    )
        print(f'Message sent successfully! Message SID :{message.sid}')
    
    except Exception as e:
        print("An error occurred")


# step-4  user input 

name = input("Enter the recipient name = ")
recipient_number = input("Enter the recipient WhatApp number with country code (e.g +1234)")
message_body = input(f" Enter the message you want to send to {name}: ")

#step-5 date / time and calculate delay

date_str = input("Enter the date to send the message (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (HH:MM in 24hour format): ")


# datetime

schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()


#calculate delay 

time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <=0 :
    print(" The specified time is in the past. Please enter a future date and time")

else:
    print(f"Message scheduled to be sent to {name} at {schedule_datetime}.")

    # wait until the scheduled time

    time.sleep(delay_seconds)

    # send message 
    send_whatsapp_message(recipient_number , message_body)