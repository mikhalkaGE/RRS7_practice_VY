

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, url):
        self.driver.get(url)
