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
        print("Taraflardan en az biri istemediginden program sonlandiriliyor.")
    
    return tekrar


def tas_kagit_makas_ABDULBAKI_TOPCU():
    
    global player_point
    global computer_point
    global tour
    
    choices=["tas","kagit","makas"]
    print(str(game)+".oyun "+str(tour) + ".tur ")

    player=input("Lutfen seciminizi yapiniz (tas-kagit-makas):").lower().strip()
    while player not in choices:
        print("Dikkat! Dogru sekilde yazdiginizdan emin olun.")
        player = input("Lutfen seciminizi yapınız (tas-kagit-makas):").lower().strip()
    
        
    print(f"\n(Oyuncu){player.capitalize()}.")
    computer = choices[randint(0, 2)]
    print(f"(Bilgisayar){computer.capitalize()}.\n")
    
    if player == "tas" and computer == "makas" or player == "makas" and computer == "kagit" or player == "kagit" and computer == "tas":  
        player_point += 1
        print(f"Oyuncu puan kazandi. Mevcut durum-> Oyuncu:{player_point} Bilgisayar:{computer_point}\n")
    
    elif computer == "tas" and player == "makas" or computer == "makas" and player == "kagit" or computer == "kagit" and player == "tas":
        computer_point += 1
        print(f"Bilgisayar puan kazandi. Mevcut durum-> Bilgisayar:{computer_point} Oyuncu:{player_point}\n")
    
    else:
        print("Beraberlik. Bu turun kazanani yok.\n")
    
    tour += 1
     
    
    
    
game = 1
tour = 1
player_point = 0
computer_point = 0
playerGamePoint = 0
computerGamePoint = 0

print("""TAS KAGIT MAKAS'A HOS GELDINIZ!
      
Kurallar:
          1- Tas Makasi kirar.
          2- Makas Kagiti keser.
          3- Kagit Tasi sarar.
          4- Iki tarafin da ayni seyi oynamasi halinde durum degismez.
          5- Her oyunda ilk iki turu kazanan oyunu da kazanir.
          6- Secim yapilirken 'tas-kagit-makas' sekilende yazilmalidir.
          7- Oyun sonunda devam edip etmek istemediginiz sorulacaktır. 
             Karsilasmaya devam etmek istediginizi belirtmek icin 'y',
             karsilasmayi bitirmek icin 'n' yaziniz.\n\n""")


while player_point < 2 or computer_point < 2:
    
    tas_kagit_makas_ABDULBAKI_TOPCU()
    
    if player_point > 1:
        playerGamePoint += 1
        print(f"OYUN BITTI. OYUNCU KAZANDI. TEBRIKLER!\nGENEL SONUC --> OYUNUCU:{playerGamePoint} BILGISAYAR:{computerGamePoint}".upper())
        
        if tekrar_sorgusu() == 0:
            break
            
    elif computer_point > 1:
        computerGamePoint += 1
        print(f"OYUN BITTI. BILGISAYAR KAZANDI.TEBRIKLER!\nGENEL SONUÇ --> OYUNCU:{playerGamePoint} BILGISAYAR:{computerGamePoint}".upper())
        if tekrar_sorgusu() == 0:
            break
    