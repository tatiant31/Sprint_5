from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from helpers import login_and_logout
import data

class TestUserLogout:
    def test_avatar_hidden_after_logout(self, driver):
        driver.get(data.URL)
        login_and_logout(driver)
        # Проверить аватар пользователя больше не отображается
        WebDriverWait(driver, 5).until_not(
            expected_conditions.presence_of_element_located(TestLocators.AVATAR_BUTTON))
        avatar = driver.find_elements(*TestLocators.AVATAR_BUTTON)
        assert len(avatar) == 0, f"Найдено {len(avatar)} элементов аватара после выхода: {[el.get_attribute('outerHTML')[:100] for el in avatar]}"

    def test_username_hidden_after_logout(self, driver):
        driver.get(data.URL)
        login_and_logout(driver)
        # Проверить  имя User больше не отображается
        WebDriverWait(driver, 5).until_not(
            expected_conditions.presence_of_element_located(TestLocators.USER_NAME))
        names = driver.find_elements(*TestLocators.USER_NAME)
        assert len(names) == 0, f"Найдено {len(names)} элементов имени после выхода. Тексты: {[name.text for name in names]}"

    def test_login_button_visible_after_logout(self, driver):
        driver.get(data.URL)
        login_and_logout(driver)
        # Проверить отображение кнопки «Вход и регистрация»
        login_button = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON))
        assert login_button.is_displayed(), "Кнопка входа не видна"

    def test_place_ad_button_visible_after_logout(self, driver):
        driver.get(data.URL)
        login_and_logout(driver)
        #кнопка Разместить объявление осталась
        place_ad_button = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.PLACE_ADVERTISEMENT_BUTTON))
        assert place_ad_button.is_displayed(), "Кнопка 'Разместить объявление' не видна"



