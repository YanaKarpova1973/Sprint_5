# Выполнить регистрацию
import pytest
import random
from locators_for_testing import Test_Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import datatest

class TestRegistration():

    @pytest.mark.parametrize("valid_name,valid_password", [("Вася", "123456")])
    def test_succesfull_registration_of_new_member(self, driver, valid_name, valid_password):   # Проверка ввода валидных данных
        # Генерация логина - email
        valid_login = 'karpova_' + str(random.randint(100, 999)) + '@ya.ru'
        # Перейти в личный кабинет
        driver.find_element(*Test_Locators.PERSONAL_CABINET).click()
        # Дождись, что появился текст "Вы — новый пользователь? Зарегистрироваться"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Test_Locators.NEW_USER)))
        # Нажми на кнопку "Зарегистрироваться"
        driver.find_element(*Test_Locators.TO_REGISTRATE).click()
        # Дождись, что открылась форма регистрации с заголовком "Регистрация"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Test_Locators.REGISTRATION_FORM)))
        # Ввести валидное Имя нового пользователя
        driver.find_element(*Test_Locators.REGISTRATION_NAME).send_keys(valid_name)
        # Ввести валидную почту нового пользователя
        driver.find_element(*Test_Locators.REGISTRATION_EMAIL).send_keys(valid_login)
        # Ввести валидный пароль нового пользователя
        driver.find_element(*Test_Locators.REGISTRATION_PASSWORD).send_keys(valid_password)
        # Нажать кнопку "Зарегистрироваться"
        driver.find_element(*Test_Locators.THE_SITE_IN).click()
        # Дождись, что открылась форма авторизации с заголовком "Вход"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Test_Locators.ENTER_TEXT)))
        assert  driver.find_element(*Test_Locators.ENTER_TEXT).text == "Вход"

    def test_registration_of_new_member_with_empty_name(self, driver):          # Проверка ввода пустого имени
        # Перейти в личный кабинет
        driver.find_element(*Test_Locators.PERSONAL_CABINET).click()
        # Дождись, что появился текст "Вы — новый пользователь? Зарегистрироваться"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Test_Locators.NEW_USER)))
        # Нажми на кнопку "Зарегистрироваться"
        driver.find_element(*Test_Locators.TO_REGISTRATE).click()
        # Дождись, что открылась форма регистрации с заголовком "Регистрация"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Test_Locators.REGISTRATION_FORM)))
        # Ввести пустое Имя нового пользователя
        driver.find_element(*Test_Locators.REGISTRATION_NAME).send_keys(datatest.incorrect_user_info['name'])
        # Ввести валидную почту нового пользователя
        driver.find_element(*Test_Locators.REGISTRATION_EMAIL).send_keys(datatest.new_user_info['login'])
        # Ввести валидный пароль нового пользователя
        driver.find_element(*Test_Locators.REGISTRATION_PASSWORD).send_keys(datatest.new_user_info['password'])
        # Нажать кнопку "Зарегистрироваться"
        driver.find_element(*Test_Locators.THE_SITE_IN).click()
        assert driver.find_element(*Test_Locators.REGISTRATION_FORM).text != "Вход"

    def test_registration_of_new_member_with_wrong_email_format(self, driver):      # Проверка ввода некорректного формата email
        # Дождись, что появился текст "Вы — новый пользователь? Зарегистрироваться"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Test_Locators.NEW_USER)))
        # Нажми на кнопку "Зарегистрироваться"
        driver.find_element(*Test_Locators.TO_REGISTRATE).click()
        # Дождись, что открылась форма регистрации с заголовком "Регистрация"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Test_Locators.REGISTRATION_FORM)))
        # Ввести валидное Имя нового пользователя
        driver.find_element(*Test_Locators.REGISTRATION_NAME).send_keys(datatest.new_user_info['name'])
        # Ввести почту нового пользователя в некорректном формате
        driver.find_element(*Test_Locators.REGISTRATION_EMAIL).send_keys(datatest.incorrect_user_info['login'])
        # Ввести валидный пароль нового пользователя
        driver.find_element(*Test_Locators.REGISTRATION_PASSWORD).send_keys(datatest.new_user_info['password'])
        # Нажать кнопку "Зарегистрироваться"
        driver.find_element(*Test_Locators.THE_SITE_IN).click()
        # Дождись, что появилась надпись "Такой пользователь уже существует"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Test_Locators.WRONG_FORMAT)))
        assert driver.find_element(*Test_Locators.REGISTRATION_FORM).text != "Вход"

    def test_registration_of_new_member_with_wrong_password_format(self, driver):       # Проверка некорректного формата пароля
        # Дождись, что появился текст "Вы — новый пользователь? Зарегистрироваться"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Test_Locators.NEW_USER)))
        # Нажми на кнопку "Зарегистрироваться"
        driver.find_element(*Test_Locators.TO_REGISTRATE).click()
        # Дождись, что открылась форма регистрации с заголовком "Регистрация"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Test_Locators.REGISTRATION_FORM)))
        # Ввести валидное Имя нового пользователя
        driver.find_element(*Test_Locators.REGISTRATION_NAME).send_keys(datatest.new_user_info['name'])
        # Ввести валидную почту нового пользователя
        driver.find_element(*Test_Locators.REGISTRATION_EMAIL).send_keys(datatest.new_user_info['login'])
        # Ввести пароль нового пользователя - меньше 6 символов
        driver.find_element(*Test_Locators.REGISTRATION_PASSWORD).send_keys(datatest.incorrect_user_info['password'])
        # Нажать кнопку "Зарегистрироваться"
        driver.find_element(*Test_Locators.THE_SITE_IN).click()
        # Дождись, что появилась надпись "Некорректный пароль"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.WRONG_FORMAT)))
        assert driver.find_element(*Test_Locators.WRONG_FORMAT).text == "Некорректный пароль"
