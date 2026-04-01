def calcular_financiamento(capital,taxa_juros,tempo):
    perc = taxa_juros /100
    #Juros Compostos
    montante_total = capital * (1 + perc)**tempo
    fator = (1 + perc)**tempo
    parcela = (capital*fator*perc)/(fator-1)
    return  montante_total, parcela

def tabela_amortizacao(capital, taxa_juros, tempo, parcela):
    saldo = capital
    for i in range(1,tempo+1) :
        juros = saldo * (taxa_juros/100)
        amortizacao = parcela - juros
        saldo = saldo - amortizacao
        print(f'Parcela: {i} | Juros: {juros:.2f}R$ | Amortizacao: {amortizacao:.2f}R$ | Saldo Devedor: {saldo:.2f}R$')

    
capital = float(input("Entre com seu dinheiro inicial:\n"))
taxa_juros = float(input("Entre com a taxa de juros:\n"))
tempo= int(input("Entre com a quantidade de parcelas:\n"))

total,parcela = calcular_financiamento(capital,taxa_juros,tempo) #Chamada função para calcular o financiamento

print(f'O valor de cada parcela: {parcela:.2f}R$\n')
print(f'Valor da montante total: {total:.2f}R$\n')

tabela_amortizacao(capital, taxa_juros, tempo, parcela) #Chamada função para gerar a tabela de amortização