from pathlib import Path

from PySide2.QtCore import Signal
from PySide2.QtGui import QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMainWindow, QFileDialog
from maya import cmds
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

UI_FILE = Path(__file__).parent / 'UI.ui'


class MainWindow(MayaQWidgetBaseMixin, QMainWindow):
    import_csv_signal = Signal(str)
    import_dna_signal = Signal(str)

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.__widget = QUiLoader().load(UI_FILE.as_posix())
        self.setCentralWidget(self.__widget)
        self.setWindowTitle('MetaHuman Facial Importer')
        self.resize(400, 100)

        self.__widget.btn_csv_dialog.setIcon(QIcon(':/folder-open.png'))
        self.__widget.btn_csv_dialog.clicked.connect(lambda: self.open_csv_dialog())
        self.__widget.btn_import_csv.clicked.connect(lambda: self.import_csv_signal.emit(self.csv_path))

        self.__widget.btn_dna_dialog.setIcon(QIcon(':/folder-open.png'))
        self.__widget.btn_dna_dialog.clicked.connect(lambda: self.open_dna_dialog())
        self.__widget.btn_import_dna.clicked.connect(lambda: self.import_dna_signal.emit(self.dna_path))

    @property
    def csv_path(self) -> str:
        return self.__widget.lineEdit_csv_dialog.text()

    @property
    def dna_path(self) -> str:
        return self.__widget.lineEdit_dna_dialog.text()

    def open_dna_dialog(self):
        project_dir = cmds.workspace(q=True, rd=True)
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open DNA File', project_dir, 'DNA Files (*.dna)')
        self.__widget.lineEdit_dna_dialog.setText(file_path)

    def open_csv_dialog(self):
        project_dir = cmds.workspace(q=True, rd=True)
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open CSV File', project_dir, 'CSV Files (*.csv)')
        self.__widget.lineEdit_csv_dialog.setText(file_path)

    def show_error(self, message: str):
        self.show_error(message)
