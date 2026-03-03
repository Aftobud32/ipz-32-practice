import requests

print("--- GET Запит ---")
response_get = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(f"Статус код: {response_get.status_code}")
print("Заголовки:")
for key, value in response_get.headers.items():
    print(f"  {key}: {value}")
print("Тіло:")
print(response_get.text)

print("\n--- POST Запит ---")
payload = {'title': 'foo', 'body': 'bar', 'userId': 1}
response_post = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)
print(f"Статус код: {response_post.status_code}")
print("Тіло відповіді:")
print(response_post.text)