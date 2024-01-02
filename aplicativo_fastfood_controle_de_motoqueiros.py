def cardapio():
    print('''*****Salgados*****
    101 - Coxinha Comum R$ 4.50
    102 - Coxinha Catupiri - R$ 5.50
    103 - Pastel Assado - R$ 4.80
    104 - Hamburgão - R$ 7.00
    105 - Enrolado - R$ 10.00
    106 - Esfiha - R$ 10.00
    107 - Joelho - R$ 8.00
    
    *****Bebidas*****
    
    201 - Coca-Cola 350ml - R$ 5.00
    202 - Fanta 350 ml - R$ 5.00
    203 - Coca-Cola 1l - R$ 7.00
    204 - Mate-Couro 1l - R$ 6.00
    205 - Coca-Cola 2l - R$ 15.00
    206 - Fanta 2l - R$ 9.00
    500 - Deseja Finalizar? 1-Sim 2-Não 
    ''')

def processar_pedido(escolha, vr_unit):
    qtd = int(input('Quantidade: '))
    vr_parcial = vr_unit * qtd
    print(f'R$: {vr_parcial}')
    return vr_parcial, qtd

def realizar_entrega(motoqueiros):
    motoqueiro = motoqueiros.pop(0)
    motoqueiros.append(motoqueiro)
    print(f'Pedido entregue por Motoqueiro {motoqueiro}')

def calcular_taxa_entrega():
    entrega = input('Deseja entrega? 1-Sim 2-Não: ')
    if entrega == '1':
        return 5.00
    else:
        return 0.00

def obter_forma_pagamento(soma):
    forma_pagamento = input('Escolha a forma de pagamento (1-Crédito, 2-Débito, 3-Dinheiro): ')
    if forma_pagamento == '1':
        return 'Crédito'
    elif forma_pagamento == '2':
        return 'Débito'
    elif forma_pagamento == '3':
        pgt = float(input('Valor pago: '))
        troco = pgt - soma
        print(f'Troco R$:{troco}')
    else:
        print('Opção inválida. Pagamento em dinheiro será assumido.')
        return 'Dinheiro'

cardapio()

soma = 0
escolha = 0
pedidos = {}
motoqueiros = [1, 2, 3]  # Exemplo de motoqueiros disponíveis

while escolha != 500:
    escolha = int(input('Digite o número código do pedido: '))
    
    if escolha not in {101, 102, 103, 104, 105, 106, 107, 201, 202, 203, 204, 205, 206, 500}:
        print("Código inválido. Tente novamente.")
        continue
    
    descricoes = {
        101: 'Coxinha Comum', 102: 'Coxinha Catupiri', 103: 'Pastel Assado', 104: 'Hamburgão',
        105: 'Enrolado', 106: 'Esfiha', 107: 'Joelho', 201: 'Coca-Cola 350ml', 202: 'Fanta 350ml',
        203: 'Coca-Cola 1L', 204: 'Mate-Couro 1l', 205: 'Coca-Cola 2l', 206: 'Fanta 2l',
        500: 'Finalizar'
    }
  
    vr_units = {
        101: 4.5, 102: 5.5, 103: 4.8, 104: 7.0, 105: 10.0, 106: 10.0, 107: 8.0, 201: 5.0, 202: 5.0,
        203: 7.0, 204: 6.0, 205: 15.00, 206: 9.00,
    }
    
    if escolha == 500:
        taxa_entrega = calcular_taxa_entrega()
        soma += taxa_entrega
        realizar_entrega(motoqueiros)
    else:
        print(f'{descricoes[escolha]} R$ {vr_units[escolha]}')
        vr_parcial, qtd = processar_pedido(escolha, vr_units[escolha])
        soma += vr_parcial
        pedidos[descricoes[escolha]] = qtd

forma_pagamento = obter_forma_pagamento(soma)
print(f'Total: R$ {soma} - Forma de pagamento: {forma_pagamento}')

# Adicionando opção para reiniciar o programa
reiniciar = input("Deseja fazer outro pedido? (1-Sim, 2-Não): ")
if reiniciar == '1':
    cardapio()
    soma = 0
    escolha = 0
    pedidos = {}
    motoqueiros = [1, 2, 3]
else:
    print("Programa encerrado. Obrigado!")