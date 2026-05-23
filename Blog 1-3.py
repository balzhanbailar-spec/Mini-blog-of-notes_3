class Blog:
    def __init__(self, title, text, date):
        if len(title) < 3:
            print(f"Қате: '{title}' тақырыбы тым қысқа! (3 таңбадан көп керек)")
            self.is_valid = False
            return
        if len(text) < 5:
            print(f"Қате: '{title}' постының мәтіні жеткіліксіз! (5 таңбадан көп болуы керек)")
            self.is_valid = False
            return
        self.title = title
        self.text = text
        self.date = date
        self.is_valid = True
    def show(self):
        if not self.is_valid:
            print("Бұл постты шығару мүмкін емес, себебі валидациядан өтпеді.")
            print("-" * 20)
            return
        print("Title:", self.title)
        print("Text:", self.text)
        print("Date:", self.date)
        print("-" * 20)
print("Посттарды жасау кезеңі")
post1 = Blog("Кино", "Пейіш киносына 10/10 қойдым, маған қатты ұнады!", "17.05.2026")
post2 = Blog("IT", "Бүгін Python тілінде жаңа класс жазуды үйрендім.", "18.05.2026")
post3 = Blog("Спорт", "Ойын", "19.05.2026")
post4 = Blog("Саяхат", "Алматы тауларына серуендеп қайттық, ауа райы тамаша болды.", "20.05.2026")
print("Посттарды экранға шығару")
post1.show()
post2.show()
post3.show()
post4.show()