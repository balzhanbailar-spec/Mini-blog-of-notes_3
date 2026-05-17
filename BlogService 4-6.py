class BlogService:
    def __init__(self):
        self.posts = []
    def add_post(self, title, text, date):
        if len(title) < 3:
            print("Title тым қысқа")
            return
        if len(text) < 5:
            print("Text жеткіліксіз")
            return
        post = {
            "title": title,
            "text": text,
            "date": date
        }
        self.posts.append(post)
    def find_by_title(self, title):
        for post in self.posts:
            if post["title"] == title:
                print(post)
    def find_by_date(self, date):
        for post in self.posts:
            if post["date"] == date:
                print(post)
blog = BlogService()
blog.add_post("Кино", "Пейіш киносына 10/10 қойдым", "17.05.2026")
blog.add_post("Спорт", "Бүгін воллейбол ойнадым", "18.05.2026")
blog.find_by_title("Кино")
blog.find_by_date("18.05.2026")