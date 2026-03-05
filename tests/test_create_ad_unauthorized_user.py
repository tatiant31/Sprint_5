from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests import data
from tests.locators import AuthorisationLocators

class TestCreateAdUnauthorizedUser():
    def test_create_ad_unauthorized_user(self, driver):
        driver.get(data.URL)
        # Ожидать загрузку страницы и нажать кнопку «Разместить объявление».
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable
            (AuthorisationLocators.PLACE_ADVERTISEMENT_BUTTON)).click()
        #Проверить отображается модальное окно
        # заголовком «Чтобы разместить объявление, авторизуйтесь»
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(AuthorisationLocators.WINDOW_ADVERTISEMENT))
        #Модальное окно отображается
        modal_window = driver.find_element(*AuthorisationLocators.WINDOW_ADVERTISEMENT)
        assert modal_window.is_displayed()
        print("✓ Модальное окно объявления отображается")
        # заголовок «Чтобы разместить объявление, авторизуйтесь»
        modal_title = driver.find_element(*AuthorisationLocators.WINDOW_TITLE)
        assert modal_title.text == "Чтобы разместить объявление, авторизуйтесь"
        print("✓ Заголовок модального окна - 'Чтобы разместить объявление, авторизуйтесь'")

