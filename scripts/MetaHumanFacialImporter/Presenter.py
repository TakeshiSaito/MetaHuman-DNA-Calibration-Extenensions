from functools import partial

from MetaHumanFacialImporter.UseCase import ImportFacialAnimUseCase, ImportRigUseCase
from MetaHumanFacialImporter.Exceptions import InValidFileTypeError
from MetaHumanFacialImporter.View.MainWindow import MainWindow


class Presenter:
    def __init__(self, view: MainWindow):
        self.__view = view
        self.__view.import_dna_signal.connect(partial(self.on_import_rig))
        self.__view.import_csv_signal.connect(partial(self.on_import_csv))

    def show(self):
        self.__view.show()

    def on_import_csv(self, path):
        try:
            ImportFacialAnimUseCase.execute(path)
        except FileNotFoundError as e:
            self.__view.show_error(str(e))
        except InValidFileTypeError as e:
            self.__view.show_error(str(e))

    def on_import_rig(self, path):
        try:
            ImportRigUseCase.execute(path)
        except FileNotFoundError as e:
            self.__view.show_error(str(e))
        except InValidFileTypeError as e:
            self.__view.show_error(str(e))
