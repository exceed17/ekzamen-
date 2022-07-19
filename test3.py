# задание1


def card(number):
    number = str(number)
    if len(number) == 16:
        print(('*' * 12) + number[-5:-1])
    else:
        print('Ошибка')


card(1234567898765432)

# задание2

def check(word):
    n = 0
    for i in word:
        n -= 1
        if i == word[n]:
            continue
        else:
            print('Данное слово не палиндром')
            break


check('течет')


# задание3

class Tomato:
    states = ['начало', 'середина', 'созрел', 'салат']

    def __init__(self, index):
        self._index = index
        self._state = Tomato.states[0]
        self.n = 1

    def grow(self):
        if len(Tomato.states) <= self.n:
            print(f'Стадия созревания {Tomato.states[-1]}')
        else:
            print(f'Стадия созревания {Tomato.states[self.n]}')
            self.n += 1

    def is_rise(self):
        if len(Tomato.states) <= self.n:
            print('Томат созрел')
            return 100
        else:
            print('Томат ещё не созрел')
            return 200


# задание 4

class TomatoBush():
    def __init__(self, number):
        self.tomatoes = [Tomato(f'list {number}') for i in range(number)]

    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):
        prov = []
        for i in self.tomatoes:
            prov.append(i.is_rise())
            if sum(prov) == 300:
                return True

    def give_away_all(self):
        self.tomatoes = []



# задание5

class Gardener():
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Садовник начинает работу')
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe() == True:
            print('Собираем урожай')
            TomatoBush.give_away_all(self)
            print('Урожай успешно собран')
        else:
            print('Урожай ещё не созрел')

    @staticmethod
    def knowledge_base():
        print('work - начало работы садовника, перед на новый уровень созревания. harvest - сбор урожая(только'
              'в том случае, если он созрел. ')

tomato = TomatoBush(3)
Gardener.knowledge_base()
garden = Gardener('Ivan', tomato)
garden.work()
garden.work()
garden.work()
garden.harvest()
garden.harvest()