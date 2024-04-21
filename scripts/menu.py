from maya import cmds


def run_facial_importer(*args):
    import MetaHumanFacialImporter.main as facial_importer
    facial_importer.run_main()


def run_dna_viewer(*args):
    import dna_viewer
    dna_viewer.show()

def create_menu():
    cmds.menu(label='MetaHuman', tearOff=True, parent='MayaWindow')
    cmds.menuItem(label='Facial Importer', command=run_facial_importer)
    cmds.menuItem(label='DNA Viewer', command=run_dna_viewer)
