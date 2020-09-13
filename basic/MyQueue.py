class nuri_queue(object):
    def __init__(self, arr) -> None:
        super().__init__()
        self.__list = arr

    def append(self, data):
        self.__list.append(data)

    def pop_left(self):
        data = self.__list[0]
        self.__list = self.__list[1:]
        return data

    def get_left(self):
        return self.__list[0]

