from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
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

        #  «Категорию»
        category_input = WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located(TestLocators.ADV_CATEGORY_INPUT))
        driver.execute_script("arguments[0].click();", category_input)
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(TestLocators.ADV_CATEGORY_SELECT))
        driver.execute_script("arguments[0].click();", driver.find_element(*TestLocators.ADV_AVTO))
        # ГОРОД
        city_input = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(TestLocators.ADV_CITY))
        driver.execute_script("arguments[0].click();", city_input)
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(TestLocators.ADV_CITY_SELECT))
        driver.execute_script("arguments[0].click();",
                          driver.find_element(*TestLocators.ADV_MOSCOW))
        # RadioButton "Новый"
        radio = driver.find_element(*TestLocators.ADV_NEW)
        driver.execute_script("arguments[0].click();", radio)
        # Опубликовать
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(TestLocators.PUBLISH_BUTTON)).click()

        # Ждем полной загрузки страницы после публикации
        WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
        # Перейти в профиль пользователя.
        avatar = WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.AVATAR_BUTTON))
        driver.execute_script("arguments[0].click();", avatar)
        # ждем появление карточек
        WebDriverWait(driver, 15).until(
            lambda d: len(d.find_elements(*TestLocators.AVD_CARDS)) > 0)
        # Ищем объявление по заголовку
        ad_locator = TestLocators.AVD_TITLE
        ad_title = WebDriverWait(driver, 60).until(
            expected_conditions.presence_of_element_located(ad_locator)
        )
        assert ad_title.is_displayed(), "Объявление не найдено в профиле"