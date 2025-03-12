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

print("\n" + "=" * 55)
print("CÁLCULO DA DÍVIDA ACUMULADA COM JUROS COMPOSTOS")
print("=" * 55)
print(f'A dívida total no final do período será de R${final_debt:.2f}')
print("=" * 55)

