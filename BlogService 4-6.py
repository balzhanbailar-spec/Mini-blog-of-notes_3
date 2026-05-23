class BlogService:
    def __init__(self):
        self.posts = []
    def add_post(self, title, text, date):
        if len(title) < 3:
            print(
                f"Қате: '{title}' тақырыбы тым қысқа! (3 таңбадан көп болуы керек)"
            )
            return
        if len(text) < 5:
            print(
                f"Қате: '{title}' постының мәтіні жеткіліксіз! (5 таңбадан көп болуы керек)"
            )
            return
        post = {"title": title, "text": text, "date": date}
        self.posts.append(post)
    def find_by_title(self, title):
        found = False
        for post in self.posts:
            if post["title"] == title:
                print(f"Title: {post['title']}")
                print(f"Text: {post['text']}")
                print(f"Date: {post['date']}")
                print("-" * 20)
                found = True
        if not found:
            print("Кешіріңіз, мұндай тақырыппен пост табылмады.")
    def find_by_date(self, date):
        found = False
        for post in self.posts:
            if post["date"] == date:
                print(f"Title: {post['title']}")
                print(f"Text: {post['text']}")
                print(f"Date: {post['date']}")
                print("-" * 20)
                found = True
        if not found:
            print("Кешіріңіз, бұл күнге ешқандай пост табылмады.")
if __name__ == "__main__":
    blog = BlogService()

    blog.add_post("Кино", "Пейіш киносына 10/10 қойдым, тамаша!", "17.05.2026")
    blog.add_post("Спорт", "Бүгін волейбол ойнадық", "18.05.2026")
    blog.add_post("IT", "Код", "18.05.2026")

    blog.find_by_title("Кино")
    blog.find_by_date("18.05.2026")