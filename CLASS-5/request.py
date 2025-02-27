import requests  #pip install request
# get request
# response=requests.get("https://jsonplaceholder.typicode.com/posts")
# print(response)

# print(response.json())

# post req
# data={'userId': 1, 'id': 2, 'title': 'qui est esse'}
# response=requests.post("https://jsonplaceholder.typicode.com/posts",json=data)
# print(response.status_code)
# print(response.json())

# update req
# data={'userId': 1, 'id': 2, 'title': 'updatedreq'}
# response=requests.put("https://jsonplaceholder.typicode.com/posts/1",json=data)
# print(response.status_code)
# print(response.json())

# Del req
data={'userId': 1, 'id': 2, 'title': 'updatedreq'}
response=requests.delete("https://jsonplaceholder.typicode.com/posts/1",json=data)
print(response.status_code)
print(response.json())