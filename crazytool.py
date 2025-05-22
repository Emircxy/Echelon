
#!/usr/bin/env python3
import os
import random
import socket
import base64
import argparse
from colorama import Fore, init

init()  # Renkleri başlat

def print_banner():
    print(Fore.GREEN + """
  ____ ____      _   _   _     _   _ 
 / ___|  _ \    / \ | |_| |   | | | |
| |   | |_) |  / _ \| __| |   | |_| |
| |___|  _ <  / ___ \ |_| |___|  _  |
 \____|_| \_\/_/   \_\__|_____|_| |_|
    """ + Fore.RESET)

def get_ip(target):
    try:
        ip = socket.gethostbyname(target)
        print(Fore.BLUE + f"[IP Adresi] {target} → {ip}" + Fore.RESET)
    except:
        print(Fore.RED + "[Hata] Geçersiz URL/IP!" + Fore.RESET)

def mac_vendor(mac):
    vendors = {
        "00:00:0C": "Cisco",
        "00:1A:11": "HP",
        "00:1B:63": "Apple",
        "00:50:56": "VMware",
    }
    prefix = mac[:8].upper()
    vendor = vendors.get(prefix, "Bilinmiyor")
    print(Fore.YELLOW + f"[MAC Üretici] {mac} → {vendor}" + Fore.RESET)

def generate_password(length=12):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(length))
    print(Fore.CYAN + f"[Şifre] {password}" + Fore.RESET)

def fake_email():
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "protonmail.com"]
    name = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(8))
    email = f"{name}@{random.choice(domains)}"
    print(Fore.MAGENTA + f"[Fake Mail] {email}" + Fore.RESET)

def ascii_art(text):
    arts = {
        "cool": f"""
        ˁ˚ᴥ˚ˀ {text}
        """,
        "angry": f"""
        (╯°□°）╯︵ {text[::-1]}
        """
    }
    art = random.choice(list(arts.values()))
    print(Fore.GREEN + art + Fore.RESET)

def roll_dice():
    dice = random.randint(1, 6)
    print(Fore.RED + f"[Zar] 🎲 → {dice}" + Fore.RESET)

def reverse_text(text):
    reversed_text = text[::-1]
    print(Fore.BLUE + f"[Ters Yazı] {reversed_text}" + Fore.RESET)

def base64_encode(text):
    encoded = base64.b64encode(text.encode()).decode()
    print(Fore.YELLOW + f"[Base64] {encoded}" + Fore.RESET)

def wifi_list():
    if os.name == 'posix':
        os.system("nmcli dev wifi list")
    else:
        print(Fore.RED + "[Hata] Sadece Linux/Termux'ta çalışır!" + Fore.RESET)

def main():
    parser = argparse.ArgumentParser(description="CrazyTool - 9 Özellikli Eğlenceli Araç")
    parser.add_argument("-i", "--ip", help="Hedef site IP'sini bul (örnek: google.com)")
    parser.add_argument("-m", "--mac", help="MAC adresi üreticisini sorgula (örnek: 00:1A:11:XX:XX:XX)")
    parser.add_argument("-p", "--password", action="store_true", help="Rastgele şifre üret")
    parser.add_argument("-f", "--fake", action="store_true", help="Fake mail oluştur")
    parser.add_argument("-a", "--ascii", help="ASCII art oluştur (örnek: 'Merhaba')")
    parser.add_argument("-d", "--dice", action="store_true", help="Zar at")
    parser.add_argument("-r", "--reverse", help="Metni ters çevir (örnek: 'hello')")
    parser.add_argument("-b", "--base64", help="Metni Base64 ile şifrele (örnek: 'sifre')")
    parser.add_argument("-w", "--wifi", action="store_true", help="Wi-Fi ağlarını listele (Linux/Termux)")
    args = parser.parse_args()

    print_banner()

    if args.ip:
        get_ip(args.ip)
    if args.mac:
        mac_vendor(args.mac)
    if args.password:
        generate_password()
    if args.fake:
        fake_email()
    if args.ascii:
        ascii_art(args.ascii)
    if args.dice:
        roll_dice()
    if args.reverse:
        reverse_text(args.reverse)
    if args.base64:
        base64_encode(args.base64)
    if args.wifi:
        wifi_list()

if __name__ == "__main__":
    main()
