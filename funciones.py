edad = int(input('Decime tu edad: '))

def mayor_de_edad(edad):
    if edad >= 20:
        print('Sos mayor de edad')
    elif edad < 20 and edad>0:
        print('No sos mayor de edad')
    else:
        print('Ingresa un numero positivo')

def run():
    mayor_de_edad(edad)

if __name__ = '__main__':
    run()
