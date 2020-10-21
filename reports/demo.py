from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver

class DriverInstance:

    __instance = None

    @classmethod
    def create_driver(cls) -> WebDriver:
        if not cls.__instance:
            cls.__instance = webdriver.Firefox()
        return cls.__instance
