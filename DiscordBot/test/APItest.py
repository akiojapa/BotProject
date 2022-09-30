import json, requests

respose = requests.get("https://api.github.com/users/akiojapa")

json_data = json.loads(respose.text)


print(json_data['login'])