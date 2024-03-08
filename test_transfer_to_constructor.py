#  Переход из личного кабинета в конструктор

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators_for_testing import Test_Locators

class TestTransferTheFolders():

    @staticmethod
    def into_personal_cabinet(driver, user):
        # Нажать кнопку "Войти в аккаунт"
        driver.find_element(*Test_Locators.ENTER_ACCOUNT).click()
        # Дождись, что появился текст Вход
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.ENTER_TEXT)))
        # Ввести логин пользователя
        driver.find_element(*Test_Locators.INPUT_EMAIL).send_keys(user['login'])
        # Ввести пароль пользователя
        driver.find_element(*Test_Locators.INPUT_PASSWORD).send_keys(user['password'])
        # Нажать на кнопку войти
        driver.find_element(*Test_Locators.THE_SITE_IN).click()
        # Дождись перехода на основную страницу сайта и появления текста "Собери бургер"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Test_Locators.COLLECT_YOUR_BURGER)))
        # Перейти в Личный кабинет
        driver.find_element(*Test_Locators.PERSONAL_CABINET).click()
        # Дождись, что появился текст "В этом разделе вы можете изменить свои персональные данные"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Test_Locators.PERSONAL_CABINET_TEXT)))

    def test_transfer_to_constructor_by_text_button(self, correct_user_info):
        options = Options()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
        driver.get("https://stellarburgers.nomoreparties.site/")
        # Выполнить вход на сайт и перейти в Личный Кабинет
        TestTransferTheFolders.into_personal_cabinet(driver, correct_user_info)
        # Перейти в Конструктор по кнопке "Конструктор"
        driver.find_element(*Test_Locators.CONSTRUCTOR).click()
        # Дождись перехода на основную страницу сайта и появления текста "Собери бургер"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.COLLECT_YOUR_BURGER)))
        # Закрыть браузер
        driver.quit()

    def test_transfer_to_constructor_by_burger_icon(self, correct_user_info):
        options = Options()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
        driver.get("https://stellarburgers.nomoreparties.site/")
        # Выполнить вход на сайт и перейти в Личный Кабинет
        TestTransferTheFolders.into_personal_cabinet(driver, correct_user_info)
        # Перейти в Конструктор по логотипу Бургер
        driver.find_element(*Test_Locators.BURGER).click()
        # Дождись перехода на основную страницу сайта и появления текста "Собери бургер"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.COLLECT_YOUR_BURGER)))
        # Закрыть браузер
        driver.quit()
