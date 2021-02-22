def calculo_area(base,altura):
    area = (base*altura)/2
    return area

def tipo_triangulo(base,altura,area):
    pass


def run():
    base = float(input('introduce la base del triángulo: '))
    altura = float(input('introduce la altura del triángulo: '))
    area = calculo_area(base,altura)

if __name__ == '__main__':
    run()
