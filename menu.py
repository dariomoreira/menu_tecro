import json

# open JSON file
f = open('menu.json',)
data = json.load(f) #data es un diccionario
#print('keys',data.keys())
#print('comida',data['comida'])
#print(len(data['comida']))
for i in data['comida']:
    print('Plato principal: ',i['principal'])
    print('Guarnicion: ',i['guarnicion'])

#print('Datos:',data.items())
    
f.close()