# #Requests Module
# import requests
# #First API Example
# response = requests.get(
#     "https://jsonplaceholder.typicode.com/users"
# )
# print(response)

# #Reading API Data
# import requests
# response = requests.get(
#     "https://jsonplaceholder.typicode.com/users"
# )
# #print(response.text)

# #Convert JSON to Python
# data = response.json()
# #print(data)

# #Accessing Data
# print(data[0]["name"])

# #Fetch User Details
# import requests
# url = "https://jsonplaceholder.typicode.com/users/1"
# response = requests.get(url)
# user = response.json()
# print("ID: ",user["id"])
# print("Name: ",user["name"])
# print("Email: ",user["email"])

# #Creating Data (POST)
# import requests
# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "title":"Python API",
#     "body":"Learning Requests",
#     "UserID": 1
# }
# response = requests.post(
#     url,
#     json=data
# )
# print(response.status_code)
# print(response.json())

# #Updating Data
# import requests
# url ="https://jsonplaceholder.typicode.com/posts/1"
# data = {
#     "title":"updated Title"
# }
# response = requests.patch(
#     url,
#     json=data
# )
# print(response.status_code)
# print(response.json())

# #Delete Data
# import requests
# url ="https://jsonplaceholder.typicode.com/posts/1"
# response = requests.delete(url)
# print(response.status_code)

# #URL
# print(response.url)

# #Headers
# print(response.headers)

# # Handling Errors 
# import requests
# try:
#     url = "https://jsonplaceholder.typicode.com/"
#     response = requests.get(url)
#     response.raise_for_status()
#     data = response.json()
#     print(data)
# except requests.exceptions.RequestException as e:
#     print("Error: ",e)

# import requests
# url = "https://jsonplaceholder.typicode.com/users"
# try:
#     response = requests.get(url)
#     response.raise_for_status()
#     users = response.json()
#     for user in users:
#         print(
#             f"User ID: {user['id']}, "
#             f"Name: {user['name']},"
#             f"Email ID: {user['email']}"
#         )
# except requests.exceptions.RequestException as e:
#     print("Error: ",e)
# import requests
# url = "https://api.open-meteo.com/v1/forecast"
# params ={
#     "latitude": 52.52,
#     "longitude": 13.41,
#     "current": "temperature_2m"
# }
# try:
#     response = requests.get(url,params=params)
#     response.raise_for_status()
#     data = response.json()
#     # print(type(data))
#     # print(data)
#     print("Temperature:", data["current"]["temperature_2m"],"°C")
# except requests.exceptions.RequestException as e:
#     print("Error:",e)