#  Переход в личный кабинет
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators_for_testing import Test_Locators
import datatest

class TestTransferToThePersonalAccount():

    def test_transfer_to_personal_account(self, driver):
        # Нажать кнопку "Войти в аккаунт"
        driver.find_element(*Test_Locators.ENTER_ACCOUNT).click()
        # Дождись, что появился текст Вход
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.ENTER_TEXT)))
        # Ввести логин пользователя
        driver.find_element(*Test_Locators.INPUT_EMAIL).send_keys(datatest.correct_user_info['login'])
        # Ввести пароль пользователя
        driver.find_element(*Test_Locators.INPUT_PASSWORD).send_keys(datatest.correct_user_info['password'])
        # Нажать на кнопку войти
        driver.find_element(*Test_Locators.THE_SITE_IN).click()
        # Дождись перехода на основную страницу сайта и появления текста "Собери бургер"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.COLLECT_YOUR_BURGER)))
        # Перейти в Личный кабинет
        driver.find_element(*Test_Locators.PERSONAL_CABINET).click()
        # Дождись, что появился текст "В этом разделе вы можете изменить свои персональные данные"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.PERSONAL_CABINET_TEXT)))
        assert driver.find_element(*Test_Locators.PERSONAL_CABINET_TEXT).text == "В этом разделе вы можете изменить свои персональные данные"
