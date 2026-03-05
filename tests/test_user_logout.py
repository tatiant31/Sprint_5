from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests import data
from tests.locators import AuthorisationLocators

class TestUserLogout:
    def test_user_logout(self, driver):
        driver.get(data.URL)
        # Ожидать загрузку страницы и нажать кнопку «Вход и регистрация».
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable
            (AuthorisationLocators.LOGIN_BUTTON)).click()
        # Заполняем email
        driver.find_element(*AuthorisationLocators.EMAIL_INPUT).send_keys(data.user_email)
        # Заполнить пароль
        driver.find_element(*AuthorisationLocators.PASSWORD_INPUT).send_keys(data.user_password)
        # Нажать кнопку Войти
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable
            (AuthorisationLocators.ENTER_BUTTON)).click()
        #Нажать кнопку Выйти
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable
            (AuthorisationLocators.LOGOUT_BUTTON)).click()
        # Проверить аватар пользователя больше не отображается
        WebDriverWait(driver, 5).until_not(
            expected_conditions.presence_of_element_located
            (AuthorisationLocators.AVATAR_BUTTON))
        assert len(driver.find_elements(*AuthorisationLocators.AVATAR_BUTTON)) == 0
        print(" ✓ аватар пользователя больше не отображается")
        # Проверить  имя User больше не отображается
        WebDriverWait(driver, 5).until_not(
            expected_conditions.presence_of_element_located
            (AuthorisationLocators.USER_NAME))
        assert len(driver.find_elements(*AuthorisationLocators.USER_NAME)) == 0
        print(" ✓ имя User больше не отображается")
        # Проверить отображение кнопки «Вход и регистрация»
        login_button = driver.find_element(*AuthorisationLocators.LOGIN_BUTTON)
        assert login_button.is_displayed()
        print("✓ Кнопка 'Вход и регистрация' появилась")
        #кнопка Разместить объявление осталась
        place_ad_button = driver.find_element(*AuthorisationLocators.PLACE_ADVERTISEMENT_BUTTON)
        assert place_ad_button.is_displayed()
        print("✓ Кнопка 'Разместить объявление' видна")


