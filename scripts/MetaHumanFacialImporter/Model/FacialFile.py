import csv
import datetime
from pathlib import Path
from typing import Dict, List

IGNORE_LIST = ['Timecode', 'BlendShapeCount', 'HeadYaw', 'HeadPitch', 'HeadRoll', 'LeftEyeYaw', 'LeftEyePitch',
               'LeftEyeRoll', 'RightEyeYaw', 'RightEyePitch', 'RightEyeRoll', 'BlendshapeCount']


def load_facial_file(path: str, frame_rate: float) -> (List[float], Dict[str, List[float]]):
    with open(path, 'r') as file:
        csv_reader = csv.DictReader(file)
        frames = []
        action_unit_values: Dict[str:List[float]] = {}
        for row in csv_reader:
            frame = timecode_to_fps(row["Timecode"], frame_rate)
            frames.append(frame)

            for key in row:
                if key in IGNORE_LIST:
                    continue

                try:
                    action_unit_value = float(row[key])
                except ValueError:
                    action_unit_value = 0.0
                except TypeError:
                    action_unit_value = 0.0

                try:
                    action_unit_values[key].append(action_unit_value)
                except KeyError:
                    action_unit_values[key] = [action_unit_value]

    return frames, action_unit_values


def in_import_range(frame: float, start_frame: int, end_frame: int) -> bool:
    return start_frame <= frame <= end_frame


def timecode_to_fps(time_code: str, frame_rate: float) -> float:
    time_code_components = time_code.split(':')
    time_delta = datetime.timedelta(hours=int(time_code_components[0]),
                                    minutes=int(time_code_components[1]),
                                    seconds=int(time_code_components[2]) + float(time_code_components[3]) / 60.0)
    fps = time_delta.total_seconds() * frame_rate
    return fps


def check_exists(path: str) -> bool:
    file = Path(path)
    return file.exists()


def check_extension(path: str) -> bool:
    file = Path(path)
    return file.suffix == '.csv'
