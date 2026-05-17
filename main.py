import json
import pandas as pd
import matplotlib.pyplot as plt
from fastapi import FastAPI
import uvicorn
app = FastAPI()
#1
class Blog:
    def __init__(self, title, text, date):
        if len(title) < 3:
            print("Title тым қысқа")
            return
        if len(text) < 5:
            print("Text жеткіліксіз")
            return
        self.title = title
        self.text = text
        self.date = date
    def show(self):
        print("Title:", self.title)
        print("Text:", self.text)
        print("Date:", self.date)
        print()
#2
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
#3
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
#4
class Notes:
    def __init__(self):
        self.posts = []
    def add_post(self, title, text, author, tag):
        post = {
            "title": title,
            "text": text,
            "author": author,
            "tag": tag
        }
        self.posts.append(post)
    def pandas_info(self):
        df = pd.DataFrame(self.posts)
        df["text_length"] = df["text"].str.len()
        print(df)
        print(df["tag"].value_counts())
        print(df.groupby("author").count())
#5
class ActivityBlog:
    def __init__(self):
        self.posts = [
            {
                "title": "Кино",
                "text": "Маған Гарри Поттер фильмі ұнады",
                "date": "2026-05-17",
                "author": "Gaukhar",
            },
            {
                "title": "Спорт",
                "text": "Бүгін тренировка жасадық",
                "date": "2026-05-17",
                "author": "Esengeldi",
            },
            {
                "title": "Сабақ",
                "text": "Математика сабағы өте қызық",
                "date": "2026-05-18",
                "author": "Nurai",
            },
            {
                "title": "Табиғат",
                "text": "Бүгін ауа-райы тамаша болып тұр",
                "date": "2026-05-19",
                "author": " Ernur",
            },
        ]
    def show_activity_chart_popup(self):
        df = pd.DataFrame(self.posts)
        date_counts = df["date"].value_counts().sort_index()
        plt.figure(figsize=(6, 4))
        date_counts.plot(kind="bar", color="green", edgecolor="black")
        plt.title("Блог белсенділігі (Күндер бойынша)")
        plt.xlabel("Күні")
        plt.ylabel("Пост саны")
        plt.tight_layout()
        print("Веб-сайтты қосу үшін графикті жабыңыз.")
        plt.show()
    def api_get_all_posts(self):
        return {
            "status": "success",
            "total_posts": len(self.posts),
            "data": self.posts,
        }
    def api_search_posts(self, query: str):
        search_results = []
        query_lower = query.lower()
        for post in self.posts:
            if (
                    query_lower in post["title"].lower()
                    or query_lower in post["text"].lower()
            ):
                search_results.append(post)
        return {
            "status": "success",
            "search_query": query,
            "found_count": len(search_results),
            "data": search_results,
        }

blog_service = ActivityBlog()

@app.get("/")
def get_all_posts_api():
    return blog_service.api_get_all_posts()
@app.get("/search")
def search_posts_api(query: str):
    return blog_service.api_search_posts(query)

if __name__ == "__main__":
    #1
    print("1-тапсырма: Blog класы")
    post1 = Blog("Кино", "Пейіш киносына 10/10 қойдым, маған қатты ұнады!", "17.05.2026")
    post2 = Blog("Спорт", "Бүгін воллейбол ойнадым", "18.05.2026")
    post1.show()
    post2.show()
    print("-" * 50)
    #2
    print("2-тапсырма:BlogService класы")
    blog = BlogService()
    blog.add_post("Кино", "Пейіш киносына 10/10 қойдым", "17.05.2026")
    blog.add_post("Спорт", "Бүгін воллейбол ойнадым", "18.05.2026")
    blog.find_by_title("Кино")
    blog.find_by_date("18.05.2026")
    print("-" * 50)
    #3
    print("3-тапсырма:MiniBlog класы")
    mini_blog = MiniBlog()
    mini_blog.add_post("Кино", "Пейіш киносы маған қатты ұнады!", "17.05.2026", "Nurzhan")
    mini_blog.add_post("Спорт", "Бүгін достарыммен бірге жүгірдім", "18.05.2026", "Gaukhar")
    mini_blog.find_by_author("Nurzhan")
    mini_blog.export_json()
    print("-" * 50)
    #4
    print("4-тапсырма: Notes класы / Pandas")
    pandas_blog = Notes()
    pandas_blog.add_post("Кино", "Томирис фильмі өте әсерлі болды!", "Ali", "movie")
    pandas_blog.add_post("Футбол", "Бүгін футбол ойнадым", "Ali", "sport")
    pandas_blog.add_post("Музыка", "Әлемнің жаңа әнін тыңдадым", "Aruzhan", "music")
    pandas_blog.pandas_info()
    print("-" * 50)

    #5
    print("5-тапсырма: ActivityBlog / FastAPI / Matplotlib")
    blog_service.show_activity_chart_popup()
    uvicorn.run(app, host="127.0.0.1", port=8000)