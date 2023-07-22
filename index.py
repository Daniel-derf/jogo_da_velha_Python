def checar_numero(numero):
    numero_string = str(numero)
    for digito in numero_string:
        if digito == '0' and len(numero_string) == 1:
            return False
    return True

def dividir_numeros(n1, n2):
    if checar_numero(n2):
        print('Resultado: ', n1 / n2)
        return n1 / n2
    else:
        print('Não se pode dividir por 0!')
        return 0


dividir_numeros(120, 2)



