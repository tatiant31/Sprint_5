from helpers import *
from locators import TestLocators

class TestUserRegistration:
    # Проверяет, что кнопка «Разместить объявление» отображается после успешной регистрации
    def test_place_advertisement_button_displayed_after_registration(self, driver):
        register_new_user(driver)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located
            (TestLocators.PLACE_ADVERTISEMENT_BUTTON))
        assert True, "Кнопка 'Разместить объявление' отображается после входа"

    def  test_avatar_button_displayed_after_registration(self, driver):
        #Проверяет, что кнопка аватара отображается после успешной регистрации
        register_new_user(driver)
        # Проверить кнопку аватара есть на главной странице
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located
            (TestLocators.AVATAR_BUTTON))
        assert True, "Кнопка аватара отображается после входа"

    def test_user_name_displayed_after_registration(self, driver):
        #Проверяет, что имя пользователя 'User.' отображается после успешной регистрации
        register_new_user(driver)
        user_name_element = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located
            (TestLocators.USER_NAME))
        assert user_name_element.text.strip() == "User.", f"Ожидалось 'User.', получено: '{user_name_element.text}'"
