import requests


# resp = requests.post('http://127.0.0.1:5000/articles/',
#                      json={
#                          'title': 'Заголовок 4',
#                          "text": "Содержание текста 4",
#                          'user': 2
#                      }).json()
# print(resp)


# resp = requests.put('http://127.0.0.1:5000/articles/3',
#                     json={
#                          'title': 'Заголовок изменный Юзер2'
#                     }).json()
# print(resp)

#
resp = requests.delete('http://127.0.0.1:5000/articles/5').json()
print(resp)



# resp = requests.get('http://127.0.0.1:5000/users/2').json()
# print(resp)
#
# resp = requests.get('http://127.0.0.1:5000/articles/').json()
# print(resp)

#
# resp = requests.post('http://127.0.0.1:5000/users/',
#                      json={
#                          'username': 'test2',
#                          "password": "4jkhgsgdhjjklplkkjgo34FET3238h9",
#                          "email": "test@test2.test"
#                      }).json()
# print(resp)