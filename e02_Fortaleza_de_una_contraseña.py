from validPwd import validPwd

niveles = { 0:'Muy debil',
            1:'Debil',
            2:'Fuerte',
            3:'Muy fuerte'
          }

contraseña = input('Introduce contraseña: ')

nivel = validPwd(contraseña)

print('Tu contraseña es {}'.format(niveles[nivel]))

