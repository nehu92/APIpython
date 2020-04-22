import jwt

token = jwt.encode({'name': 'nehuen', 'pass' : 'nehu1992'}, 'pepe', algorithm='HS256')

print(token)


token = jwt.decode(token, 'pepe', algorith=['HS256'])

print(token)