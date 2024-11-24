import time
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

def set_volume_by_name(app_name, volume):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name() == app_name:
            volume_control = session._ctl.QueryInterface(ISimpleAudioVolume)
            volume_control.SetMasterVolume(volume, None)
            return

set_volume_by_name("chrome.exe",1)
