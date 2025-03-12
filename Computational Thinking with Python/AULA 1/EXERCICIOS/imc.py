print(r"""                               
                  ____              
   ,---,        ,'  , `.  ,----..   
,`--.' |     ,-+-,.' _ | /   /   \  
|   :  :  ,-+-. ;   , |||   :     : 
:   |  ' ,--.'|'   |  ;|.   |  ;. / 
|   :  ||   |  ,', |  ':.   ; /--`  
'   '  ;|   | /  | |  ||;   | ;     
|   |  |'   | :  | :  |,|   : |     
'   :  ;;   . |  ; |--' .   | '___  
|   |  '|   : |  | ,    '   ; : .'| 
'   :  ||   : '  |/     '   | '/  : 
;   |.' ;   | |`-'      |   :    /  
'---'   |   ;/           \   \ .'   
        '---'             `---`     
""")

height = input('Insira sua altura (exemplo - 1,70): ').replace(',', '.')
weight = input('Insira seu peso (exemplo - 75,3): ').replace(',', '.')

height = float(height)
weight = float(weight)

imc = weight / (height * height)

print(f'Seu IMC é igual a: {imc:.2f}')
