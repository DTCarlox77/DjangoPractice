lista = ['Luisa', 'Mercedes', 'Carlos', 'Adrian']

nombre = 'Benito'

if nombre in lista:
    print('El nombre no puede ser insertado dado que ya existe')
    
else:
    lista.append(nombre)
    
print(lista)