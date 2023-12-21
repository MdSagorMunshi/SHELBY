import random
import string
import http.client
import socket
import subprocess
import os
import psutil
from cryptography.fernet import Fernet
from github import Github
from colorama import init, Fore, Style
from datetime import datetime
import requests  # Added for URL shortening
from fake_useragent import UserAgent  # Added for User-Agents
from faker import Faker  # Added for IPs and proxies

init(autoreset=True)  # Initialize colorama

RESULTS_FOLDER = "results"

# Ensure the 'results' folder exists
if not os.path.exists(RESULTS_FOLDER):
    os.makedirs(RESULTS_FOLDER)

def check_http_status(url):
    try:
        conn = http.client.HTTPConnection(url)
        conn.request("HEAD", "/")
        response = conn.getresponse()
        return response.status
    except Exception as e:
        return f"Error: {e}"

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)

    with open(file_path + ".enc", 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()

    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)

    original_file_path = encrypted_file_path.rsplit('.', 1)[0]
    with open(original_file_path, 'wb') as file:
        file.write(decrypted_data)

def get_network_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    gateway = os.popen("ip route | grep default | awk '{print $3}'").read().strip()
    open_ports = os.popen("netstat -lntu | awk '{print $4}' | grep -E ':[0-9]+' | cut -d: -f2").read().splitlines()
    
    return {
        "Hostname": hostname,
        "IP Address": ip_address,
        "Gateway": gateway,
        "Open Ports": open_ports
    }

def analyze_github_repo(repo_url):
    g = Github()
    try:
        repo = g.get_repo(repo_url)
        return {
            "Repository Name": repo.name,
            "Description": repo.description,
            "Language": repo.language,
            "Stars": repo.stargazers_count,
            "Forks": repo.forks_count,
            "Last Updated": repo.updated_at
        }
    except Exception as e:
        return f"Error: {e}"

def monitor_system_resources():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')

    return {
        "CPU Usage (%)": cpu_percent,
        "Memory Usage": {
            "Total": memory_info.total,
            "Used": memory_info.used,
            "Free": memory_info.free
        },
        "Disk Usage": {
            "Total": disk_usage.total,
            "Used": disk_usage.used,
            "Free": disk_usage.free
        }
    }

def generate_random_ips(count=5):
    fake = Faker()
    ips = [fake.ipv4() for _ in range(count)]
    return ips

def generate_random_proxies(count=5):
    fake = Faker()
    proxies = [fake.ipv4_proxy() for _ in range(count)]
    return proxies

def generate_random_user_agents(count=5):
    ua = UserAgent()
    user_agents = [ua.random for _ in range(count)]
    return user_agents

def shorten_url(url):
    api_url = "https://api-ssl.bitly.com/v4/shorten"
    access_token = "7c46111065008633b71e42f1f9c6c4596a777bcc"  # Replace with your Bitly access token

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    payload = {
        "long_url": url,
    }

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json().get("id")
    else:
        return f"Error: {response.status_code}"

def rickroll():
    subprocess.run(["curl", "ascii.live/rick"])

def save_to_file_and_print(data, filename):
    with open(filename, 'w') as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")
            print(Fore.CYAN + f"{key}: {value}")

def get_next_filename():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    index = 1
    while True:
        filename = f"{RESULTS_FOLDER}/result{index}_{timestamp}.txt"
        if not os.path.exists(filename):
            return filename
        index += 1

def print_logo():
    logo = r"""    
   _____ _    _ ______ _      ______     __
  / ____| |  | |  ____| |    |  _ \ \   / /
 | (___ | |__| | |__  | |    | |_) \ \_/ / 
  \___ \|  __  |  __| | |    |  _ < \   /  
  ____) | |  | | |____| |____| |_) | | |   v1.0
 |_____/|_|  |_|______|______|____/  |_|   
                                           
                                              """
    print(Fore.BLUE + Style.BRIGHT + logo)

if __name__ == "__main__":
    try:
        print_logo()

        print(Fore.GREEN + Style.BRIGHT + "Options:")
        print("1. Check HTTP Status Code")
        print("2. Generate Password")
        print("3. Encrypt File")
        print("4. Decrypt File")
        print("5. Get Network Information")
        print("6. Analyze GitHub Repository")
        print("7. Monitor System Resources")
        print("8. Generate Random IPs")
        print("9. Generate Random Proxies")
        print("10. Generate Random User-Agents")
        print("11. Shorten URL")
        print("12. Rickroll ")

        option = int(input(Fore.YELLOW + "Enter your choice (1-12): "))

        if option == 1:
            url = input("Enter the URL to check status code: ")
            status_code = check_http_status(url)
            result = {"HTTP Status Code": status_code}
            filename = get_next_filename()
            save_to_file_and_print(result, filename)
        elif option == 2:
            password_length = int(input("Enter the password length: "))
            generated_password = generate_password(password_length)
            result = {"Generated Password": generated_password}
            filename = get_next_filename()
            save_to_file_and_print(result, filename)
        elif option == 3:
            file_path = input("Enter the path of the file to encrypt: ")
            key = Fernet.generate_key()
            encrypt_file(file_path, key)
            print(Fore.GREEN + f"File encrypted successfully. Key: {key}")
        elif option == 4:
            encrypted_file_path = input("Enter the path of the encrypted file: ")
            key = input("Enter the key for decryption: ")
            decrypt_file(encrypted_file_path, key)
            print(Fore.GREEN + "File decrypted successfully.")
        elif option == 5:
            network_info = get_network_info()
            filename = get_next_filename()
            save_to_file_and_print(network_info, filename)
        elif option == 6:
            repo_url = input("Enter the GitHub repository URL: ")
            repo_info = analyze_github_repo(repo_url)
            filename = get_next_filename()
            save_to_file_and_print(repo_info, filename)
        elif option == 7:
            system_resources = monitor_system_resources()
            filename = get_next_filename()
            save_to_file_and_print(system_resources, filename)
        elif option == 8:
            count = int(input("Enter the number of random IPs to generate: "))
            ips = generate_random_ips(count)
            result = {"Random IPs": ips}
            filename = get_next_filename()
            save_to_file_and_print(result, filename)
        elif option == 9:
            count = int(input("Enter the number of random proxies to generate: "))
            proxies = generate_random_proxies(count)
            result = {"Random Proxies": proxies}
            filename = get_next_filename()
            save_to_file_and_print(result, filename)
        elif option == 10:
            count = int(input("Enter the number of random User-Agents to generate: "))
            user_agents = generate_random_user_agents(count)
            result = {"Random User-Agents": user_agents}
            filename = get_next_filename()
            save_to_file_and_print(result, filename)
        elif option == 11:
            url_to_shorten = input("Enter the URL to shorten: ")
            shortened_url = shorten_url(url_to_shorten)
            result = {"Shortened URL": shortened_url}
            filename = get_next_filename()
            save_to_file_and_print(result, filename)
        elif option == 12:
            rickroll()
            print(Fore.GREEN + "Never gonna give you up!")
        else:
            print(Fore.RED + "Invalid option. Please choose a number between 1 and 12.")
    except KeyboardInterrupt:
        print(Fore.RED + Style.BRIGHT + "\nOperation aborted by the user.")
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f"An error occurred: {e}")
