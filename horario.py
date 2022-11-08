def converta(h, m):
    if 0 < h <= 12 and 0 < m < 60:
        print(f'{h}:{m} AM')
    elif 12 < h < 24 and 0 < m < 60:
        print(f'{h - 12}:{m} PM')
    else:
        print('Valor inválido')


while True:
    h = int(input('Hora: '))
    if h == 999: break
    m = int(input('Minuto: '))
    converta(h,m)
    print('='*12)
    controle = int(input("Deseja finalizar o programa(1 - SIM / 2 - NAO: "))
    
    if(controle == 1):
      print("programa finalizado com sucesso")
      break
    elif(controle == 2):
      continue