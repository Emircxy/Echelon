import os
import socket
import subprocess
import platform
import sys

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print(r"""
███████╗ ██████╗  ██████╗██╗  ██╗ ██████╗ ██╗      ██████╗ ██╗   ██╗
██╔════╝██╔═══██╗██╔════╝██║ ██╔╝██╔═══██╗██║     ██╔═══██╗██║   ██║
█████╗  ██║   ██║██║     █████╔╝ ██║   ██║██║     ██║   ██║██║   ██║
██╔══╝  ██║   ██║██║     ██╔═██╗ ██║   ██║██║     ██║   ██║██║   ██║
███████╗╚██████╔╝╚██████╗██║  ██╗╚██████╔╝███████╗╚██████╔╝╚██████╔╝
╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ 
    """)

def get_ip():
    site = input("Site adresi girin (örnek: google.com): ")
    try:
        ip = socket.gethostbyname(site)
        print(f"{site} IP adresi: {ip}")
    except Exception as e:
        print("IP adresi bulunamadı:", e)

def ping_site():
    site = input("Ping atılacak siteyi girin: ")
    param = '-c' if os.name == 'posix' else '-n'
    subprocess.call(['ping', param, '4', site])

def port_scan():
    site = input("Port taraması yapılacak site/IP: ")
    start_port = int(input("Başlangıç portu: "))
    end_port = int(input("Bitiş portu: "))
    print(f"{site} üzerinde port taraması yapılıyor...")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((site, port))
        if result == 0:
            print(f"Port {port} açık")
        sock.close()

def dns_lookup():
    site = input("DNS sorgusu yapılacak domain: ")
    subprocess.call(['nslookup', site])

def traceroute():
    site = input("Traceroute yapılacak site/IP: ")
    cmd = 'traceroute' if os.name == 'posix' else 'tracert'
    subprocess.call([cmd, site])

def show_current_directory():
    print(f"Mevcut dizin: {os.getcwd()}")

def list_files():
    files = os.listdir('.')
    for f in files:
        print(f)

def system_info():
    print(f"Sistem: {platform.system()}")
    print(f"Sürüm: {platform.version()}")
    print(f"Mimari: {platform.machine()}")
    print(f"İşlemci: {platform.processor()}")

def whoami():
    print(f"Kullanıcı: {os.getlogin()}")

def uptime():
    if os.name == 'posix':
        subprocess.call(['uptime'])
    else:
        print("Bu komut Windows'ta desteklenmiyor.")

def netstat():
    if os.name == 'posix':
        subprocess.call(['netstat', '-tuln'])
    else:
        subprocess.call(['netstat', '-an'])

def show_env():
    for k, v in os.environ.items():
        print(f"{k}={v}")

def disk_usage():
    if os.name == 'posix':
        subprocess.call(['df', '-h'])
    else:
        subprocess.call(['wmic', 'logicaldisk', 'get', 'size,freespace,caption'])

def cpu_usage():
    if os.name == 'posix':
        subprocess.call(['top', '-b', '-n', '1'])
    else:
        subprocess.call(['wmic', 'cpu', 'get', 'loadpercentage'])

def memory_usage():
    if os.name == 'posix':
        subprocess.call(['free', '-h'])
    else:
        subprocess.call(['wmic', 'OS', 'get', 'FreePhysicalMemory,TotalVisibleMemorySize', '/Format:List'])

def calendar():
    if os.name == 'posix':
        subprocess.call(['cal'])
    else:
        print("Bu komut Windows'ta desteklenmiyor.")

def date_time():
    subprocess.call(['date'])

def who():
    if os.name == 'posix':
        subprocess.call(['who'])
    else:
        print("Bu komut Windows'ta desteklenmiyor.")

def last_logins():
    if os.name == 'posix':
        subprocess.call(['last', '-n', '5'])
    else:
        print("Bu komut Windows'ta desteklenmiyor.")

def check_open_ports():
    site = input("Port kontrolü yapılacak site/IP: ")
    ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]
    print(f"{site} üzerinde yaygın portlar kontrol ediliyor...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((site, port))
        if result == 0:
            print(f"Port {port} açık")
        sock.close()

def reverse_dns():
    ip = input("Ters DNS sorgusu yapılacak IP: ")
    try:
        host = socket.gethostbyaddr(ip)
        print(f"{ip} için ters DNS: {host[0]}")
    except Exception as e:
        print("Ters DNS bulunamadı:", e)

def whois_lookup():
    domain = input("Whois sorgusu yapılacak domain: ")
    if sys.platform.startswith('linux') or sys.platform == 'darwin':
        subprocess.call(['whois', domain])
    else:
        print("Whois komutu bu sistemde desteklenmiyor.")

def check_website_status():
    site = input("Kontrol edilecek site (http:// veya https:// ile): ")
    try:
        import requests
        r = requests.get(site)
        print(f"Site durumu: {r.status_code}")
    except Exception as e:
        print("Siteye erişilemedi:", e)

def download_file():
    url = input("İndirilecek dosyanın URL'si: ")
    filename = input("Kaydedilecek dosya adı: ")
    try:
        import requests
        r = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(r.content)
        print(f"{filename} indirildi.")
    except Exception as e:
        print("Dosya indirilemedi:", e)

def simple_http_server():
    port = input("HTTP sunucusu için port numarası (örnek: 8000): ")
    try:
        port = int(port)
        from http.server import HTTPServer, SimpleHTTPRequestHandler
        server = HTTPServer(('', port), SimpleHTTPRequestHandler)
        print(f"HTTP sunucusu başlatıldı, durdurmak için Ctrl+C")
        server.serve_forever()
    except Exception as e:
        print("Sunucu başlatılamadı:", e)

def main():
    while True:
        clear()
        banner()
        print("1. Site IP adresini öğren")
        print("2. Siteye ping at")
        print("3. Port taraması yap")
        print("4. DNS sorgusu yap")
        print("5. Traceroute yap")
        print("6. Mevcut dizini göster")
        print("7. Dosyaları listele")
        print("8. Sistem bilgisi göster")
        print("9. Kullanıcı adını göster")
        print("10. Sistem çalışma süresi")
        print("11. Ağ bağlantılarını göster (netstat)")
        print("12. Ortam değişkenlerini göster")
        print("13. Disk kullanımını göster")
        print("14. CPU kullanımını göster")
        print("15. Bellek kullanımını göster")
        print("16. Takvimi göster")
        print("17. Tarih ve saati göster")
        print("18. Sisteme giriş yapan kullanıcıları göster (who)")
        print("19. Son girişleri göster (last)")
        print("20. Yaygın portları kontrol et")
        print("21. Ters DNS sorgusu yap")
        print("22. Whois sorgusu yap")
        print("23. Web sitesi durumunu kontrol et")
        print("24. Dosya indir")
        print("25. Basit HTTP sunucusu başlat")
        print("26. Çıkış")

        choice = input("\n
