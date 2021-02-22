def conversor(tipo_pesos,valor_dolar):
    pesos = float(input('¿Cuántos pesos '+tipo_pesos+' tienes?: '))
    if tipo_pesos == 'argentinos':
        coeficiente_impuesto_pais = 1.3
    else:
        coeficiente_impuesto_pais = 1
    dolares = str(round((pesos/(valor_dolar*coeficiente_impuesto_pais)), 2))
    print('Tienes U$S '+dolares+' dolares')

menu = """
Bienvenido al conversor de monedas 🤑💰

 1 - Pesos Argentinos
 2 - Pesos Colombianos
 3 - Pesos Mexicanos

 Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    #convierte pesos argentinos a dólares al valor oficial considerando el impuesto país
    conversor('argentinos',72.4)
elif opcion ==2:
    #convierte pesos colombianos a dólares al valor oficial considerando el impuesto país 
    conversor('colombianos', 3743.12)
elif opcion ==3:
    #convierte pesos mexicanos a dólares al valor oficial considerando el impuesto país
    conversor('mexicanos', 22.29)
else:
    print('Ingresa una opción correcta por favor')
