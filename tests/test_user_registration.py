from helpers import *
from locators import TestLocators

class TestUserRegistration:
    # Проверяет, что кнопка «Разместить объявление» отображается после успешной регистрации
    def test_place_advertisement_button_displayed_after_registration(self, driver):
        register_new_user(driver)
        place_ad_btn = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located
            (TestLocators.PLACE_ADVERTISEMENT_BUTTON))
        assert place_ad_btn.text == "Разместить объявление", "Неверный текст кнопки"

    def  test_avatar_button_displayed_after_registration(self, driver):
        #Проверяет, что кнопка аватара отображается после успешной регистрации
        register_new_user(driver)
        # Проверить кнопку аватара есть на главной странице
        avatar_element = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(TestLocators.AVATAR_BUTTON))
        assert avatar_element.is_displayed(), "Аватар не отображается"

    def test_user_name_displayed_after_registration(self, driver):
        #Проверяет, что имя пользователя 'User.' отображается после успешной регистрации
        register_new_user(driver)
        user_name_element = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located
            (TestLocators.USER_NAME))
        assert user_name_element.text.strip() == "User.", f"Ожидалось 'User.', получено: '{user_name_element.text}'"
