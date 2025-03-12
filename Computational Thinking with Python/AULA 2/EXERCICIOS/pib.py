print("""                         
,-.----.                       
\    /  \     ,---,    ,---,.  
|   :    \ ,`--.' |  ,'  .'  \ 
|   |  .\ :|   :  :,---.' .' | 
.   :  |: |:   |  '|   |  |: | 
|   |   \ :|   :  |:   :  :  / 
|   : .   /'   '  ;:   |    ;  
;   | |`-' |   |  ||   :     \ 
|   | ;    '   :  ;|   |   . | 
:   ' |    |   |  ''   :  '; | 
:   : :    '   :  ||   |  | ;  
|   | :    ;   |.' |   :   /   
`---'.|    '---'   |   | ,'    
  `---`            `----'                                 
""")

country_pib = input('Insira o PIB de um país: ')
country_name = input('Insira o nome do país: ')

country_pib = float(country_pib)
actual_year = 2025

print(f'No ano de {actual_year}, o PIB do {country_name} era {country_pib}')
actual_year += 1

for _ in range(4):
    percent_new_year = input('Quanto percentual ganhou ou perdeu no próximo ano (exemplo - 20,4)? ')
    gain_or_loss = input(f'Ganhou ou perdeu {percent_new_year}% (exemplo - 1 ou 0)? ')

    percent_new_year = float(percent_new_year) / 100

    if gain_or_loss == "1":
        country_pib += country_pib * percent_new_year
    elif gain_or_loss == "0":
        country_pib -= country_pib * percent_new_year
    else:
        print('Valor Inválido na pergunta \'Ganhou ou perdeu\'')

    print(f'No ano de {actual_year}, o PIB do {country_name} era {country_pib:.2f}')
    actual_year += 1