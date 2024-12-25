import requests
api_key="117bcab1cbd84084ff08ea814d397a02"
user_input=input("enter City:  ")
weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
weather=weather_data.json()["weather"][0]["main"]
temp=weather_data.json()["main"]["temp"]
print(f" the weather in {user_input} is {weather}")
print(f" the temp in {user_input} is {temp} celsius")


print("welcome to the random user genderator")
response=requests.get("https://randomuser.me/api")
print(response.status_code)
print(response.json())
gen=response.json()["results"][0]["gender"]
fn=response.json()["results"][0]["name"]["first"]
ln=response.json()["results"][0]["email"]
print(f"your gender is {gen}")
print(f" your first name is {fn}")
print(f" your email is {ln}")


print("welcome")
