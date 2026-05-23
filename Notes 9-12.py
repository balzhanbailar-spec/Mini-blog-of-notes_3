import pandas as pd
class Notes:
    def __init__(self):
        self.posts = []
    def add_post(self, title, text, author, tag):
        if len(title) < 3:
            print(f"Қате: '{title}' тақырыбы тым қысқа!")
            return
        if len(text) < 5:
            print(f"Қате: '{title}' постының мәтіні жеткіліксіз!")
            return
        post = {"title": title, "text": text, "author": author, "tag": tag}
        self.posts.append(post)
    def pandas_info(self):
        df = pd.DataFrame(self.posts)
        df["text_length"] = df["text"].str.len()
        print(df)
        print(df["tag"].value_counts())
        print(df.groupby("author").size().reset_index(name="posts_count"))
if __name__ == "__main__":
    blog = Notes()

    blog.add_post("Кино", "Томирис фильмі өте әсерлі болды!", "Ali", "movie")
    blog.add_post("Футбол", "Бүгін футбол ойнадым", "Ali", "sport")
    blog.add_post("Музыка", "Әлемнің жаңа әнін тыңдадым", "Aruzhan", "music")
    blog.pandas_info()