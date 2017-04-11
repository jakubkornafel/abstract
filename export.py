# - AbstractExporter - klasa która mi składać się z następujących metod:
#     - __init__ - przyjmuje argument storage oraz data
#     - process - tutaj również chcemy podnieć wyjątek, który mówi że metoda nie została zaimplementowana
#     - jak wyżej wybierz właściwy wyjątek.


class AbstractExporter(object):
    def __init__(self, argument, data):
        self.argument = argument
        self.data = data

    def process(self):
        raise NotImplementedError
