from pages.base_page import BasePage
from helps import (
    sbis_dowload_selector,
    cont_selector,
    region_selector,
    tenzor_selector,
    contact_selector,
    windows_selector,
    download_selector,
    block_contacts_selector,
    sbis_plagin
)

from selenium.webdriver.common.by import By
import re


class SbisPage(BasePage):
    url = "https://sbis.ru/"

    def __init__(self, browser) -> None:
        super().__init__(browser)

    def contact_buttons(self):
        return self.find_element(contact_selector)

    def contact_is_selected(self):
        return self.find_element(cont_selector).is_displayed()

    def region_button(self):
        return self.find_element(region_selector)

    def tensor_button(self):
        return self.find_element(tenzor_selector)

    def check_region(self, region):
        region = self.browser.find_element(
            By.XPATH,
            f"//*[contains(text(), '{region}')]"
            )
        return region.is_displayed()

    def change_region(self, region):
        region = self.browser.find_element(
            By.XPATH,
            f"//*[contains(text(), '{region}')]"
            )
        return region.click()

    def check_block_contacts(self):
        return self.find_element(block_contacts_selector)

    def dowload_button(self):
        return self.find_element(download_selector)

    def windows_button(self):
        return self.find_element(windows_selector)

    def sbis_button(self):
        return self.find_element(sbis_plagin)

    def dowload_file(self):
        return self.find_elements(sbis_dowload_selector)[0]

    def check_size_file(self):
        string = self.find_element(sbis_dowload_selector).text
        mb = re.search(r"\d+.\d+", string)
        return (int(float(mb[0])))
