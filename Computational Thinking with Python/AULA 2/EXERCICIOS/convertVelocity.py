print("""                                                                                                                                                                                                    
                        ,--,                                                                            
       ,---.          ,--.'|                        ,--,         ,---,                  ,---,           
      /__./|          |  | :     ,---.            ,--.'|       ,---.'|                ,---.'|           
 ,---.;  ; |          :  : '    '   ,'\           |  |,        |   | :                |   | :           
/___/ \  | |   ,---.  |  ' |   /   /   |   ,---.  `--'_        |   | |   ,--.--.      |   | |   ,---.   
\   ;  \ ' |  /     \ '  | |  .   ; ,. :  /     \ ,' ,'|     ,--.__| |  /       \   ,--.__| |  /     \  
 \   \  \: | /    /  ||  | :  '   | |: : /    / ' '  | |    /   ,'   | .--.  .-. | /   ,'   | /    /  | 
  ;   \  ' ..    ' / |'  : |__'   | .; :.    ' /  |  | :   .   '  /  |  \__\/: . ..   '  /  |.    ' / | 
   \   \   ''   ;   /||  | '.'|   :    |'   ; :__ '  : |__ '   ; |:  |  ," .--.; |'   ; |:  |'   ;   /| 
    \   `  ;'   |  / |;  :    ;\   \  / '   | '.'||  | '.'||   | '/  ' /  /  ,.  ||   | '/  ''   |  / | 
     :   \ ||   :    ||  ,   /  `----'  |   :    :;  :    ;|   :    :|;  :   .'   \   :    :||   :    | 
      '---"  \   \  /  ---`-'            \   \  / |  ,   /  \   \  /  |  ,     .-./\   \  /   \   \  /  
              `----'                      `----'   ---`-'    `----'    `--`---'     `----'     `----'                                                                                                    
""")

kilometer_per_hour = input('Insira a velocidade em km/h (exemplo - 75,6): ')

kilometer_per_hour = float(kilometer_per_hour)
meter_per_hour = kilometer_per_hour * 1000
meter_per_seconds = kilometer_per_hour / 3.6

print(f'A velocidade em km/h é igual à {kilometer_per_hour}')
print(f'A velocidade em m/h é igual à {meter_per_hour}')
print(f'A velocidade em m/s é igual à {meter_per_seconds:.2f}')