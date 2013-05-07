#Embedded file name: /Users/versonator/Jenkins/live/Projects/AppLive/Resources/MIDI Remote Scripts/Push/Settings.py
from Setting import OnOffSetting, EnumerableSetting
from PadSensitivity import PadParameters
import consts
action_pad_sensitvity = PadParameters(off_threshold=200, on_threshold=270, gain=85000, curve1=120000, curve2=60000)

def _create_pad_settings():
    return [PadParameters(gain=100000, curve1=45000, curve2=0, name='Linear'),
     PadParameters(gain=85000, curve1=120000, curve2=60000, name='Log 1 (Default)'),
     PadParameters(gain=85000, curve1=120000, curve2=50000, name='Log 2'),
     PadParameters(gain=100000, curve1=120000, curve2=50000, name='Log 3'),
     PadParameters(gain=130000, curve1=120000, curve2=50000, name='Log 4'),
     PadParameters(gain=140000, curve1=120000, curve2=0, name='Log 5')]


def _threshold_formatter(value):
    return str(value) if value != 0 else '0 (Default)'


SETTING_THRESHOLD = 0
SETTING_CURVE = 1
SETTING_WORKFLOW = 2

def create_settings(preferences = None):
    preferences = preferences if preferences != None else {}
    pad_settings = _create_pad_settings()
    return {SETTING_WORKFLOW: OnOffSetting(name='Workflow', value_labels=['Scene', 'Clip'], default_value=True, preferences=preferences),
     SETTING_THRESHOLD: EnumerableSetting(name='Pad Threshold', values=range(consts.MIN_THRESHOLD_STEP, consts.MAX_THRESHOLD_STEP + 1), default_value=0, preferences=preferences, value_formatter=_threshold_formatter),
     SETTING_CURVE: EnumerableSetting(name='Velocity Curve', values=pad_settings, default_value=pad_settings[1], preferences=preferences)}