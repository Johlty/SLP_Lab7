from colorama import Fore, Style

def get_color_choice():
    colors = {
        "1": Fore.RED,
        "2": Fore.GREEN,
        "3": Fore.BLUE,
        "4": Fore.YELLOW,
        "5": Fore.CYAN
    }
    print("Choose color:\n1. Red\n2. Green\n3. Blue\n4. Yellow\n5. Cyan")
    choice = input("Enter your choice: ")
    return colors.get(choice, Fore.RESET)
