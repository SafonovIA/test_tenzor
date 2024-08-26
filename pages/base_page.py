class BasePage:
    url = None

    def __init__(self, browser) -> None:
        self.browser = browser

    def open(self):
        if self.url:
            self.browser.get(self.url)

    def find_element(self, args):
        return self.browser.find_element(*args)

    def find_elements(self, args):
        return self.browser.find_elements(*args)
