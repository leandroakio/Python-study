adicionar = 's'
fatura = []
total = 0
valid_vfatura = False

print('Este programa avalia se o crédito para financiamento de veículo pode ser liberado. Baseia-se na média de valor das faturas do cartão de crédito')
input('Aperte enter para começar')
parcela = float(input('Digite o valor da parcela mensal do financiamento em R$ (ex: 700.50): '))

while adicionar == 's':
    while valid_vfatura == False:
        vfatura = input('Digite o valor da fatura do mês: ')
        try:
            vfatura = float(vfatura)
            if vfatura <= 0:
                print('O valor da fatura precisa ser maior que zero')
            else:
                valid_vfatura = True
                
        except:
            print("Valor da fatura inválido. Use apenas números e separe os centavos com '.'.")
        
        
    fatura.append([vfatura])
    total += vfatura
    valid_vfatura = False
    adicionar = input('Deseja adicionar mais alguma fatura? (S ou N)').lower()

media = total / len(fatura)

if media < parcela:
    resultado = ('Crédito NÃO aprovado devido a score baixo. Fatura mensal média precisa ser maior que valor da parcela do financiamento')
else:
    resultado = ('Solicitação de crédito aprovada')
    

print ('O valor médio das faturas é de: ',media)
print (resultado)
