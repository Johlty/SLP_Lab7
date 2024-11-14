from Classes.unit_of_work import UnitOfWork
from Classes.api_repository import APIRepository
from Classes.post_saver import PostSaver
from Functions.utils import get_color_choice
from colorama import Fore, Style

def main_menu():
    repository = APIRepository()
    uow = UnitOfWork()
    saver = PostSaver()
    color_title = Fore.GREEN
    color_body = Fore.RESET

    while True:
        print("1. Get all posts\n2. Get post by ID\n3. View history\n4. Save history\n5. Save post\n6. Change color\n7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            posts = repository.get_all_posts()
            uow.record_query("Get all posts", posts)
            for post in posts:
                print(f"{color_title}ID: {post['id']}\nTitle: {post['title']}{Style.RESET_ALL}")
                print(f"{color_body}Body: {post['body']}{Style.RESET_ALL}")

        elif choice == "2":
            post_id = input("Enter post ID: ")
            post = repository.get_post_by_id(post_id)
            if post:
                uow.record_query(f"Get post by ID {post_id}", post)
                print(f"{color_title}ID: {post['id']}\nTitle: {post['title']}{Style.RESET_ALL}")
                print(f"{color_body}Body: {post['body']}{Style.RESET_ALL}")
            else:
                print("Post not found.")

        elif choice == "3":
            for entry in uow.get_history():
                print(f"{entry['timestamp']}: {entry['query']} -> {entry['result']}")

        elif choice == "4":
            saver.save_post(uow.get_history(), "json", "history.json")

        elif choice == "5":
            post_id = int(input("Enter saved post ID: "))
            post = repository.get_post_by_id(post_id)
            format_choice = input("Choose format (json/csv/txt): ").lower()
            saver.save_post(post, format_choice, f"post_{post_id}.{format_choice}")

        elif choice == "6":
            color_title = get_color_choice()
            color_body = get_color_choice()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print(Fore.RED + "Invalid choice. Try again." + Style.RESET_ALL)
