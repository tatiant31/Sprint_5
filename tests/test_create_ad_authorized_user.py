from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import data
from data import VALID_USER
from data import TEST_AD
from locators import TestLocators

class TestCreateAdAuthorizedUser:
    def test_create_ad_authorized_user(self, driver):
        #Авторизоваться под заранее созданным пользователем.
        driver.get(data.URL)
        # Ожидать загрузку страницы и нажать кнопку «Вход и регистрация».
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable
            (TestLocators.LOGIN_BUTTON)).click()
        # Заполняем email
        (driver.find_element(*TestLocators.EMAIL_INPUT).
         send_keys(VALID_USER.email))
        # Заполнить пароль
        (driver.find_element(*TestLocators.PASSWORD_INPUT).
         send_keys(VALID_USER.password))
        # Нажать кнопку Войти
        WebDriverWait(driver, 15).until(
            expected_conditions.element_to_be_clickable
            (TestLocators.ENTER_BUTTON)).click()
        # Проверить Кнопка «Разместить объявление» присутствует
        place_ad_btn = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(TestLocators.PLACE_ADVERTISEMENT_BUTTON))
        assert place_ad_btn.is_displayed(), "Кнопка 'Разместить объявление' не видна после логина"
        # Ждем кликабельную кнопку И сразу кликаем ActionChains
        ActionChains(driver).move_to_element(place_ad_btn).click().perform()
        WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located(TestLocators.ADV_NAME))
        # Заполнение текстовых полей
        driver.find_element(*TestLocators.ADV_NAME).send_keys(TEST_AD.title)
        #driver.find_element(*AuthorisationLocators.ADV_DESCRIPTION).send_keys(data.ad_data['description'])
        driver.execute_script("arguments[0].value = arguments[1];",
                              driver.find_element(*TestLocators.ADV_DESCRIPTION),
                              TEST_AD.description)
        driver.find_element(*TestLocators.ADV_PRICE).send_keys(TEST_AD.price)
        # Кликаем по полю для открытия списка в dropdown «Категорию»
        driver.find_element(*TestLocators.ADV_CATEGORY_INPUT).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
            (TestLocators.ADV_CATEGORY_SELECT))
        # JS-клик
        driver.execute_script("arguments[0].click();",
            driver.find_element(By.XPATH, "//*[contains(text(), 'Авто')][1]"))
        # Выбрать из Dropdown «Город»
        driver.find_element(*TestLocators.ADV_CITY).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
            (TestLocators.ADV_CITY_SELECT))
        driver.execute_script("arguments[0].click();",
            driver.find_element(By.XPATH, "//*[contains(text(), 'Москва')][1]"))
        # Выбрать RadioButton «Состояние товара».
        driver.find_element(By.XPATH, "//label[contains(text(), 'Новый')]").click()
        # Нажать кнопку «Опубликовать».
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable
            (TestLocators.PUBLISH_BUTTON)).click()
        # Перейти в профиль пользователя.
        avatar = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable
            (TestLocators.AVATAR_BUTTON))
        driver.execute_script("arguments[0].click();", avatar)
        # Проверить: в блоке «Мои объявления» отображается созданное объявление.
        ad_title = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located
            ((By.XPATH, f"//*[contains(text(), {TEST_AD.title})]")))
        assert ad_title.is_displayed(), f"Объявление '{TEST_AD.title}' не найдено в профиле"

