# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:18:21 2024
tas-kagıt-makas 
@author: HP
"""
from random import randint

def tekrar_sorgusu():
    tekrar = 0
    global game
    global tour
    global player_point
    global computer_point
    
    replayP = input("(Oyuncu)Yeniden oynamak ister misiniz? (y/n)\n").lower().strip()
    while replayP not in ["y","n"]:
        print("Dikkat! Dogru sekilde yazdiginizdan emin olun.")
        replayP = input("(Oyuncu)Yeniden oynamak ister misiniz? (y/n)\n").lower().strip()
        
    replayC = ["y","n"][randint(0, 1)]
    print(f"(Bilgisayar)Yeniden oynamak ister misiniz? (y/n)\n{replayC}")
    if replayC == "y" and replayP == "y":
        game += 1
        tour = 1
        player_point = 0
        computer_point = 0
        tekrar = 1
    else:
        print("Taraaflardan en az biri istemediğinden program sonlandırılıyor.")
    
    return tekrar


def tas_kagit_makas_ABDULBAKİ_TOPCU():
    
    global player_point
    global computer_point
    global tour
    
    choices=["tas","kagit","makas"]
    print(str(game)+".oyun "+str(tour) + ".tur ")

    player=input("Lütfen seçiminizi yapınız (tas-kagit-makas):").lower().strip()
    while player not in choices:
        print("Dikkat! Doğru şekilde yazdiğinizdan emin olun.")
        player = input("Lütfen seçiminizi yapınız (tas-kagit-makas):").lower().strip()
    
        
    print(f"\n(Oyuncu){player.capitalize()}.")
    computer = choices[randint(0, 2)]
    print(f"(Bilgisayar){computer.capitalize()}.\n")
    
    if player == "tas" and computer == "makas" or player == "makas" and computer == "kagit" or player == "kagit" and computer == "tas":  
        player_point += 1
        print(f"Oyuncu puan kazandı. Mevcut durum-> Oyuncu:{player_point} Bilgisayar:{computer_point}\n")
    
    elif computer == "tas" and player == "makas" or computer == "makas" and player == "kagit" or computer == "kagit" and player == "tas":
        computer_point += 1
        print(f"Bilgisayar puan kazandı. Mevcut durum-> Bilgisayar:{computer_point} Oyuncu:{player_point}\n")
    
    else:
        print("Beraberlik. Bu turun kazananı yok.\n")
    
    tour += 1
     
    
    
    
game = 1
tour = 1
player_point = 0
computer_point = 0
playerGamePoint = 0
computerGamePoint = 0

print("""TAŞ KAĞIT MAKAS'A HOŞ GELDİNİZ!
      
Kurallar:
          1- Taş Makası kırar.
          2- Makas Kağıtı keser.
          3- Kağıt Taşı sarar.
          4- İki tarafın da aynı şeyi oynaması halinde durum değişmez.
          5- Her oyunda ilk iki turu kazanan oyunu da kazanır.
          6- Seçim yapılırken 'tas-kagit-makas' şekilende yazılmalıdır.
          7- Oyun sonunda devam edip etmek istemediğiniz sorulacaktır. 
             Karşılaşmaya devam etmek istediğinizi belirtmek için 'y',
             karşılaşmayı bitirmek için 'n' yazınız.\n\n""")


while player_point < 2 or computer_point < 2:
    
    tas_kagit_makas_ABDULBAKİ_TOPCU()
    
    if player_point > 1:
        playerGamePoint += 1
        print(f"OYUN BİTTİ.OYUNCU KAZANDI.TEBRİKLER!\nGENEL SONUÇ --> OYUNUCU:{playerGamePoint} BİLGİSAYAR:{computerGamePoint}".upper())
        
        if tekrar_sorgusu() == 0:
            break
            
    elif computer_point > 1:
        computerGamePoint += 1
        print(f"OYUN BİTTİ.BİLGİSAYAR KAZANDI.TEBRİKLER!\nGENEL SONUÇ --> OYUNCU:{playerGamePoint} BİLGİSAYAR:{computerGamePoint}".upper())
        if tekrar_sorgusu() == 0:
            break
    