# Max Clingroth
# Lab 07 Question 9
import requests

response = requests.get("https://docs.python-requests.org/en/latest/api/")
print(response.status_code)
if response.status_code == 200:
    print("SUCCESS")
else:
    print("Error")
print(response.headers["Content-Type"])
