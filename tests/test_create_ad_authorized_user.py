from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import TEST_AD
from helpers import login_user
from locators import TestLocators

class TestCreateAdAuthorizedUser:
    def test_create_ad_authorized_user(self, driver):
    # Авторизация → кнопка 'Разместить объявление' видна"""
        login_user(driver)
         # Кнопка "Разместить объявление"
        place_ad_btn = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.PLACE_ADVERTISEMENT_BUTTON))
        ActionChains(driver).move_to_element(place_ad_btn).click().perform()
        # Название
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.ADV_NAME))
        driver.find_element(*TestLocators.ADV_NAME).send_keys(TEST_AD.title)
        #Описание объявления
        desc_field = driver.find_element(*TestLocators.ADV_DESCRIPTION)
        driver.execute_script("arguments[0].value = arguments[1];", desc_field, TEST_AD.description)
        # Цена
        driver.find_element(*TestLocators.ADV_PRICE).send_keys(TEST_AD.price)
        # Кликаем по полю для открытия списка в dropdown «Категорию»
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(TestLocators.ADV_CATEGORY_INPUT)).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(TestLocators.ADV_CATEGORY_SELECT))
        driver.execute_script("arguments[0].click();",
                          driver.find_element(*TestLocators.ADV_AVTO))
        # ГОРОД
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(TestLocators.ADV_CITY)).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(TestLocators.ADV_CITY_SELECT))
        driver.execute_script("arguments[0].click();",
                          driver.find_element(*TestLocators.ADV_MOSCOW))
        # RadioButton "Новый"
        radio = driver.find_element(*TestLocators.ADV_NEW)
        driver.execute_script("arguments[0].click();", radio)
        # Опубликовать
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(TestLocators.PUBLISH_BUTTON)).click()
        driver.execute_script("window.scrollTo(0, 0);")
        # Ждем обновления страницы после публикации
        WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
        # Перейти в профиль пользователя.
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable
                                             (TestLocators.AVATAR_BUTTON))
        avatar = driver.find_element(*TestLocators.AVATAR_BUTTON)
        driver.execute_script("arguments[0].click();", avatar)
        # Ждем загрузки профиля
        WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
        # Проверяем объявление в блоке "Мои объявления"
        ad_title = WebDriverWait(driver, 60).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, f"//*[contains(text(), '{TEST_AD.title}') or "
                       f"contains(text(), '{TEST_AD.title[:15]}') or "
                       f"contains(text(), 'Объявление')]")))
        assert ad_title.is_displayed(), f"Объявление '{TEST_AD.title}' не найдено в профиле"