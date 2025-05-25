import os
import subprocess

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print("""
███████╗ ██████╗ ██████╗ ███████╗██╗      ██████╗ ██╗      ██████╗ ██╗     
██╔════╝██╔═══██╗██╔══██╗██╔════╝██║     ██╔═══██╗██║     ██╔═══██╗██║     
█████╗  ██║   ██║██████╔╝█████╗  ██║     ██║   ██║██║     ██║   ██║██║     
██╔══╝  ██║   ██║██╔══██╗██╔══╝  ██║     ██║   ██║██║     ██║   ██║██║     
██║     ╚██████╔╝██║  ██║███████╗███████╗╚██████╔╝███████╗╚██████╔╝███████╗
╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝
    """)

def show_menu():
    print("Welcome to Echelon Multi-Tool by YourName\n")
    print("Select an option:")
    print("1. Display your public IP")
    print("2. Show network interfaces")
    print("3. Ping a host")
    print("4. DNS lookup")
    print("5. Traceroute to a host")
    print("6. Show current directory")
    print("7. List files in current directory")
    print("8. Show system info")
    print("9. Exit")

def get_public_ip():
    try:
        import requests
        ip = requests.get('https://api.ipify.org').text
        print(f"Your public IP is: {ip}")
    except Exception as e:
        print("Could not retrieve public IP. Make sure you have internet connection and 'requests' module installed.")

def show_network_interfaces():
    if os.name == 'posix':
        subprocess.call(['ip', 'addr'])
    else:
        subprocess.call(['ipconfig'])

def ping_host():
    host = input("Enter host to ping: ")
    subprocess.call(['ping', '-c', '4', host])

def dns_lookup():
    host = input("Enter domain for DNS lookup: ")
    subprocess.call(['nslookup', host])

def traceroute_host():
    host = input("Enter host for traceroute: ")
    subprocess.call(['traceroute', host])

def show_current_directory():
    print(f"Current directory: {os.getcwd()}")

def list_files():
    files = os.listdir('.')
    for f in files:
        print(f)

def show_system_info():
    if os.name == 'posix':
        subprocess.call(['uname', '-a'])
    else:
        subprocess.call(['systeminfo'])

def main():
    while True:
        clear_screen()
        banner()
        show_menu()
        choice = input("\nEnter choice (1-9): ").strip()
        if choice == '1':
            get_public_ip()
        elif choice == '2':
            show_network_interfaces()
        elif choice == '3':
            ping_host()
        elif choice == '4':
            dns_lookup()
        elif choice == '5':
            traceroute_host()
        elif choice == '6':
            show_current_directory()
        elif choice == '7':
            list_files()
        elif choice == '8':
            show_system_info()
        elif choice == '9':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-9.")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
