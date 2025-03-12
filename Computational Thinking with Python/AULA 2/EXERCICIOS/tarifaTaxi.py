print("""
        ,----,                                                               ,----,                               
      ,/   .`|                                                             ,/   .`|                               
    ,`   .'  :                                                           ,`   .'  :                               
  ;    ;     /                    ,--,     .--.,                       ;    ;     /                       ,--,    
.'___,/    ,'            __  ,-.,--.'|   ,--.'  \                    .'___,/    ,'                      ,--.'|    
|    :     |           ,' ,'/ /||  |,    |  | /\/                    |    :     |             ,--,  ,--,|  |,     
;    |.';  ;  ,--.--.  '  | |' |`--'_    :  : :    ,--.--.           ;    |.';  ;  ,--.--.    |'. \/ .`|`--'_     
`----'  |  | /       \ |  |   ,',' ,'|   :  | |-, /       \          `----'  |  | /       \   '  \/  / ;,' ,'|    
    '   :  ;.--.  .-. |'  :  /  '  | |   |  : :/|.--.  .-. |             '   :  ;.--.  .-. |   \  \.' / '  | |    
    |   |  ' \__\/: . .|  | '   |  | :   |  |  .' \__\/: . .             |   |  ' \__\/: . .    \  ;  ; |  | :    
    '   :  | ," .--.; |;  : |   '  : |__ '  : '   ," .--.; |             '   :  | ," .--.; |   / \  \  \'  : |__  
    ;   |.' /  /  ,.  ||  , ;   |  | '.'||  | |  /  /  ,.  |             ;   |.' /  /  ,.  | ./__;   ;  \  | '.'| 
    '---'  ;  :   .'   \---'    ;  :    ;|  : \ ;  :   .'   \            '---'  ;  :   .'   \|   :/\  \ ;  :    ; 
           |  ,     .-./        |  ,   / |  |,' |  ,     .-./                   |  ,     .-./`---'  `--`|  ,   /  
            `--`---'             ---`-'  `--'    `--`---'                        `--`---'                ---`-'                                                                                                                   
""")

miles_wheels = input('Insira o número de km rodados (exemplo - 20,5): ').replace(',', '.')
hours_stop = input('Insira o número de horas esperadas parado (exemplo - 2,5): ').replace(',', '.')
# minutes_stop = input('Insira o número de minutos esperados parado (exemplo - 150)').replace(',', '.')

miles_wheels = float(miles_wheels)
stopped_time = float(hours_stop) # float(minutes_stop) / 60

fare = 5.5 + (2.8 * miles_wheels) + (stopped_time * 44)

print(f'A tarifa a ser paga será no valor de R${fare:.2f}')
