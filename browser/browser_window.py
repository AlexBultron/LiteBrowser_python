# browser_window.py
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QToolBar, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView
from chatgpt_popup import open_chatgpt
from adblock import enable_adblock
from PyQt5.QtCore import QUrl, QDir
import os

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Fast Browser")
        self.setGeometry(100, 100, 1200, 800)

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tabs)

        self.create_toolbar()
        self.add_new_tab(QUrl("https://www.google.com"), "Home")

        enable_adblock()

    def create_toolbar(self):
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        new_tab_action = QAction("New Tab", self)
        new_tab_action.triggered.connect(lambda: self.add_new_tab(QUrl("https://www.google.com"), "New Tab"))
        toolbar.addAction(new_tab_action)

        chatgpt_action = QAction("ChatGPT", self)
        chatgpt_action.triggered.connect(open_chatgpt)
        toolbar.addAction(chatgpt_action)

    def add_new_tab(self, url, label):
        browser = QWebEngineView()
        browser.load(url)
        index = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(index)

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)
