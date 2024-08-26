from selenium.webdriver.common.by import By

# Вспомогательный файл для поиска эллементов

# Кнопка "Контакты"
contact_selector = (
    By.XPATH,
    '//*[@class="sbisru-Header__menu-item sbisru-Header__menu-item-1 mh-8  s-Grid--hide-sm"]'
    )

# Кнопка "Контакты" (нажата)
cont_selector = (
    By.XPATH,
    "//*[@class='sbisru-Header__menu-link sbisru-Header__menu-link--selected']"
    )

# Ссылка "Тензор"
tenzor_selector = (
    By.XPATH,
    '//*[@class="sbisru-Contacts__logo-tensor mb-12"]'
    )

# Блок с контактами
block_contacts_selector = (
    By.CLASS_NAME,
    'controls-ListViewV'
)

# Выбор региона
region_selector = (
    By.XPATH,
    '//*[@class="sbis_ru-Region-Chooser__text sbis_ru-link"]'
)

# Скачать
download_selector = (
    By.XPATH,
    '//*[@href="/download"]'
)

# Кнопка "Windows"
windows_selector = (
    By.XPATH,
    '//*[@class="sbis_ru-DownloadNew-innerTabs__title sbis_ru-DownloadNew-innerTabs__title--default"]'
    )

# Выбор плагина
sbis_plagin = (By.XPATH, '//*[@class="controls-TabButton__caption"]')

# Сслыка на скачивание
sbis_dowload_selector = (
    By.XPATH,
    '//*[@class="sbis_ru-DownloadNew-loadLink__link js-link"]'
    )

# Поиск блока
block_selector = (
    By.XPATH,
    '//*[@class="tensor_ru-link tensor_ru-Index__link"]'
)

# Поиск картинок
images_selector = (
    By.XPATH,
    '//*[@class="tensor_ru-About__block3-image-wrapper"]//img'
)
