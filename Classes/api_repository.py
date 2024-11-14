import requests

class APIRepository:
    BASE_URL = "https://jsonplaceholder.typicode.com/posts"

    def get_all_posts(self):
        try:
            response = requests.get(self.BASE_URL)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching posts: {e}")
            return []

    def get_post_by_id(self, post_id):
        try:
            response = requests.get(f"{self.BASE_URL}/{post_id}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching post with ID {post_id}: {e}")
            return None
