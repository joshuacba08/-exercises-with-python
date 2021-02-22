def num_primo(numero):
#declaro una variable para contar
    count = 0
#este ciclo se repetirá dentro del rango del número ingresado
    for i in range(1,numero + 1): 
#Siempre que el módulo sea 0, agregaré una unidad a mi contador
        if numero%i == 0:
            count +=1
#si el contador llegó a ser 1 o 2 retornaré True
    if count == 2 or count ==1:
        return True
#Cualquier otro valor para el contador devolverá False
    else:
        return False

def run():
    num = int(input('Ingresa un número: '))
    if num_primo(num):
        print('El número es primo')
    else:
        print('No es primo')

if __name__ == "__main__":
    run()


