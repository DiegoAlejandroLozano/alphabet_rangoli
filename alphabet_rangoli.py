def print_rangoli(size):
    # your code goes here
    letras_alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v',
    'w','x','y','z']
    #Recorriendo las filas superiores
    rango_superior = list(range(size-1,-1,-1))
    indices_letras_izq = size-2
    indices_letras_der = size
    for i in rango_superior:
        if indices_letras_izq >= 0:
            texto_izq = '-'.join(letras_alfabeto[(size-1):indices_letras_izq:-1])
            texto_der = '-'.join(letras_alfabeto[indices_letras_der:size])
        else:
            texto_izq = '-'.join(letras_alfabeto[(size-1)::-1])
            texto_der = '-'.join(letras_alfabeto[indices_letras_der:size])
        texto = texto_izq + '-' + texto_der
        print(texto.center((((size-1)*2)*2)+1, '-'))
        indices_letras_izq-=1
        indices_letras_der-=1    
    #Recorriendo las filas inferiores
    rango_inferior = list(range(1,size))
    indices_letras_izq = 0
    indices_letras_der = 2
    for i in rango_inferior:
        texto_izq = '-'.join(letras_alfabeto[(size-1):indices_letras_izq:-1])
        texto_der = '-'.join(letras_alfabeto[indices_letras_der:size])
        texto = texto_izq + '-' +texto_der
        print(texto.center((((size-1)*2)*2)+1,'-'))
        indices_letras_izq+=1
        indices_letras_der+=1


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
