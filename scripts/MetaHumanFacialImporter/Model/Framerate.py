from maya import cmds


def get_fps() -> float:
    current_time_unit = cmds.currentUnit(q=True, time=True)
    if current_time_unit == 'ntsc':
        return 30
    elif current_time_unit == 'film':
        return 24
    elif current_time_unit == 'pal':
        return 25
    elif current_time_unit == 'show':
        return 48
    elif current_time_unit == 'palf':
        return 50
    elif current_time_unit == 'ntscf':
        return 60
    elif current_time_unit == 'game':
        return 15
    else:
        current_time_unit = current_time_unit.replace('fps', '')
        current_time_unit = float(current_time_unit)
        return current_time_unit
