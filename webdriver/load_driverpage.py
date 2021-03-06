import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class EdgeOptions(object):
    pass

class LoadDriver(object):
    driver_folderpath = "null"

    def setupOptionBrowserMethod(self, argument, ini_location="\\drivers\\"):
        finalorg = argument.lower()
        self.driver_folderpath = ini_location
        file_directory = os.path.dirname(os.path.abspath(__file__))
        self.parent_directory = os.path.dirname(file_directory) + self.driver_folderpath
        print(self.parent_directory)
        driver = self.chrome()
        return driver

    def chrome(self):
        # driverobject = webdriver.Chrome(executable_path= self.parent_directory +"\\chromedriver.exe");
        driverobject = webdriver.Chrome(ChromeDriverManager().install())
        return driverobject

    def edge(self):
        # driverobject = webdriver.edge()
        driverobject = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
        return driverobject

    def firefox(self):
        # driverobject = webdriver.firefox()
        driverobject = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        return driverobject

    def edgechromium(self):
        options = EdgeOptions()
        options.use_chromium = True
        options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

        driverobject = webdriver.Edge(
            executable_path=self.parent_directory + "\\msedgedriver.exe")
        return driverobject
