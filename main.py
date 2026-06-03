# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import requests
from twilio.rest import Client
import os

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

print("$$$$TEST$$$$$")

print(api_key)
print("$$$$TEST$$$$$")

parameters ={
    "lat": 54.5972 ,
    "lon": -5.930120,
    "appid": api_key,
    "cnt": 4
}


url = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(url = url, params = parameters)
response.raise_for_status()

data = response.json()

will_rain = 0
for i in range(len(data["list"])):
    print((data["list"][i]["weather"][0]["id"]))
    if data["list"][i]["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    print("Take an umbrella")
    # client = Client(account_sid, auth_token)
    # message = client.messages.create(
    #     body="It might rain, bring an umbrella",
    #     from_="+17744482357",
    #     to="+31647645794",
    # )
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It might rain, bring an umbrella",
        from_="whatsapp:+14155238886",
        to="whatsapp:+31647645794",
    )

    print(message.sid)
