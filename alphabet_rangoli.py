def obtener_linea_texto(tamanio:int,index_izq:int,index_dere:int)-> str:
    '''Función encargada de imprimir cada fila del patrón'''
    letras_alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p',
    'q','r','s','t','u','v','w','x','y','z']
    texto_izq = ''
    texto_der = ''
    if index_izq >= 0:
        texto_izq = '-'.join(letras_alfabeto[(tamanio-1):index_izq:-1])
        texto_der = '-'.join(letras_alfabeto[index_dere:tamanio])
    else:
        texto_izq = '-'.join(letras_alfabeto[(tamanio-1)::-1])
        texto_der = '-'.join(letras_alfabeto[index_dere:tamanio])     
    return texto_izq + '-' + texto_der


def print_rangoli(size:int):  
    '''Función encargada de imprimir el patrón'''  
    rango_superior:list = list(range(size-1,-1,-1))
    rango_inferior:list = list(range(1,size))
    indices_letras_izq:int = size-2
    indices_letras_der:int = size
    tamanio_columnas:int = (((size-1)*2)*2)+1
    texto:list = []
    #Recorriendo las filas superiores
    for i in rango_superior:
        texto.append(obtener_linea_texto(size,indices_letras_izq,indices_letras_der).center(tamanio_columnas, '-')+ '\n')      
        indices_letras_izq-=1
        indices_letras_der-=1    
    #Recorriendo las filas inferiores    
    indices_letras_izq = 0
    indices_letras_der = 2
    for i in rango_inferior:
        texto.append(obtener_linea_texto(size,indices_letras_izq,indices_letras_der).center(tamanio_columnas, '-')+ '\n')      
        indices_letras_izq+=1
        indices_letras_der+=1
    print(''.join(texto))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
