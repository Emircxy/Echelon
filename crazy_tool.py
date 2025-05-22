#!/usr/bin/env python3
import os
import random
import socket
import base64
import json
import requests
import time
from colorama import Fore, init, Back

init(autoreset=True)  # Renkleri başlat

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print(Fore.RED + """
    ███████╗ ██████╗██╗  ██╗███████╗██╗      ██████╗ ███╗   ██╗
    ██╔════╝██╔════╝██║  ██║██╔════╝██║     ██╔═══██╗████╗  ██║
    █████╗  ██║     ███████║█████╗  ██║     ██║   ██║██╔██╗ ██║
    ██╔══╝  ██║     ██╔══██║██╔══╝  ██║     ██║   ██║██║╚██╗██║
    ███████╗╚██████╗██║  ██║███████╗███████╗╚██████╔╝██║ ╚████║
    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
    """ + Fore.RESET)
    print(Fore.CYAN + ">"*20 + " v2.0 - Termux/Kali " + "<"*20 + "\n" + Fore.RESET)

def menu():
    print(Back.BLACK + Fore.WHITE + "\n╔═══════════════════════ ECHELON MENÜ ═══════════════════════╗")
    print("║ " + Fore.CYAN + "1. IP Sorgula       2. MAC Üretici Bul     3. Şifre Üret     ║")
    print("║ " + Fore.GREEN + "4. Fake Mail        5. ASCII Art          6. Zar At         ║")
    print("║ " + Fore.YELLOW + "7. Ters Yazı        8. Base64 Şifrele     9. Wi-Fi Listele  ║")
    print("║ " + Fore.MAGENTA + "10. URL Kısalt      11. QR Kod Oluştur    12. Çıkış (q)     ║")
    print("╚═══════════════════════════════════════════════════════════════════╝" + Fore.RESET)

# Yeni Özellikler
def shorten_url():
    url = input(Fore.GREEN + "Kısaltılacak URL: " + Fore.RESET)
    try:
        response = requests.get(f"https://tinyurl.com/api-create.php?url={url}")
        print(Fore.BLUE + f"[+] Kısaltılmış URL: {response.text}" + Fore.RESET)
    except:
        print(Fore.RED + "[!] Hata oluştu!" + Fore.RESET)

def qr_generator():
    text = input(Fore.GREEN + "QR için metin/URL: " + Fore.RESET)
    try:
        os.system(f"qrencode -t ANSIUTF8 '{text}'")
    except:
        print(Fore.RED + "[!] qrencode kurulu değil! 'pkg install qrencode'" + Fore.RESET)

# Diğer fonksiyonlar (get_ip, mac_vendor vb.) öncekiyle aynı

def main():
    while True:
        clear_screen()
        print_banner()
        menu()
        
        secim = input(Fore.MAGENTA + "\n[?] Seçiminiz (1-12): " + Fore.RESET)
        
        if secim == "1":
            get_ip()
        elif secim == "2":
            mac_vendor()
        elif secim == "3":
            generate_password()
        elif secim == "4":
            fake_email()
        elif secim == "5":
            ascii_art()
        elif secim == "6":
            roll_dice()
        elif secim == "7":
            reverse_text()
        elif secim == "8":
            base64_encode()
        elif secim == "9":
            wifi_list()
        elif secim == "10":
            shorten_url()
        elif secim == "11":
            qr_generator()
        elif secim in ["12", "q"]:
            print(Fore.RED + "\n[!] Çıkış yapılıyor..." + Fore.RESET)
            break
        else:
            print(Fore.RED + "[!] Geçersiz seçim!" + Fore.RESET)
        
        input(Fore.YELLOW + "\n[!] Devam etmek için Enter..." + Fore.RESET)

if __name__ == "__main__":
    main()
