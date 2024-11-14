from File_Handler import json_handler, csv_handler, txt_handler

class PostSaver:
    def save_post(self, post, format, filename):
        if format == "json":
            json_handler.save_to_json(post, filename)
        elif format == "csv":
            csv_handler.save_to_csv(post, filename)
        elif format == "txt":
            txt_handler.save_to_txt(post, filename)
        else:
            print("Invalid format.")
