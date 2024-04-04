from termcolor import colored
import os
import datetime
import random
import requests
from urllib.parse import urlparse
import platform

# Global variables
current_user = "rex"  # Initial user
prompt_symbol = "➤"  # Prompt symbol

# Flag to check if ASCII art has been displayed
ascii_art_displayed = False
# Function to print ASCII art for ExeGod
def print_exe_god_ascii():
    # Clear the screen
    clear_screen()

    ascii_art = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⣄⠀⣀⣀⡤⣴⠶⠾⠿⢿⣿⡛⠛⠛⢻⠷⠶⠤⢤⣾⣀⠀⠀⠀⢀⠄⠀⠀⠀⠀⠀⢀⡾⠀⠀⠀⠀⠀
⢀⠀⠀⠀⠀⠀⠀⠀⢀⡤⢿⣿⡉⡀⠀⣈⣶⣄⣀⣸⣿⣄⣀⠀⡸⠀⠀⢀⣼⠀⠉⠛⠳⢶⣬⣄⡀⠀⠀⣠⣾⡟⠀⠀⠀⠀⠀⠀
⠀⠻⢦⣀⠀⠀⣠⡾⣻⣾⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣷⣶⣤⣖⣤⣏⣻⣿⣿⣿⣿⣿⣉⠀⠀⠀⠀⠀⢀⡄
⠀⠀⠀⢙⣿⣿⣿⣿⣿⣿⣿⠿⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣻⣿⣷⣦⣤⠶⠋⠀
⠀⠀⣠⣿⣿⣿⠿⠛⠉⠁⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣷⣿⡿⢟⢛⡻⠀⠀⠀
⠀⠈⢀⣞⡛⠁⠀⠀⠀⠀⢴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⢸⣿⣿⣿⣇⠘⢀⠛⢟⡻⢿⣿⣿⣿⣿⣿⣶⣦⣤⣤⠤
⠀⠴⠋⠀⠀⠀⠀⠀⠀⢀⣾⣟⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣀⣠⣴⣿⣿⣿⣿⡎⠁⠈⠀⠑⠋⠛⢿⣿⣿⡿⠉⠉⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡯⣾⣟⢿⣿⣿⣿⣿⣿⣿⠛⢏⠀⣿⣿⣿⡟⡿⡿⡿⣿⣿⡇⠀⠛⠳⣥⠀⠀⠙⣿⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀⠈⠙⠛⠄⠘⣩⣍⣃⣿⣿⣿⣧⣝⡛⠃⠁⠀⠀⢝⢻⣿⠀⠀⠀⠀⠀⢤⢠⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠐⠈⣦⢹⣿⣿⣿⣿⡍⢴⣿⠇⠀⠀⠁⠀⣹⡏⠀⠀⠀⠀⠀⠀⠸⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠁⢾⠿⣛⣛⣛⡻⢷⠈⠀⠀⠀⠀⠀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢳⡀⠀⠀⠀⠀⠀⠀⠉⠛⠟⠛⠋⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣬⣿⣶⣤⣈⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠁⠀⢀⣀⣤⣴⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⠟⠉⠀⠀⢈⠟⠻⠿⣶⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣲⣿⣵⠶⠿⢏⠉⠁⠈⠙⠷⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⣴⣟⡉⠙⡿⠛⠻⠿⣿⠿⠿⢿⠛⠋⠉⠻⣆⠀⠀⠀⠑⠄⠀⠀⠀⠘⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠈⢹⠋⠒⠲⠴⣷⠤⠀⠈⣇⠀⠀⠀⠈⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀
          𝙿𝚕𝚎𝚊𝚜𝚎 𝚝𝚢𝚙𝚎 "𝙷𝚎𝚕𝚙" 𝚝𝚘 𝚜𝚝𝚊𝚛𝚝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    colored_ascii = colored(ascii_art, 'yellow')
    print(colored_ascii)

# Function to execute commands based on user input
def execute_command(command):
    global current_user

    if command == "exit":
        print("Exiting...")
        exit()
    elif command == "clear":
        clear_screen()
    elif command == "methods":
        print_methods()
    else:
        run_command(command)

