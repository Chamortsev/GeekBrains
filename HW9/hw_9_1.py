import time


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    @staticmethod
    def running(n):
        i = 0
        while i < n:
            print('\033[K%s\r' + TrafficLight.__color[0], end='')
            time.sleep(7)
            print('\033[K%s\r' + TrafficLight.__color[1], end='')
            time.sleep(2)
            print('\033[K%s\r' + TrafficLight.__color[2], end='')
            time.sleep(5)
            i = i + 1


a = TrafficLight
a.running(2)
