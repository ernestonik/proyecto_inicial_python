#IMPORTAR
#DEFINIR
#EL MAIN
#APLICAR
#PERSONALIZAR
#PONER MAS PALABRAS DIFICILES
#MEJORAS
    #2 JUGADORES
    #QUE RESTE LAS VIDAS
    #TABLA DE INTENTOS
    #¡¡¡¡¡¡¡¡¡¡¡¡MAXIMO HASTA EL DOMINGO 15:00 NO OLVIDAR!!!!!!!!!!!!!!!



import csv
import random
import interfaz

def leer_palabra_secreta(csvfilename):

    archivo = 'palabras.csv'
    with open(archivo) as f:
        palabras_secretas = csv.DictReader(f) 
        lista = list(palabras_secretas)
        lista_palabras = []
        for row in lista:
            lista_palabras.append(row['palabras'])
        
    #HASTA ACA
    palabra_secreta = random.choice(lista_palabras)
    return(palabra_secreta)


def pedir_letra(letras_usadas):
    while True:
    
        letra_ingresada = str(input('INGRESA UNA LETRA POR FAVOR: '))
        letra = letra_ingresada.lower()
        if len(letra) > 1:
            continue
        else:
            if letra in letras_usadas:
                continue
        
            else:
        
                letras_usadas.append(letra)
        return(letra)
        break
#HASTA ACA 
#VERIFICAR, VALIDAR Y PERSONALIZAR
def verificar_letra(letra, palabra_secreta):

    if letra in palabra_secreta:
        return(True)
    else:
        return(False)



def validar_palabra(letras_usadas, palabra_secreta):
    a = 0
    for i in palabra_secreta:
        if i not in letras_usadas:
            a = 0
        else:
            a = a + 1
    if a == len(palabra_secreta):
        return(True)
    else:
        return(False)
#HASTA ACA
#PREGUNTAR EN DISCORD MAÑANA

if __name__ == "__main__":
    
    print("\n¡Aquí comienza el juego del ahorcado!\n")
    max_cantidad_intentos = 7 #CAMBIAR SI HAY TIEMPO PARA QUE RESTE
    intentos = 0
    letras_usadas = []
    es_ganador = False

    palabra_secreta = leer_palabra_secreta('palabras.csv')
    
#CAMBIAR DIBUJOS PARA PERSONALIZAR Y ESO
    interfaz.dibujar(palabra_secreta, letras_usadas, intentos)
    
    while intentos < max_cantidad_intentos and not es_ganador:
        
        letra = pedir_letra(letras_usadas)

        if verificar_letra(letra, palabra_secreta) == False:
            intentos += 1
        
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

        if validar_palabra(letras_usadas, palabra_secreta) == True:
            es_ganador = True
            break
#HASTA ACA
#PERSONALIZAR SI HAY TIEMPO
    if es_ganador:
        print(f'\n¡FELICITACIONES GANASTE! {palabra_secreta}!\n')
        print ("Cantidad de Intentos:", intentos)
    else:
        print('\n¡MUERTO!')
        print(f'\n¡PERDISTE!, LA PALABRA ERA, {palabra_secreta}!\n')
        print ("X.X")
