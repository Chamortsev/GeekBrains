class Clothes:
    def __init__(self, param1=None, param2=None):
        self.param1 = param1
        self.param2 = param2

    @property
    def coast(self):
        return f'Расход всего {(self.param1 / 6.5 + 0.5) + (2 * self.param2 + 0.3) :.2f}'


class Coat(Clothes):
    def coast(self):
        coat_coast = self.param1 / 6.5 + 0.5
        return f'Расход ткани на пальто {coat_coast}'


class Suit(Clothes):
    def coast(self):
        suit_coast = 2 * self.param2 + 0.3
        return f'Расход ткани на костюм {suit_coast}'


v = 400
h = 55
c = Clothes(v, h)
coat = Coat(param1=v)
suit = Suit(param2=h)
print(c.coast)
print(coat.coast())
print(suit.coast())
