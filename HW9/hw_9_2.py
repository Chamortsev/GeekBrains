class Road:

    def __init__(self, lenght, width):
        self.__lenght = lenght
        self.__width = width

        print('Масса асфальта, необходимого для покрытия всей дороги: ', lenght * width * 25 * 5 / 1000)


Road(20, 5000)
