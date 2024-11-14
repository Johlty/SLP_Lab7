def save_to_txt(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"ID: {data['id']}\nTitle: {data['title']}\nBody: {data['body']}\n")
