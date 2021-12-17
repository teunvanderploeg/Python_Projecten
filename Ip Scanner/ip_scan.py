import socket
import threading
import concurrent.futures
import colorama
from colorama import Fore

colorama.init()

print_lock = threading.Lock()

ip = input("Enter the IP to scan: ")
ip_range = input("Enter the range of ports you want to scan: 1-")


def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close()
        print(Fore.WHITE + f"[{port}]" + Fore.GREEN + " Opened")
    except:
        pass


with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(int(ip_range)):
        executor.submit(scan, ip, port + 1)