# Function to display prompt with round white background and black text
def display_prompt():
    global current_user, ascii_art_displayed

    if not ascii_art_displayed:
        print_exe_god_ascii()
        ascii_art_displayed = True

    prompt_text = f"{current_user} • ExeGod {prompt_symbol} "
    styled_prompt = colored(prompt_text, 'black', 'on_white', attrs=['bold'])
    user_input = input(styled_prompt)
    execute_command(user_input)

# Function to display methods information
def print_methods():
    methods_info = """
                ╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
                ║║║║╣  ║ ╠═╣║ ║ ║║╚═╗
                ╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝╚═╝
        NAME         DESCRIPTION      DURATION
    ╔═══════════╬═══════════════════╬═══════════╗
    ║  BROWSER          LAYER7           300    ║
    ║  TLS              LAYER7           300    ║
    ║  BYPASS           LAYER7           300    ║
    ║  MIX              LAYER7           300    ║
    ║  TCP              LAYER4           300    ║
    ║  UAM              LAYER7           300    ║
    ║  GHOST            LAYER7           300    ║
    ║  HTTPS            LAYER7           300    ║
    ║  CFBYPASS         LAYER7           300    ║
    ║  BOMB             LAYER7           300    ║
    ╚═══════════════════════════════════════════╝
    """
    print(colored(methods_info, 'cyan'))

# Function to run the mix.js or tls.js command
def run_command(command):
    if command.startswith("mix "):
        script_name = "mix"
        run_mix(command, script_name)
    elif command.startswith("tls "):
        script_name = "tls"
        run_mix(command, script_name)
    elif command == "help":
        # Clear the screen
        clear_screen()
        print("Available commands:")
        print("- mix <url> <time> <thread> <rate>")
        print("- tls <url> <time> <thread> <rate>")
        print("- clear (clear the screen)")
        print("- help (display this help)")
        print("- exit (exit the program)")
    else:
        print(f"Command not recognized: {command}")

# Function to run the mix.js or tls.js command
def run_mix(command, script_name):
    script_command = command[len(script_name) + 1:]
    script_arguments = script_command.split()
    if len(script_arguments) == 4:
        url, time, thread, rate = script_arguments
        print(f"Running '{script_name}.js' with parameters - URL: {url}, Time: {time}, Thread: {thread}, Rate: {rate}")

        # Simulating an attack with details in ASCII art
        print_attack_details(url, time, script_name)

        # Add your mix.js or tls.js execution logic here
    else:
        print(f"Invalid '{script_name}' command. Please provide URL, Time, Thread, and Rate.")

# Function to generate a random ASN
def generate_random_asn():
    return f"AS{random.randint(1000, 9999)}"

# Function to get organization and country details from the URL
def get_url_details(url):
    # Fetch organization details (disesuaikan menjadi Cloudflare Inc.)
    org = "Cloudflare Inc."

    # Fetch country details secara acak (misalnya, menggunakan beberapa negara contoh)
    countries = ["United States", "United Kingdom", "Germany", "France", "Canada", "Australia", "Japan", "Brazil", "India", "China"]
    country = random.choice(countries)

    return org, country

def print_attack_details(url, time, method):
    # Clear the screen
    clear_screen()

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    asn = generate_random_asn()
    org, country = get_url_details(url)
    
    attack_ascii = f"""
      {colored("╔═════════════════════════════════", 'cyan')}
        {colored("Attack Registered Successfully", 'red')}
{colored("╔═════╩═════════════════════════════════╩═════╗", 'cyan')}
     {colored("Status: Requests sent to ExeGod Api.", 'white')}
     Target: {url}
     Duration: {time} seconds
     Method: {method}  # Perubahan di sini
     Requests completed on: {current_time}

{colored("     Target Details:", 'red')}
     ASN: {asn}
     ORG: {org}
     COUNTRY: {country}
{colored("╚═════════════════════════════════════════════╝", 'cyan')}
    """
    
    print(attack_ascii)

# Function to clear the screen based on the operating system
def clear_screen():
    system_platform = platform.system()
    if system_platform == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Main loop for the terminal interface
while True:
    display_prompt()
