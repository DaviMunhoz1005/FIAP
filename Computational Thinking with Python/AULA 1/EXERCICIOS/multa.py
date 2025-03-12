print("""                                                                                                                                                 
          ____                                              
        ,'  , `.                ,--,    ___                 
     ,-+-,.' _ |              ,--.'|  ,--.'|_               
  ,-+-. ;   , ||         ,--, |  | :  |  | :,'              
 ,--.'|'   |  ;|       ,'_ /| :  : '  :  : ' :              
|   |  ,', |  ':  .--. |  | : |  ' |.;__,'  /    ,--.--.    
|   | /  | |  ||,'_ /| :  . | '  | ||  |   |    /       \   
'   | :  | :  |,|  ' | |  . . |  | ::__,'| :   .--.  .-. |  
;   . |  ; |--' |  | ' |  | | '  : |__'  : |__  \__\/: . .  
|   : |  | ,    :  | : ;  ; | |  | '.'|  | '.'| ," .--.; |  
|   : '  |/     '  :  `--'   \;  :    ;  :    ;/  /  ,.  |  
;   | |`-'      :  ,      .-./|  ,   /|  ,   /;  :   .'   \ 
|   ;/           `--`----'     ---`-'  ---`-' |  ,     .-./ 
'---'                                          `--`---'                                                                                             
""")

name = input('Insira o nome da pessoa: ')
value_fine = input('Insira o valor da multa (exemplo - 249,99):').replace(',', '.')

value_fine = float(value_fine)

print(f"""
Prezado(a) {name},
Informamos que foi registrada uma multa em seu nome no valor de R$ {value_fine:.2f}, referente à excesso de velocidade. Solicitamos que o pagamento seja efetuado para evitar encargos adicionais.
Caso precise de mais informações, estamos à disposição.
Atenciosamente,
Davi Munhoz
(11) 93425-0859
""")