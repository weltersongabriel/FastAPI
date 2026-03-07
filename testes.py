import requests

headers = {
   "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZXhwIjoxNzczNDkzMTg0fQ.gP4kqq0c3KgQcr63blHoHC0VaLHnxbZCiNNxHo9u2ps"
}

requisicao = requests.get("http://127.0.0.1:8000/auth/refresh", headers=headers)
print(requisicao)
print(requisicao.json())