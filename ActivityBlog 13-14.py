import json
from fastapi import FastAPI
import matplotlib.pyplot as plt
import pandas as pd
import uvicorn
app = FastAPI()
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
    blog_service.show_activity_chart_popup()
    uvicorn.run(app, host="127.0.0.1", port=8000)