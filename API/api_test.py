import requests


response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
# print(type(response))
# print(response)
# print(response.text)
# print(type(response.text))
print(response.json())
list_response = response.json()
# print(type(response.json()))
# print(response.json()[0])
# print(response.json()[0]["name"])
for index in list_response:
    print("name:", index["name"])
    print("Web URL:", index["web_url"])
