# - чтение из файла, метод read возвращает строку с текущим содержанием файла

# - запись в файл, метод write принимает в качестве аргумента строку с новым содержанием файла

# - сложение объектов типа File, результатом сложения является объект класса File, при этом создается новый файл и файловый объект, в котором содержимое второго файла добавляется к содержимому первого файла. Новый файл должен создаваться в директории, полученной с помощью функции tempfile.gettempdir. Для получения нового пути можно использовать os.path.join.

# - возвращать в качестве строкового представления объекта класса File полный путь до файла

# - поддерживать протокол итерации, причем итерация проходит по строкам файла
import tempfile
import os


class File:
    def __init__(self, path):
        self.path = path
        self.file = self._open_file(self.path)
        self.file_list = self.prod_list()
        self.count = 0

    @staticmethod
    def _open_file(path):
        if os.path.exists(path):
            return open(path, 'r+')

        else:
            return open(path, 'w+')

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def write(self, some_string):
        with open(self.path, 'w') as f:
            print(some_string, file=f, end='')
            self.file = open(self.path)

    def prod_list(self):
        result = []
        for line in self.file:
            result.append(line.strip())
        return result

    def __str__(self):
        return self.path

    def __iter__(self):
        return self

    def __next__(self):

        if self.count > len(self.file_list) - 1:
            raise StopIteration
        line = self.file_list[self.count]
        self.count += 1
        return line

    def __add__(self, other):
        storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
        new_file = File(storage_path)
        new_file.write(self.read() + other.read())
        new_file.file_list = new_file.prod_list()
        return new_file
