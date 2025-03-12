print("""                                                                                                                                                                                          
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
platelets_per_mililiter = platelets_per_deciliter * 100

print(f'O número de plaquetas por litro é {platelets_per_liter:.2f}')
print(f'O número de plaquetas por decilitro é {platelets_per_deciliter:.2f}')
print(f'O número de plaquetas por mililitro é {platelets_per_mililiter:.2f}')
