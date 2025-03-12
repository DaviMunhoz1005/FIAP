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

debt = input('Por favor, insira o valor da sua dívida (exemplo - 1000.50): ').replace(',', '.')
fees = input('Insira a porcentagem de juros que incidem mensalmente (exemplo - 20.12): ').replace(',', '.')
num_months = input('Insira o número de meses que você quer saber (exemplo - 6 para 6 meses): ')

debt = float(debt)
fees = float(fees)
num_months = int(num_months)

if debt <= 0 or fees <= 0 or num_months <= 0:
    print("Por favor, insira valores positivos e válidos para a dívida, juros e número de meses.")
else:
    accumulated_debt = debt
    print("\nAqui está o seu cálculo de dívida acumulada:")
    for i in range(1, num_months + 1):
        accumulated_debt += accumulated_debt * (fees / 100)
        print(f'A dívida acumulada no {i}º mês será de R$ {accumulated_debt:.2f}')
