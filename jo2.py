class Animal:

    name = ''
    weight = 0
    speaks = ''

    def feed(self, food):
        self.weight += food

    def says(self):
        print(f'{self.name} goes "{self.speaks}"')


class Cow(Animal):

    def __init__(self, name, weight=0.0, speaks='Mo-o-o'):
        self.name = name
        self.weight = weight
        self.speaks = speaks

    def milk(self):
        print(f'{self.name} was milked')

class Duck(Animal):

    def __init__(self, name, weight=0.0, speaks='Quack-quack'):
        self.name = name
        self.weight = weight
        self.speaks = speaks

    def eggs(self):
        print(f'Eggs were collected from the {self.name}')


class Goose(Animal):

    def __init__(self, name, weight=0.0, speaks='Ga-ga-ga'):
        self.name = name
        self.weight = weight
        self.speaks = speaks

    def eggs(self):
        print(f'Eggs were collected from the {self.name}')

class Sheep(Animal):

    def __init__(self, name, weight=0.0, speaks='Ba-a-a'):
        self.name = name
        self.weight = weight
        self.speaks = speaks

    def shear(self):
        print(f'{self.name} was sheared')

class Goat(Animal):

    def __init__(self, name, weight=0.0, speaks='Ma-a-a'):
        self.name = name
        self.weight = weight
        self.speaks = speaks

    def milk(self):
        print(f'{self.name} was milked')

class Chicken(Animal):

    def __init__(self, name, weight=0.0, speaks='Co-co-co'):
        self.name = name
        self.weight = weight
        self.speaks = speaks

    def eggs(self):
        print(f'Eggs were collected from the {self.name}')

animals = []


def init_animals():

    goose_seryj = Goose('Seryj', 2.3)
    goose_belyj = Goose('Belyj', 1.5)

    animals.append(goose_seryj)
    animals.append(goose_belyj)

    cow_manka = Cow('Manka', 200)

    animals.append(cow_manka)

    sheep_barashek = Sheep('Barashek', 20)
    sheep_kudrjavyj = Sheep('Kudrjavyj', 25)

    animals.append(sheep_barashek)
    animals.append(sheep_kudrjavyj)

    chicken_koko = Chicken('Ko-Ko', 0.52)
    chicken_kukareku = Chicken('Kukareku', 0.63)

    animals.append(chicken_koko)
    animals.append(chicken_kukareku)

    goat_roga = Goat('Roga', 65)
    goat_kopyta = Goat('Kopyta', 64)

    animals.append(goat_roga)
    animals.append(goat_kopyta)

    duck_krjakva = Duck('Krjakva', 1.2)

    animals.append(duck_krjakva)


def animal_care():

    for animal in animals:

        print()

        animal.says()
        animal.feed(1.3)

        if isinstance(animal, Cow) or isinstance(animal, Goat):
            animal.milk()

        if isinstance(animal, Sheep):
            animal.shear()

        if isinstance(animal, Chicken) or isinstance(animal, Duck) or isinstance(animal, Goose):
            animal.eggs()

def main():

    init_animals()
    animal_care()

if __name__ == '__main__':
    main()
