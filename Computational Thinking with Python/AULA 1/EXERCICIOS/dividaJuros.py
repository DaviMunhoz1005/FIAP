def calculate_debt(principal, rate, months):
    return principal * (1 + rate / 100) ** months

def get_float_input(prompt):
    while True:
        try:
            value = input(prompt).replace(',', '.')
            return float(value)
        except ValueError:
            print("Entrada inválida! Por favor, insira um número válido.")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro válido.")

print("""                                                                                          
         ,---._                              ,----..               
       .-- -.' \               ,-.----.     /   /   \   .--.--.    
       |    |   :         ,--, \    /  \   /   .     : /  /    '.  
       :    ;   |       ,'_ /| ;   :    \ .   /   ;.  \  :  /`. /  
       :        |  .--. |  | : |   | .\ :.   ;   /  ` ;  |  |--`   
       |    :   :,'_ /| :  . | .   : |: |;   |  ; \ ; |  :  ;_     
       :         |  ' | |  . . |   |  \ :|   :  | ; | '\  \    `.  
       |    ;   ||  | ' |  | | |   : .  /.   |  ' ' ' : `----.   \ 
   ___ l         :  | | :  ' ; ;   | |  \'   ;  \; /  | __ \  \  | 
 /    /\    J   :|  ; ' |  | ' |   | ;\  \\   \  ',  / /  /`--'  / 
/  ../  `..-    ,:  | : ;  ; | :   ' | \.' ;   :    / '--'.     /  
\    \         ; '  :  `--'   \:   : :-'    \   \ .'    `--'---'   
 \    \      ,'  :  ,      .-./|   |.'       `---`                 
  "---....--'     `--`----'    `---'                                 
""")

debt = get_float_input('Por favor, insira o valor da sua dívida (exemplo - 1000.50): ')
fees = get_float_input('Insira a porcentagem de juros mensal (exemplo - 20.12): ')
num_months = get_int_input('Insira o número de meses (exemplo - 6 para 6 meses): ')

final_debt = calculate_debt(debt, fees, num_months)

print("\n" + "=" * 50)
print("CÁLCULO DA DÍVIDA ACUMULADA COM JUROS COMPOSTOS")
print("=" * 50)

for i in range(1, num_months + 1):
    accumulated_debt = calculate_debt(debt, fees, i)
    print(f'A dívida acumulada no {i}º mês será de R$ {accumulated_debt:.2f}')

print("=" * 50)
