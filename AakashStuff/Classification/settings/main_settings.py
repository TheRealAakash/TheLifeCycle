from . import TRASH
from types import SimpleNamespace


def get_settings():
    mainConfig = TRASH.config
    return SimpleNamespace(**mainConfig), mainConfig
