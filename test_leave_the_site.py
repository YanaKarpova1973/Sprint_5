# Выйти из аккаунта

from selenium import webdriver
from locators_for_testing import Test_Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options

class TestTheSiteOut():

    def test_the_site_out(self, correct_user_info):
        options = Options()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
        driver.get("https://stellarburgers.nomoreparties.site/")
        # Перейти в личный кабинет
        driver.find_element(*Test_Locators.PERSONAL_CABINET).click()
        # Дождись, что появился текст Вход
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.ENTER_TEXT)))
        # Ввести логин пользователя
        driver.find_element(*Test_Locators.INPUT_EMAIL).send_keys(correct_user_info['login'])
        # Ввести пароль пользователя
        driver.find_element(*Test_Locators.INPUT_PASSWORD).send_keys(correct_user_info['password'])
        # Нажать на кнопку войти
        driver.find_element(*Test_Locators.THE_SITE_IN).click()
        # Дождись перехода на основную страницу сайта и появления текста "Собери бургер"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.COLLECT_YOUR_BURGER)))
        # Перейти в личный кабинет
        driver.find_element(*Test_Locators.PERSONAL_CABINET).click()
        # Дождись, что появился текст "В этом разделе вы можете изменить свои персональные данные"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.PERSONAL_CABINET_TEXT)))
        #time.sleep(5)
        # Нажать кнопку "Выход"
        driver.find_element(*Test_Locators.THE_SITE_OUT).click()
        # Дождаться отображения текста Вход на странице
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Test_Locators.ENTER_TEXT)))
        # Убедиться, что в поле логина отображается плейсхолдер Email
        assert driver.find_element(*Test_Locators.EMAIL_PLACEHOLDER).text == "Email"
        # Закрыть браузер
        driver.quit()
