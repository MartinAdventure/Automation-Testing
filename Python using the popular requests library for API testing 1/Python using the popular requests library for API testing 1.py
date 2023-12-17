import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(api_url)

if response.status_code == 200:
    print("API call successful!")
    print("Response JSON:")
    print(response.json())
else: 
    print(f"API call failed with status code: {response.status_code}")