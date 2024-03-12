# Локаторы
from selenium.webdriver.common.by import By

class Test_Locators():
    ENTER_ACCOUNT = By.XPATH, '//*[contains(@class,"button_button_size_large")]'    # Войти в аккаунт
    PERSONAL_CABINET = By.XPATH, "//a[@href='/account']"                            # Войти в личный кабинет
    NEW_USER = By.XPATH, "//p[contains(@class,'undefined text')]"                   # Вы — новый пользователь? Зарегистрироваться
    REGISTRATION_FORM = By.XPATH, "//h2[text()='Регистрация']"                      # Заголовок "Регистрация"
    ENTER_IN_REG_FORM = By.XPATH, "//a[@href='/login']"                             # Кнопка "Войти" в форме регистрации
    CONSTRUCTOR = By.XPATH, "//a[@href='/']"                                        # Кнопка Конструктор
    TO_REGISTRATE = By.XPATH, "//a[@href='/register']"                              # Зарегистрироваться
    FORGOT_PASSWORD = By.XPATH, "//a[@href='/forgot-password']"                     # Забыли пароль
    PASSWORD_REINSTALL = By.XPATH, "//h2[text()='Восстановление пароля']"           # Восстановление пароля
    INPUT_EMAIL = By.XPATH, "//label[text()='Email']/following::input"              # Ввод логина
    EMAIL_PLACEHOLDER = By.XPATH, "//div[contains(@class,'input pr-6')]"            # Плейсхолдер Email в пустом поле логина
    INPUT_PASSWORD = By.XPATH, "//label[text()='Пароль']/following::input"          # Ввод пароля
    ENTER_TEXT = By.XPATH, "//h2[text()='Вход']"                                    # Заголовко "Вход"
    THE_SITE_IN = By.XPATH, "//button[contains(@class,'button_button')]"            # Кнопка Войти
    COLLECT_YOUR_BURGER = By.TAG_NAME, "h1"                                         # Собери свой бургер
    THE_SITE_OUT = By.XPATH, "//button[text()='Выход']"                             # Выход - в личном кабинете
    BUNS = By.XPATH, "//div[contains(@class,'tab_tab__1SPyG ')]"                    # Меню - Булки
    SAUCES = By.XPATH, "//span[text()='Соусы']"                                     # Меню - Соусы
    FILLINGS = By.XPATH, "//span[text()='Начинки']"                                 # Меню - Начинки
    BURGER = By.CSS_SELECTOR, "html > body > div > div > header > nav > div > a > svg"          # Логотип StellaBurger
    PERSONAL_CABINET_TEXT = By.XPATH, "//p[contains(@class,'Account_text')]"        # "В этом разделе вы можете изменить свои персональные данные"
    LIST_OF_BUNS = By.XPATH, "//h2[contains(@class,'text text_type_main-medium')]"  # Список булок
    LIST_OF_SAUCES = By.XPATH, "//ul[@class='BurgerIngredients_ingredients__list__2A-mT']/following-sibling::h2"        # Список соусов
    LIST_OF_FILLINGS = By.CSS_SELECTOR, "div#root>div>main>section>div:nth-of-type(2)>h2:nth-of-type(3)"                # Список начинок
    REGISTRATION_NAME = By.XPATH, "//input[@name='name']"                           # Регистрация нового пользователя - имя
    REGISTRATION_EMAIL = By.XPATH, "//label[text()='Email']/following::input"       # Регистрация нового пользователя - email
    REGISTRATION_PASSWORD = By.NAME, "Пароль"                                       # Регистрация нового пользователя - пароль
    WRONG_FORMAT = By.XPATH, "//p[@class='input__error text_type_main-default']"    # Некорректный пароль