#!/usr/bin/env python3
import os
import random
import socket
import base64
import json
import requests
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
    print("9. Wi-Fi Ağlarını Listele (Termux)" + Fore.RESET)
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
    try:
        response = requests.get(f"https://api.macvendors.com/{mac}")
        print(Fore.YELLOW + f"[+] Üretici: {response.text}" + Fore.RESET)
    except:
        print(Fore.RED + "[!] API hatası!" + Fore.RESET)

def generate_password():
    length = int(input(Fore.GREEN + "Şifre uzunluğu: " + Fore.RESET))
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(length))
    print(Fore.CYAN + f"[+] Şifre: {password}" + Fore.RESET)

def fake_email():
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "protonmail.com"]
    name = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(8))
    email = f"{name}@{random.choice(domains)}"
    print(Fore.MAGENTA + f"[+] Fake Mail: {email}" + Fore.RESET)

def ascii_art():
    text = input(Fore.GREEN + "ASCII için metin: " + Fore.RESET)
    arts = [
        f" ︻デ═一 {text}",
        f"(っ◔◡◔)っ {text}",
        f"˚✧₊⁎ {text} ⁎⁺˳✧༚"
    ]
    print(Fore.GREEN + random.choice(arts) + Fore.RESET)

def roll_dice():
    dice = random.randint(1, 6)
    print(Fore.RED + f"[+] Zar: {dice} 🎲" + Fore.RESET)

def reverse_text():
    text = input(Fore.GREEN + "Ters çevrilecek metin: " + Fore.RESET)
    print(Fore.BLUE + f"[+] Ters: {text[::-1]}" + Fore.RESET)

def base64_encode():
    text = input(Fore.GREEN + "Metin: " + Fore.RESET)
    encoded = base64.b64encode(text.encode()).decode()
    print(Fore.YELLOW + f"[+] Base64: {encoded}" + Fore.RESET)

def wifi_list():
    try:
        if os.path.exists("/data/data/com.termux/files/usr/bin/termux-wifi-scaninfo"):
            os.system("termux-wifi-scaninfo")
        else:
            print(Fore.RED + "[!] Termux API yüklü değil! Şu komutu çalıştır:" + Fore.RESET)
            print("pkg install termux-api")
    except:
        print(Fore.RED + "[!] Bu özellik sadece Termux'ta çalışır!" + Fore.RESET)

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
            ascii_art()
        elif secim == "6":
            roll_dice()
        elif secim == "7":
            reverse_text()
        elif secim == "8":
            base64_encode()
        elif secim == "9":
            wifi_list()
        elif secim.lower() == "q":
            print(Fore.RED + "Çıkış yapılıyor..." + Fore.RESET)
            break
        else:
            print(Fore.RED + "[!] Geçersiz seçim! (1-9 arası gir)" + Fore.RESET)

if __name__ == "__main__":
    main()
