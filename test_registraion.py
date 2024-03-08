# Выполнить регистрацию
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from locators_for_testing import Test_Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestRegistration():
    @staticmethod
    def minto_registration_for(driver):
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

    def test_succesfull_registration_of_new_member(self, new_user_info):
        options = Options()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
        driver.get("https://stellarburgers.nomoreparties.site/")
        TestRegistration.into_registration_form(driver)
        # Ввести валидное Имя нового пользователя
        if new_user_info["name"] != "":
            driver.find_element(*Test_Locators.REGISTRATION_NAME).send_keys(new_user_info['name'])
        # Ввести валидную почту нового пользователя
        if (new_user_info["login"].endswith('@ya.ru') and (len(new_user_info["login"]) > 6)):
            driver.find_element(*Test_Locators.REGISTRATION_EMAIL).send_keys(new_user_info['login'])
        # Ввести валидный пароль нового пользователя
        if len(new_user_info['password']) >= 6:
            driver.find_element(*Test_Locators.REGISTRATION_PASSWORD).send_keys(new_user_info['password'])
        # Нажать кнопку "Зарегистрироваться"
        driver.find_element(*Test_Locators.THE_SITE_IN).click()
        # Дождись, что открылась форма авторизации с заголовком "Вход"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Test_Locators.ENTER_TEXT)))
        assert driver.find_element(*Test_Locators.ENTER_TEXT).text == "Вход"
        # Выйти из браузера
        driver.quit()

    def test_registration_of_new_member_with_empty_name(self, new_user_info, incorrect_user_info):
        options = Options()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
        driver.get("https://stellarburgers.nomoreparties.site/")
        TestRegistration.into_registration_form(driver)
        # Ввести пустое Имя нового пользователя
        driver.find_element(*Test_Locators.REGISTRATION_NAME).send_keys(incorrect_user_info['name'])
        # Ввести валидную почту нового пользователя
        driver.find_element(*Test_Locators.REGISTRATION_EMAIL).send_keys(new_user_info['login'])
        # Ввести валидный пароль нового пользователя
        driver.find_element(*Test_Locators.REGISTRATION_PASSWORD).send_keys(new_user_info['password'])
        # Нажать кнопку "Зарегистрироваться"
        driver.find_element(*Test_Locators.THE_SITE_IN).click()
        assert driver.find_element(*Test_Locators.REGISTRATION_FORM).text != "Вход"
        # Выйти из браузера
        driver.quit()

    def test_registration_of_new_member_with_wrong_email_format(self, new_user_info, incorrect_user_info):
        options = Options()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
        driver.get("https://stellarburgers.nomoreparties.site/")
        TestRegistration.into_registration_form(driver)
        # Ввести валидное Имя нового пользователя
        driver.find_element(*Test_Locators.REGISTRATION_NAME).send_keys(new_user_info['name'])
        # Ввести почту нового пользователя в некорректном формате
        driver.find_element(*Test_Locators.REGISTRATION_EMAIL).send_keys(incorrect_user_info['login'])
        # Ввести валидный пароль нового пользователя
        driver.find_element(*Test_Locators.REGISTRATION_PASSWORD).send_keys(new_user_info['password'])
        # Нажать кнопку "Зарегистрироваться"
        driver.find_element(*Test_Locators.THE_SITE_IN).click()
        # Дождись, что появилась надпись "Такой пользователь уже существует"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Test_Locators.WRONG_FORMAT)))
        assert driver.find_element(*Test_Locators.WRONG_FORMAT).text == "Такой пользователь уже существует"
        driver.quit()

    def test_registration_of_new_member_with_wrong_password_format(self, new_user_info, incorrect_user_info):
        options = Options()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
        driver.get("https://stellarburgers.nomoreparties.site/")
        TestRegistration.into_registration_form(driver)
        # Ввести валидное Имя нового пользователя
        driver.find_element(*Test_Locators.REGISTRATION_NAME).send_keys(new_user_info['name'])
        # Ввести валидную почту нового пользователя
        driver.find_element(*Test_Locators.REGISTRATION_EMAIL).send_keys(new_user_info['login'])
        # Ввести пароль нового пользователя - меньше 6 символов
        driver.find_element(*Test_Locators.REGISTRATION_PASSWORD).send_keys(incorrect_user_info['password'])
        # Нажать кнопку "Зарегистрироваться"
        driver.find_element(*Test_Locators.THE_SITE_IN).click()
        # Дождись, что появилась надпись "Некорректный пароль"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.WRONG_FORMAT)))
        assert driver.find_element(*Test_Locators.WRONG_FORMAT).text == "Некорректный пароль"
        driver.quit()
