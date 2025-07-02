import requests
url="https://jsonplaceholder.typicode.com/posts/"
data={
    "title": "Hi students",
    "boy":"Wipro Greeks",
    "userId":1

}
response=requests.post(url,json=data)
print("Staus code",response.status_code)
print("Response json",response.json())