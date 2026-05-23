import json
class MiniBlog:
    def __init__(self):
        self.posts = []
    def add_post(self, title, text, date, author):
        if len(title) < 3:
            print("Title тым қысқа")
            return
        if len(text) < 5:
            print("Text жеткіліксіз")
            return
        post = {
            "title": title,
            "text": text,
            "date": date,
            "author": author
        }
        self.posts.append(post)
    def find_by_author(self, author):
        for post in self.posts:
            if post["author"] == author:
                print(post)
    def export_json(self):
        with open("posts.json", "w", encoding="utf-8") as file:
            json.dump(self.posts, file, ensure_ascii=False, indent=4)
        print("JSON файл сақталды")

if __name__ == "__main__":
    blog = MiniBlog()

    blog.add_post("Кино", "Пейіш киносы маған қатты ұнады!", "17.05.2026", "Nurzhan")
    blog.add_post("Спорт", "Бүгін достарыммен бірге жүгірдім", "18.05.2026", "Gaukhar")
    blog.find_by_author("Nurzhan")
    blog.export_json()