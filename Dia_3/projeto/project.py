# pylint: disable-all

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem-vindo à Ilha do Tesouro.")
print("A sua missão é encontrar o tesouro.")

primeira_escolha = input("Esquerda ou direita?\nDigite Direita/Esquerda: ").lower()
if primeira_escolha == "direita":
  print('''                      -     =    .--._
                - - ~_=  =~_- = - `.  `-.
              ==~_ = =_  ~ -   =  .-'    `.
            --=~_ - ~  == - =   .'      _..:._
           ---=~ _~  = =-  =   `.  .--.'      `.
          --=_-=- ~= _ - =  -  _.'  `.      .--.:
            -=_~ -- = =  ~-  .'      :     :    :
             -=-_ ~=  = - _-`--.     :  .--:    D
               -=~ _=  =  -~_=  `;  .'.:   ,`---'@
             --=_= = ~-   -=   .'  .'  `._ `-.__.'
            --== ~_ - =  =-  .'  .'     _.`---'
           --=~_= = - = ~  .'--''   .   `-..__.--.
             --==~ _= - ~-=  =-~_-   `-..___(  ===;
          --==~_==- =__ ~-=  - -    .'       `---'
  ''')
  print("Sonic encontrou o tesouro antes de você, tente novamente.")
elif primeira_escolha == 'esquerda':
  print('''
   _                                                           
  | |                                                          
  | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ __ ___   __ _ _ __  
  | __| '__/ _ \/ _` / __| | | | '__/ _ \ '_ ` _ \ / _` | '_ \ 
  | |_| | |  __/ (_| \__ \ |_| | | |  __/ | | | | | (_| | |_) |
  \__|_|  \___|\__,_|___/\__,_|_|  \___|_| |_| |_|\__,_| .__/ 
                                                        | |    
                                                        |_| 
  ''')
  print("Legal, você passou para o próximo nível!")

  segunda_escolha = input("O seu mapa mostra que você precisa chegar à Ilha do Tesouro, você pode esperar para embarcar em um navio ou nadar através do mar, escolha um.\nDigite Nadar/Esperar: ").lower()
  if segunda_escolha == "nadar":
    print('''
                    (`.
                    \ `.
                      )  `._..---._
    \`.       __...---`         o  )
    \ `._,--'           ,    ___,'
      ) ,-._          \  )   _,-'
    /,'    ``--.._____\/--''
        ''')
    print("Infelizmente, você foi comido por um Grande Tubarão Branco, tente novamente.")
  elif segunda_escolha == "esperar":
    print("Ótimo, você passou para o próximo nível, você é muito bom nisso!")
    print ("Bem-vindo a:")
    print ('''
     _                                     _     _                 _ 
    | |                                   (_)   | |               | |
    | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
    | __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
    | |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
    \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
    ''')

    terceira_escolha = input("Agora que você chegou à Ilha do Tesouro, você pode cavar ou procurar na caverna. \n Digite Cavar/Caverna: ").lower()
    if terceira_escolha == "cavar":
      print("Você encontrou o tesouro, você venceu!")
    elif terceira_escolha == "caverna":
      print('''
      _                     
      | |                    
      | |__   ___  __ _ _ __ 
      | '_ \ / _ \/ _` | '__|
      | |_) |  __/ (_| | |   
      |_.__/ \___|\__,_|_|   
                  ''')
      print("Você foi comido por um urso, fim de jogo.")
