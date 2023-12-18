import requests

def test_api_call():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(api_url)

    assert response.status_code == 200, f"API call failed with status code: {response.status_code}"

    assert "userId" in response.json(), "Missing 'userId' in response"
    assert "title" in response.json(), "Missing 'title' in response"