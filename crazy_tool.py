#!/usr/bin/env python3
import os
import random
import socket
import base64
import json
import requests
import time
import subprocess
from colorama import Fore, init, Back, Style

init(autoreset=True)  # Renkleri başlat

# Renkli mesaj fonksiyonları
def print_error(msg):
    print(Fore.RED + f"[!] {msg}" + Fore.RESET)

def print_success(msg):
    print(Fore.GREEN + f"[+] {msg}" + Fore.RESET)

def print_info(msg):
    print(Fore.CYAN + f"[*] {msg}" + Fore.RESET)

def print_warning(msg):
    print(Fore.YELLOW + f"[!] {msg}" + Fore.RESET)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print(Fore.RED + Style.BRIGHT + """
    ▓█████▄  ▄▄▄       ██▀███   ██ ▄█▀
    ▒██▀ ██▌▒████▄    ▓██ ▒ ██▒ ██▄█▒ 
    ░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░ 
    ░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄ 
    ░▒████▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄
     ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒
     ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░
     ░ ░  ░   ░   ▒     ░░   ░ ░ ░░ ░ 
       ░          ░  ░   ░     ░  ░   
     ░                                
    """ + Fore.RESET)
    print(Fore.CYAN + ">"*25 + " v3.0 - Termux/Kali " + "<"*25 + "\n" + Fore.RESET)

def menu():
    print(Back.BLACK + Fore.WHITE + Style.BRIGHT + "\n╔═══════════════════════ ECHELON PRO ═══════════════════════╗")
    print("║ " + Fore.CYAN + "1. IP Sorgula       2. MAC Üretici Bul     3. Şifre Üret     ║")
    print("║ " + Fore.GREEN + "4. Fake Mail        5. ASCII Art          6. Zar At         ║")
    print("║ " + Fore.YELLOW + "7. Ters Yazı        8. Base64 İşlemleri   9. Wi-Fi Listele  ║")
    print("║ " + Fore.MAGENTA + "10. URL Kısalt      11. QR Kod Oluştur    12. Sistem Bilgisi ║")
    print("║ " + Fore.BLUE + "13. Dosya Şifrele    14. Konum Bul         15. Çıkış (q)     ║")
    print("╚═══════════════════════════════════════════════════════════════════╝" + Fore.RESET)

# Geliştirilmiş Wi-Fi Listeleme (Rootsuz)
def wifi_list():
    try:
        if os.path.exists("/data/data/com.termux/files/usr/bin/termux-wifi-scaninfo"):
            result = subprocess.run(["termux-wifi-scaninfo"], capture_output=True, text=True)
            if result.returncode == 0:
                try:
                    wifi_data = json.loads(result.stdout)
                    print(Fore.CYAN + "\n{:<20} {:<15} {:<10} {:<5}".format("SSID", "BSSID", "Sinyal", "Kanal"))
                    print("-"*50 + Fore.RESET)
                    for network in wifi_data:
                        print("{:<20} {:<15} {:<10} {:<5}".format(
                            network.get("ssid", "Bilinmiyor"),
                            network.get("bssid", "Bilinmiyor"),
                            str(network.get("rssi", 0)) + " dBm",
                            network.get("frequency", 0)
                        ))
                except json.JSONDecodeError:
                    print_error("Wi-Fi verileri okunamadı")
            else:
                print_error("Wi-Fi taraması başarısız. Termux API izni verildi mi?")
        else:
            print_error("Termux API yüklü değil! 'pkg install termux-api'")
    except Exception as e:
        print_error(f"Wi-Fi hatası: {str(e)}")

# Yeni Özellik: Konum Bulma
def get_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        print_success(f"IP: {data['ip']}")
        print_success(f"Ülke: {data.get('country', 'Bilinmiyor')}")
        print_success(f"Şehir: {data.get('city', 'Bilinmiyor')}")
        print_success(f"Konum: {data.get('loc', 'Bilinmiyor')}")
        print_info("Haritada görüntüle: https://www.google.com/maps?q=" + data.get('loc', ''))
    except Exception as e:
        print_error(f"Konum bilgisi alınamadı: {str(e)}")

# Yeni Özellik: Dosya Şifreleme
def encrypt_file():
    file_path = input(Fore.GREEN + "Şifrelenecek dosya yolu: " + Fore.RESET)
    if not os.path.exists(file_path):
        print_error("Dosya bulunamadı!")
        return
    
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        encoded = base64.b64encode(data)
        
        new_path = file_path + ".enc"
        with open(new_path, 'wb') as f:
            f.write(encoded)
        print_success(f"Dosya şifrelendi: {new_path}")
    except Exception as e:
        print_error(f"Şifreleme hatası: {str(e)}")

# Diğer fonksiyonlar (get_ip, mac_vendor vb.) öncekiyle aynı ama hata mesajları güncellendi

def main():
    while True:
        clear_screen()
        print_banner()
        menu()
        
        try:
            secim = input(Fore.MAGENTA + Style.BRIGHT + "\n[?] Seçiminiz (1-15): " + Fore.RESET)
            
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
                base64_operations()  # Yeni: Hem encode hem decode
            elif secim == "9":
                wifi_list()
            elif secim == "10":
                shorten_url()
            elif secim == "11":
                qr_generator()
            elif secim == "12":
                system_info()  # Yeni sistem bilgisi
            elif secim == "13":
                encrypt_file()
            elif secim == "14":
                get_location()
            elif secim in ["15", "q"]:
                print(Fore.RED + "\n[!] Çıkış yapılıyor..." + Fore.RESET)
                break
            else:
                print_error("Geçersiz seçim!")
            
            input(Fore.YELLOW + "\n[!] Devam etmek için Enter..." + Fore.RESET)
        except KeyboardInterrupt:
            print_error("\nİşlem iptal edildi!")
            time.sleep(1)
        except Exception as e:
            print_error(f"Beklenmeyen hata: {str(e)}")
            time.sleep(2)

if __name__ == "__main__":
    main()
