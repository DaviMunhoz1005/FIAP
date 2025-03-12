def display_platelets(unit_of_measurement, quantity):
    print(f'O número de plaquetas por {unit_of_measurement} é {quantity:.2f}')

print(r"""                                                                                                                                                                                          
,-.----.                                                                                              
\    /  \    ,--,                                                     ___                             
|   :    \ ,--.'|                ,----.                             ,--.'|_                           
|   |  .\ :|  | :               /   /  \-.         ,--,             |  | :,'                          
.   :  |: |:  : '              |   :    :|       ,'_ /|             :  : ' :               .--.--.    
|   |   \ :|  ' |     ,--.--.  |   | .\  .  .--. |  | :    ,---.  .;__,'  /    ,--.--.    /  /    '   
|   : .   /'  | |    /       \ .   ; |:  |,'_ /| :  . |   /     \ |  |   |    /       \  |  :  /`./   
;   | |`-' |  | :   .--.  .-. |'   .  \  ||  ' | |  . .  /    /  |:__,'| :   .--.  .-. | |  :  ;_     
|   | ;    '  : |__  \__\/: . . \   `.   ||  | ' |  | | .    ' / |  '  : |__  \__\/: . .  \  \    `.  
:   ' |    |  | '.'| ," .--.; |  `--'""| |:  | : ;  ; | '   ;   /|  |  | '.'| ," .--.; |   `----.   \ 
:   : :    ;  :    ;/  /  ,.  |    |   | |'  :  `--'   \'   |  / |  ;  :    ;/  /  ,.  |  /  /`--'  / 
|   | :    |  ,   /;  :   .'   \   |   | ::  ,      .-./|   :    |  |  ,   /;  :   .'   \'--'.     /  
`---'.|     ---`-' |  ,     .-./   `---'.| `--`----'     \   \  /    ---`-' |  ,     .-./  `--'---'   
  `---`             `--`---'         `---`                `----'             `--`---'                                                                                                                                              
""")

platelets_per_liter = input('Insira o número de plaquetas por litro: ')

platelets_per_liter = float(platelets_per_liter)
platelets_per_deciliter = platelets_per_liter * 10
platelets_per_milliliter = platelets_per_deciliter * 100

display_platelets("litro", platelets_per_liter)
display_platelets("decilitro", platelets_per_deciliter)
display_platelets("mililítro", platelets_per_milliliter)
