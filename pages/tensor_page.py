from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from helps import images_selector, block_selector


class TensorPage(BasePage):
    url = "https://tensor.ru/"

    def __init__(self, browser) -> None:
        super().__init__(browser)

    def check_block(self, block_name):
        block = self.browser.find_element(
            By.XPATH, f"//*[contains(text(), '{block_name}')]"
            )
        return block.is_displayed()

    def find_about_block(self):
        return self.find_elements(block_selector)[1]

    def check_images_size(self):
        images = self.find_elements(images_selector)
        first_img = images[0]
        for img in images[1:]:
            assert img.size["width"] == first_img.size["width"]
            assert img.size["height"] == first_img.size["height"]
