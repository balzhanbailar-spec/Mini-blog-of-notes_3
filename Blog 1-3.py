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
post1 = Blog("Кино", "Пейіш киносына 10/10 қойдым, маған қатты ұнады!", "17.05.2026")
post2 = Blog("Спорт", "Бүгін воллейбол ойнадым", "18.05.2026")
post1.show()
post2.show()