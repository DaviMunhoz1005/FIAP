print("""                                                                  
          ____                                                                     
        ,'  , `.                                      ___                          
     ,-+-,.' _ |  ,--,                              ,--.'|_                        
  ,-+-. ;   , ||,--.'|         ,---,          ,--,  |  | :,'   ,---.               
 ,--.'|'   |  ;||  |,      ,-+-. /  |       ,'_ /|  :  : ' :  '   ,'\   .--.--.    
|   |  ,', |  ':`--'_     ,--.'|'   |  .--. |  | :.;__,'  /  /   /   | /  /    '   
|   | /  | |  ||,' ,'|   |   |  ,"' |,'_ /| :  . ||  |   |  .   ; ,. :|  :  /`./   
'   | :  | :  |,'  | |   |   | /  | ||  ' | |  . .:__,'| :  '   | |: :|  :  ;_     
;   . |  ; |--' |  | :   |   | |  | ||  | ' |  | |  '  : |__'   | .; : \  \    `.  
|   : |  | ,    '  : |__ |   | |  |/ :  | : ;  ; |  |  | '.'|   :    |  `----.   \ 
|   : '  |/     |  | '.'||   | |--'  '  :  `--'   \ ;  :    ;\   \  /  /  /`--'  / 
;   | |`-'      ;  :    ;|   |/      :  ,      .-./ |  ,   /  `----'  '--'.     /  
|   ;/          |  ,   / '---'        `--`----'      ---`-'             `--'---'   
'---'            ---`-'                                                                                                                                          
""")

quantity_minutes = input('Insira uma quantidade de minutos: ')
minutes_to_add = input('Insira a quantidade de minutos que quer adicionar: ')

quantity_minutes = int(quantity_minutes)
minutes_to_add = int(minutes_to_add)

total_minutes = quantity_minutes + minutes_to_add

hours = total_minutes // 60
minutes = total_minutes % 60

if hours > 0:
    print(f'A quantidade de tempo depois da adição é {hours} horas e {minutes} minutos')
else:
    print(f'A quantidade de tempo depois da adição é {minutes} minutos')