# Переход между разделами Конструктора
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators_for_testing import Test_Locators
import datatest

class TestConstructorChapters():

    def test_constructor_buns(self, driver):
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
        # Дождись перехода на основную страницу сайта, по умолчанию открыт раздел "Булки"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Test_Locators.LIST_OF_BUNS)))
        # Перейти в раздел "Начинки"
        driver.find_element(*Test_Locators.FILLINGS).click()
        # Дождись, что появился набор начинок
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Test_Locators.LIST_OF_FILLINGS)))
        # Перейти в раздел "Булки"
        driver.find_element(*Test_Locators.BUNS).click()
        # Дождись, что появился набор булок
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.LIST_OF_BUNS)))
        assert  driver.find_element(*Test_Locators.LIST_OF_BUNS).text == "Булки"

    def test_constructor_sauces(self, driver):
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
        # Дождись перехода на основную страницу сайта, по умолчанию открыт раздел "Булки"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Test_Locators.LIST_OF_BUNS)))
        # Перейти в раздел "Соусы"
        driver.find_element(*Test_Locators.SAUCES).click()
        # Дождись, что появился набор соусов
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.LIST_OF_SAUCES)))
        assert driver.find_element(*Test_Locators.LIST_OF_SAUCES).text == "Соусы"

    def test_constructor_fillings(self, driver):
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
        # Дождись перехода на основную страницу сайта, по умолчанию открыт раздел "Булки"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Test_Locators.LIST_OF_BUNS)))
        # Перейти в раздел "Начинки"
        driver.find_element(*Test_Locators.FILLINGS).click()
        # Дождись, что появился набор начинок
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.LIST_OF_FILLINGS)))
        assert driver.find_element(*Test_Locators.LIST_OF_FILLINGS).text == "Начинки"
