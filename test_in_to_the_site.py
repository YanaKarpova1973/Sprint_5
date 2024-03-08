# Выполнить вход на сайт

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators_for_testing import Test_Locators

class TestTheSiteIn():
    @staticmethod   # Метод для ввода логина и пароля и входа на страницу
    def fill_the_fields(driver, user):
        # Дождись, что появился текст Вход
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.ENTER_TEXT)))
        # Ввести логин пользователя
        driver.find_element(*Test_Locators.INPUT_EMAIL).send_keys(user['login'])
        # Ввести пароль пользователя
        driver.find_element(*Test_Locators.INPUT_PASSWORD).send_keys(user['password'])
        # Нажать на кнопку войти
        driver.find_element(*Test_Locators.THE_SITE_IN).click()
        # Дождись перехода на основную страницу сайта и появления текста "Собери бургер"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.COLLECT_YOUR_BURGER)))

    def test_entering_through_the_personal_cabinet(self, correct_user_info):
        options = Options()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
        driver.get("https://stellarburgers.nomoreparties.site/")
        # Перейти в личный кабинет
        driver.find_element(*Test_Locators.PERSONAL_CABINET).click()
        # Ввод пароля,логина и загрузка основной страницы
        TestTheSiteIn.fill_the_fields(driver, correct_user_info)
        driver.quit()

    def test_enter_the_account(self, correct_user_info):
        options = Options()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
        driver.get("https://stellarburgers.nomoreparties.site/")
        # Нажать кнопку "Войти в аккаунт"
        driver.find_element(*Test_Locators.ENTER_ACCOUNT).click()
        # Ввод пароля,логина и загрузка основной страницы
        TestTheSiteIn.fill_the_fields(driver, correct_user_info)
        # Закрыть браузер
        driver.quit()

    def test_enter_throuth_the_registration_form(self, correct_user_info):
        options = Options()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
        driver.get("https://stellarburgers.nomoreparties.site/")
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
        # Ввод пароля,логина и загрузка основной страницы
        TestTheSiteIn.fill_the_fields(driver, correct_user_info)
        # Закрыть браузер
        driver.quit()

    def test_enter_throuth_forgot_password_form(self, correct_user_info):
        options = Options()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
        driver.get("https://stellarburgers.nomoreparties.site/")
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
        # Ввод пароля,логина и загрузка основной страницы
        TestTheSiteIn.fill_the_fields(driver, correct_user_info)
        # Закрыть браузер
        driver.quit()
