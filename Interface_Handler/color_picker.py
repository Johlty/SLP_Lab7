from colorama import Fore, Style 

def display_color_options():
    """
    Виводить доступні кольори на екран.
    """
    print("Виберіть колір для заголовка або тексту:")
    print("1. Червоний")
    print("2. Зелений")
    print("3. Синій")
    print("4. Жовтий")
    print("5. Блакитний")

def get_color_choice():
    """
    Отримує вибір кольору від користувача.
    
    Повертає:
        str: Обраний колір із бібліотеки colorama.
    """
    colors = {
        "1": Fore.RED,
        "2": Fore.GREEN,
        "3": Fore.BLUE,
        "4": Fore.YELLOW,
        "5": Fore.CYAN
    }
    
    while True:
        display_color_options()
        choice = input("Введіть номер вибору кольору: ")
        
        color = colors.get(choice)
        if color:
            return color
        else:
            print(Fore.RED + "Невірний вибір, спробуйте ще раз." + Style.RESET_ALL)
