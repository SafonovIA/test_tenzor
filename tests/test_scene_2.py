from pages.sbis_page import SbisPage
import allure


@allure.feature("scene_2")
def test_scene_2(browser):
    sbis_page = SbisPage(browser)

    with allure.step("Open page"):
        sbis_page.open()
        sbis_page.contact_buttons().click()
    with allure.step("Check region"):
        assert sbis_page.check_region("Нижегородская обл.")
        assert sbis_page.check_block_contacts()

    with allure.step("Change region"):
        sbis_page.region_button().click()
        sbis_page.change_region("Камчатский край")

    with allure.step("Check region 2"):
        assert sbis_page.check_region("Камчатский край")
        assert sbis_page.check_block_contacts()
