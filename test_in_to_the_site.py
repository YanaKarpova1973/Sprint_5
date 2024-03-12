# Выполнить вход на сайт
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators_for_testing import Test_Locators
import datatest

class TestTheSiteIn():

    def test_entering_through_the_personal_cabinet(self, driver):           # Вход через личный кабинет
        # Перейти в личный кабинет
        driver.find_element(*Test_Locators.PERSONAL_CABINET).click()
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
        assert driver.find_element(*Test_Locators.COLLECT_YOUR_BURGER).text == "Соберите бургер"

    def test_enter_the_account(self, driver):                   # Вход через "Войти в аккаунт"
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
        assert driver.find_element(*Test_Locators.COLLECT_YOUR_BURGER).text == "Соберите бургер"

    def test_enter_throuth_the_registration_form(self, driver):             # Вход через форму регистрации
        # Нажать кнопку "Войти в аккаунт"
        driver.find_element(*Test_Locators.ENTER_ACCOUNT).click()
        # Дождись, что появилась кнопка "Зарегистрироваться"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.TO_REGISTRATE)))
        # Нажать на кнопку "Зарегистрироваться"
        driver.find_element(*Test_Locators.TO_REGISTRATE).click()
        # Дождись, что появилась кнопка "Зарегистрироваться"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.ENTER_IN_REG_FORM)))
        # Нажать на кнопку "Войти"
        driver.find_element(*Test_Locators.ENTER_IN_REG_FORM).click()
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
        assert driver.find_element(*Test_Locators.COLLECT_YOUR_BURGER).text == "Соберите бургер"

    def test_enter_throuth_forgot_password_form(self, driver):              # Вход через форму "Забыли пароль"
        # Нажать кнопку "Войти в аккаунт"
        driver.find_element(*Test_Locators.ENTER_ACCOUNT).click()
        # Дождись, что появилась кнопка "Восстановить пароль"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.FORGOT_PASSWORD)))
        # Нажать на кнопку "Восстановить пароль"
        driver.find_element(*Test_Locators.FORGOT_PASSWORD).click()
        # Дождись, что появилась кнопка "Восстановление пароля"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.PASSWORD_REINSTALL)))
        # Нажать на кнопку "Войти"
        driver.find_element(*Test_Locators.ENTER_IN_REG_FORM).click()
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
        assert driver.find_element(*Test_Locators.COLLECT_YOUR_BURGER).text == "Соберите бургер"
