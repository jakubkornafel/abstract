# - Data - klasa która ma się składać z następujących metod:
#     - __init__ - przyjmuje argumenty data_source, importer, exporter
#     - import - wywołuje self.importer.process() i rezultat zapisuje w self.dat
#     - export - wywołuje self.exporter.process()


class Data(object):
    def __init__(self, data_source, importer, exporter):
        self.data_source = data_source
        self.importer = importer
        self.exporter = exporter

    def import(self):
        self.data = self.importer.process()

    def export(self):
        self.exporter.process()