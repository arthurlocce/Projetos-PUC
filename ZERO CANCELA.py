print("Bem vindo ao Zero Cancela")
num = int(input("Digite um numero(negativo para sair): "))
ultimo = 0
penultimo = 0
ant_penultimo = 0
if num > 0:
    soma = num
    ultimo = num
    num_con = 1
    num_desc = 0
    cont_zero = 0
elif num == 0:
    soma = 0
    num_con = 0
    num_desc = 0
    cont_zero = 1
elif num <0:
    soma = 0
    num_con = 0
    num_desc = 0
while num >= 0:
    num = int(input("Digite um numero(negativo para sair): "))
    if num > 0:
        soma = soma + num
        num_con = num_con + 1
        cont_zero = 0
        ant_penultimo = penultimo
        penultimo = ultimo
        ultimo = num
    elif num == 0:
        if ultimo != 0:
            num_con = num_con - 1
            num_desc = num_desc + 1
        cont_zero = cont_zero + 1
        soma = soma - ultimo
        ultimo = penultimo
        penultimo = ant_penultimo
        ant_penultimo = 0
        if cont_zero > 3:
            cont_zero=0
            print('Só é permitido até 3 zeros consecutivos!!!')
            num = int(input("Digite um numero(negativo para sair): "))
            while num==0:
                print('Só é permitido até 3 zeros consecutivos!!!')
                num = int(input("Digite um numero(negativo para sair): "))
            if num > 0:
                soma = soma + num
                ant_penultimo = penultimo
                penultimo = ultimo
                ultimo = num
                num_con = num_con + 1
print('Zero Cancela Finalizado')
print(f"Soma Total: {soma}")
print(f'Numeros Considerados: {num_con}')
print(f'Numeros Desconsiderados: {num_desc}')

