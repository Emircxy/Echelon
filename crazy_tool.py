#!/usr/bin/env python3
import os
import random
import socket
import base64
from colorama import Fore, init

init()  # Renkleri başlat

def print_banner():
    print(Fore.RED + """
     ______     __  __     ______     ______    
    /\  ___\   /\ \_\ \   /\  ___\   /\  == \   
    \ \ \____  \ \  __ \  \ \  __\   \ \  __<   
     \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
      \/_____/   \/_/\/_/   \/_____/   \/_/ /_/ 
    """ + Fore.RESET)

def menu():
    print(Fore.YELLOW + "\n" + "═"*50 + Fore.RESET)
    print(Fore.CYAN + "1. IP Sorgula")
    print("2. MAC Üretici Bul")
    print("3. Şifre Üret")
    print("4. Fake Mail Oluştur")
    print("5. ASCII Art")
    print("6. Zar At")
    print("7. Tersine Yazı")
    print("8. Base64 Şifrele/Çöz")
    print("9. Wi-Fi Ağlarını Listele" + Fore.RESET)
    print(Fore.YELLOW + "═"*50 + Fore.RESET)

def get_ip():
    target = input(Fore.GREEN + "Hedef URL/IP: " + Fore.RESET)
    try:
        ip = socket.gethostbyname(target)
        print(Fore.BLUE + f"[+] IP: {ip}" + Fore.RESET)
    except:
        print(Fore.RED + "[!] Geçersiz URL/IP!" + Fore.RESET)

def mac_vendor():
    mac = input(Fore.GREEN + "MAC Adresi (00:1A:2B:...): " + Fore.RESET)
    vendors = {"00:00:0C": "Cisco", "00:1A:11": "HP"}
    prefix = mac[:8].upper()
    print(Fore.YELLOW + f"[+] Üretici: {vendors.get(prefix, 'Bilinmiyor')}" + Fore.RESET)

# Diğer fonksiyonlar (generate_password, fake_email, vb.) aynı kalacak.
# Önceki koddan kopyalayıp yapıştır.

def main():
    print_banner()
    while True:
        menu()
        secim = input(Fore.MAGENTA + "Seçim (1-9/Çıkış=q): " + Fore.RESET)
        
        if secim == "1":
            get_ip()
        elif secim == "2":
            mac_vendor()
        elif secim == "3":
            generate_password()
        elif secim == "4":
            fake_email()
        elif secim == "5":
            text = input(Fore.GREEN + "ASCII için metin: " + Fore.RESET)
            ascii_art(text)
        elif secim == "6":
            roll_dice()
        elif secim == "7":
            text = input(Fore.GREEN + "Ters çevrilecek metin: " + Fore.RESET)
            reverse_text(text)
        elif secim == "8":
            text = input(Fore.GREEN + "Base64 metin: " + Fore.RESET)
            base64_encode(text)
        elif secim == "9":
            wifi_list()
        elif secim.lower() == "q":
            print(Fore.RED + "Çıkış yapılıyor..." + Fore.RESET)
            break
        else:
            print(Fore.RED + "[!] Geçersiz seçim! (1-9 arası gir)" + Fore.RESET)

if __name__ == "__main__":
    main()
