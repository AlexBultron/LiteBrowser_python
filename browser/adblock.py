# adblock.py
from PyQt5.QtWebEngineWidgets import QWebEngineProfile

def enable_adblock():
    profile = QWebEngineProfile.defaultProfile()
    profile.setHttpCacheType(QWebEngineProfile.MemoryHttpCache)
    profile.setPersistentCookiesPolicy(QWebEngineProfile.NoPersistentCookies)
    profile.setPersistentStoragePath("")  # avoid disk writes
