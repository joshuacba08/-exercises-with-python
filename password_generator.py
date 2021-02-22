import random

def password_generator():
    capital_letter = ['A','B','C','D','F','G']
    lower_case = ['a','b','c','d','e','f','g']
    simbol = ['!','#','$','&','/','(',')']
    number = ['1','2','3','4','5','6','7','8','9','0']

    caracter = capital_letter + lower_case + simbol + number
    password = []

    for i in range(15):
        caracter_random = random.choice(caracter)
        password.append(caracter_random)

    password = ''.join(password)
    return password


def run():
    password = password_generator()
    print('Tu nueva contraseña es: ' + password)

if __name__ == "__main__":
    run()
