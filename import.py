# - AbstractImporter - klasa która ma składać się z następujących metod:
#     - __init__ - przyjmuje argument source
#     - process - tutaj akurat podnosi wyjątek, który mówi że metoda nie została zaimplementowana - wybierz właściwy wyjątek ze strony https://docs.python.org/3/library/exceptions.html


class AbstractImporter(object):
    def __init__(self, source):
        self.source = source

    def process(self):
        raise NotImplementedError
