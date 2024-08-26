from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure


@allure.feature("scene_1")
def test_scene_1(browser):
    sbis_page = SbisPage(browser)
    tensor_page = TensorPage(browser)

    with allure.step("Open page"):
        sbis_page.open()

    with allure.step("Click on contacts"):
        sbis_page.contact_buttons().click()
        assert sbis_page.contact_is_selected

    with allure.step("Click on Tensor"):
        sbis_page.tensor_button().click()
        browser.switch_to.window(browser.window_handles[1])
        assert browser.current_url == "https://tensor.ru/", "url not found"

    with allure.step("Check block"):
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((
            By.XPATH,
            '//*[@class="tensor_ru-VideoBanner__bannerText s-Grid--hide-sm"]'
            )))
        assert tensor_page.check_block("Сила в людях")

    with allure.step("Click on about"):
        button = tensor_page.find_about_block()
        browser.execute_script("arguments[0].scrollIntoView(true);", button)
        button.click()
        assert browser.current_url == "https://tensor.ru/about"

    with allure.step("Check images size"):
        tensor_page.check_images_size()
