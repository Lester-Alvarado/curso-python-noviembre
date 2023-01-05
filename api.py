# API - stateless
# request
# URL - dominio - https://google.com - https://189.205.65.69
# URL - path - https://google.com/photos
# metodo - GET - POST - PUT - DELETE
# body - {
#   "name": "Lester",
#   "email": "email@ejemplo.com"
# }
# headers - Authorization: abc-123, Content-Type: application/jpg. Accept: application/excel
# Path parameters /photos/1
# Query params /friends?gender=male&adults=yes

# enpoint
# response
# Body
# Headers
# Codigos HTTP - 100 200 300 400

import requests 

response = requests.get("https://swapi.dev/api/people", data={"page": 2})
print(response)
print(response.status_code)
# print(response.content)
print(response.headers)
data = response.json()
print(data ["results"][0]["name"])