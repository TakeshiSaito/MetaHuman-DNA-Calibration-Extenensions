from MetaHumanFacialImporter import Presenter
from MetaHumanFacialImporter.Model import FacialRig, Animation, FacialFile
from MetaHumanFacialImporter.UseCase import ImportFacialAnimUseCase, ImportRigUseCase
from MetaHumanFacialImporter.View import MainWindow
import importlib


def run_main():
    importlib.reload(MainWindow)
    importlib.reload(Presenter)
    importlib.reload(ImportFacialAnimUseCase)
    importlib.reload(ImportRigUseCase)
    importlib.reload(FacialRig)
    importlib.reload(Animation)
    importlib.reload(FacialFile)

    main_window = MainWindow.MainWindow()
    presenter = Presenter.Presenter(main_window)
    presenter.show()


if __name__ == '__main__':
    run_main()
