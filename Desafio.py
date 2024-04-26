while True:
    nome = str(input('Qual é o nome do seu herói? '))
    quantidade_xp = int(input('Qual é a quantidade de XP que seu herói possui? '))

    if quantidade_xp <= 1000:
         nivel = 'Ferro'
    elif quantidade_xp <= 2000:
         nivel = 'Bronze'
    elif quantidade_xp <= 5000:
         nivel = 'Prata'  
    elif quantidade_xp <= 7000:
         nivel = 'Ouro'        
    elif quantidade_xp <= 8000:
         nivel = 'Platina'
    elif quantidade_xp <= 9000:
         nivel = 'Ascendente'  
    elif quantidade_xp <= 10000:
         nivel = 'Imortal'     
    else:
         nivel = 'Radiante'
    print(f'O Herói de nome {nome} está no nível {nivel}.')

    r = input('Deseja continuar? [S/N] ').upper()
    if r != 'S':
        print('Fim!')
        break
