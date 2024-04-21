from pathlib import Path
from dna_viewer import DNA, RigConfig, build_rig

CURRENT_FILE = Path(__file__)
CONTENT_ROOT = CURRENT_FILE.parent.parent.parent.parent
DNA_CALIB_ROOT = f'{CONTENT_ROOT}/epic/MetaHuman-DNA-Calibration'
DNA_CALIB_DATA_PATH = f'{DNA_CALIB_ROOT}/data'
GUI_PATH = f'{DNA_CALIB_DATA_PATH}/gui.ma'
ANALOG_GUI_PATH = f'{DNA_CALIB_DATA_PATH}/analog_gui.ma'
ADDITIONAL_ASSEMBLE_SCRIPT = f'{DNA_CALIB_DATA_PATH}/additional_assemble_script.py'


def execute(dna_path: str, *args, **kwargs):
    dna = DNA(dna_path)
    print('---' * 100)
    print(GUI_PATH)
    print(ANALOG_GUI_PATH)
    print(ADDITIONAL_ASSEMBLE_SCRIPT)
    print('---' * 100)
    config = RigConfig(
        gui_path=GUI_PATH,
        analog_gui_path=ANALOG_GUI_PATH,
        aas_path=ADDITIONAL_ASSEMBLE_SCRIPT,
    )
    build_rig(dna=dna, config=config)
