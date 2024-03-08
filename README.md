Основная цель проекта: 
Проведение автоматизированного тестирования общего функционала сайта https://stellarburgers.nomoreparties.site/

Проект содержит:
1. 6 файлов с тестами:


    test_registration.py
    В файле создан класс TestRegistration, который имеет один статический метод 
    into_registration_for для входа на форму регистрации через личный кабинет
    и 4 метода для тестирования следующего функционала:
    - test_succesfull_registration_of_new_member 
           - успешная регистрация для пользователя с валидными данными
    - test_registration_of_new_member_with_empty_name 
           - попытка регистрации для пользователя с пустым значением в поле "Имя"
    - test_registration_of_new_member_with_wrong_email_format 
           - попытка регистрации для пользователя с некорректным форматом Email
    - test_registration_of_new_member_with_wrong_password_format 
           - попытка регистрации для пользователя с некорректным форматом пароля (меньше 6 символов)
 

    test_in_to_the_site.py
    В файле создан класс TestTheSiteIn, который имеет один статический метод fill_the_fields для авторизации на сайте
    и 4 метода для тестирования следующего функционала:
    - test_enter_the_account - вход по кнопке «Войти в аккаунт» на главной странице
    - test_entering_through_the_personal_cabinet - вход через кнопку «Личный кабинет»
    - test_enter_throuth_the_registration_form - вход через кнопку в форме регистрации
    - test_enter_throuth_forgot_password_form - вход через кнопку в форме восстановления пароля
       
    test_leave_the_site.py
    В файле создан класс TestTheSiteOut, который имеет один метод test_the_site_out 
    для тестирования выхода по кнопке «Выйти» в личном кабинете.
    
    test_transfer_to_personal_account.py
    В файле создан класс TestTransferToThePersonalAccount, который имеет один 
    метод test_transfer_to_personal_account 
    для тестирования перехода по клику на «Личный кабинет».

    test_transfer_to_constructor.py
    В файле создан класс TestTransferTheFolders, который имеет один статический метод 
    into_personal_cabinet для авторизации на сайте и 2 метода для тестирования
    перехода из личного кабинета в Конструктор:    
    - test_transfer_to_constructor_by_text_button - переход по клику на «Конструктор»
    - test_transfer_to_constructor_by_burger_icon - переход по клику на логотип Stellar Burgers

    test_constructor_sections.py
    В файле создан класс TestConstructorChapters, который имеет один статический метод 
    into_personal_cabinet для авторизации на сайте и 3 метода для тестирования
    переходов в разделы Конструктора бургеров:
    - test_constructor_buns -  переход к разделу «Булки»
    - test_constructor_sauces - переход к разделу «Соусы»
    - test_constructor_fillings - переход к разделу «Начинки»

2. locators_for_testing.py - файл с используемыми локаторами
3. conftest.py - используемые фикструры в тестах
