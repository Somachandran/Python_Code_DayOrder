import requests
city_name = "Coimbatore"
API_key ='3a98608aafa22c0987ce70e6977fab7b'
url= f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print('Weather is',data['weather'][0]['description'])
    print('Current temperature is ',data['main']['temp'])
    print('Current temperature fells like is ',data['main']['feels_like'])
    print('Current humidity is ',data['main']['humidity'])