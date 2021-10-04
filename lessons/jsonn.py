import json
data = '''{
    "name":"Chuck",
    "phone": {
        "type": "intl",
        "number": "+1 432 324 2342"
        },
    "email" : {
        "hide" : "yes"
        }
        }'''

info = json.loads(data)
print('Name', info['name'])
print('Hide', info["email"]["hide"])

# example 2
print('## example 2 \n')
data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''
infoo = json.loads(data)
print('User count', len(infoo))
for item in infoo:
    print('name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

