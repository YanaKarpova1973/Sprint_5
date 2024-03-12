#  Переход из личного кабинета в конструктор
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators_for_testing import Test_Locators
import datatest

class TestTransferTheFolders():

    def test_transfer_to_constructor_by_text_button(self, driver):   # Переход в конструктор по кнопке Конструктор
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
        # Дождись перехода на основную страницу сайта и появления текста "Соберите бургер"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Test_Locators.COLLECT_YOUR_BURGER)))
        # Перейти в Личный кабинет
        driver.find_element(*Test_Locators.PERSONAL_CABINET).click()
        # Дождись, что появился текст "В этом разделе вы можете изменить свои персональные данные"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Test_Locators.PERSONAL_CABINET_TEXT)))
        # Перейти в Конструктор по кнопке "Конструктор"
        driver.find_element(*Test_Locators.CONSTRUCTOR).click()
        # Дождись перехода на основную страницу сайта и появления текста "Соберите бургер"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.COLLECT_YOUR_BURGER)))
        assert driver.find_element(*Test_Locators.COLLECT_YOUR_BURGER).text == "Соберите бургер"

    def test_transfer_to_constructor_by_burger_icon(self, driver):     # Переход в конструктор по логотипу StellaBurger
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
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Test_Locators.COLLECT_YOUR_BURGER)))
        # Перейти в Личный кабинет
        driver.find_element(*Test_Locators.PERSONAL_CABINET).click()
        # Дождись, что появился текст "В этом разделе вы можете изменить свои персональные данные"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Test_Locators.PERSONAL_CABINET_TEXT)))
        # Перейти в Конструктор по логотипу Бургер
        driver.find_element(*Test_Locators.BURGER).click()
        # Дождись перехода на основную страницу сайта и появления текста "Соберите бургер"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.COLLECT_YOUR_BURGER)))
        assert driver.find_element(*Test_Locators.COLLECT_YOUR_BURGER).text == "Соберите бургер"
