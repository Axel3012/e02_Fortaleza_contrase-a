def validPwd(pwd):
    numeros = '0123456789'
    letras = 'abcdefghijklmnñopqrstuvwxyz'
    pwdCode = []
    i = 0

    for i in range(len(pwd)):
        caracter = pwd[i]
        caracter = caracter.lower()
        if caracter in numeros:
            pwdCode.append('1')
        elif caracter in letras:
            pwdCode.append('2')
        else:
            pwdCode.append('3')

    if '1' in pwdCode and '2' in pwdCode and '3' in pwdCode:
        a = 3
    elif '1' in pwdCode and '2' in pwdCode or '1' in pwdCode and '3' in pwdCode or '3' in pwdCode and '2' in pwdCode:
        a = 2
    else:
        a = 1
    b = 0
    if len(pwdCode) < 8:
        b = -1

    fuerza = a + b
    return fuerza


    
    
    