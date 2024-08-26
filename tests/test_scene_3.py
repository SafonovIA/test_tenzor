import allure
from pages.sbis_page import SbisPage
from get_file_size import wait_for_dowload, get_size


@allure.feature("scene_3")
def test_scene_3(browser):
    sbis_page = SbisPage(browser)

    with allure.step("Open page"):
        sbis_page.open()

    with allure.step("Dowload button click"):
        sbis_page.dowload_button().click()

    with allure.step("Windows button click"):
        sbis_page.windows_button().click()

    with allure.step("Sbis plagin button click"):
        sbis_page.sbis_button().click()

    with allure.step("Dowload file"):
        sbis_page.dowload_file().click()

    with allure.step("Check size file"):
        if wait_for_dowload():
            assert sbis_page.check_size_file() == get_size()
        else:
            assert False, "Не верный размер файла"
