class User_info:
    def __init__(self, date_book, name, count, date_ar, count_day, max_price):
        self.date_book = date_book
        self.name = name
        self.count = count
        self.date_ar = date_ar
        self.count_day = count_day
        self.max_price = max_price

    def __str__(self):
        return f'{self.date_book} {self.name} {self.count} {self.date_ar} {self.count_day} {self.max_price}'

    def rooms(self):
        with open('fund.txt') as f1:
            z = f1.readlines()
        q = []
        for i in z:
            spl = i.split(' ')
            q.append(spl)
        if int(self.max_price) < 2300 or int(self.count) > 6:
            return 0
        if 2300  <= int(self.max_price) < 2900 and int(self.count) <= 2:
            total = []
            for b in q:
                if b[1] == 'двухместный':
                    total.append(b)
            if int(self.max_price)  >= 2760:
                pass










        price_room = {}
        """standart = []
        stand_up = []
        apartmnets = []
        for i in z:
            if i.find('стандарт'):
                standart.append(i)
            elif i.find('стандарт_улучшенный'):
                stand_up.append(i)
            elif i.find('апартамент')"""

    def __repr__(self):
        return self.__str__()


a = User_info('01.03.2020', 'Жиренкова Надежда Евдокимовна', '1', '01.03.2020', '3', '4400')
print(a.rooms())
