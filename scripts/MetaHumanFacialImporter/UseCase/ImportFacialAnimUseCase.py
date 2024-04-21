from MetaHumanFacialImporter.Exceptions import InValidFileTypeError
from MetaHumanFacialImporter.Model import Animation, FacialFile, FacialRig
from MetaHumanFacialImporter.Model import Framerate


def execute(path: str):
    if not FacialFile.check_exists(path):
        raise FileNotFoundError(f"No such file : {path}")

    if not FacialFile.check_exists(path):
        raise InValidFileTypeError(f"Invalid file extension : {path}. Please use .csv file")

    fps = Framerate.get_fps()
    ctrls = FacialRig.load_ctrls()

    frames, action_unit_values = FacialFile.load_facial_file(path, fps)
    Animation.set_keys(frames, action_unit_values,ctrls)
