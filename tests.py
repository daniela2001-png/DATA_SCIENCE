#!/usr/bin/env python3
PI = 3.14
def funcion_ventana(x, h):
    area_rec = x * (h - (x / 2)) # no sé como definir a h en terminos de x
    area_cir = (PI * (x ** 2)) / 2
    resultado = int(area_rec +  area_cir)
    print('el área de la ventana en funcion del ancho es: {}'.format(resultado))

funcion_ventana(20, 20)