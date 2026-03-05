from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from tests import data
from tests.locators import AuthorisationLocators

class TestCreateAdAuthorizedUser:
    def test_create_ad_authorized_user(self, driver):
        #Авторизоваться под заранее созданным пользователем.
        driver.get(data.URL)
        # Ожидать загрузку страницы и нажать кнопку «Вход и регистрация».
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable
            (AuthorisationLocators.LOGIN_BUTTON)).click()
        # Заполняем email
        (driver.find_element(*AuthorisationLocators.EMAIL_INPUT).
         send_keys(data.user_email))
        # Заполнить пароль
        (driver.find_element(*AuthorisationLocators.PASSWORD_INPUT).
         send_keys(data.user_password))
        # Нажать кнопку Войти
        WebDriverWait(driver, 15).until(
            expected_conditions.element_to_be_clickable
            (AuthorisationLocators.ENTER_BUTTON)).click()
        # Проверить Кнопка «Разместить объявление» присутствует
        print("✓ Авторизация успешна")
        # Ждем кликабельную кнопку И сразу кликаем ActionChains
        btn = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable
            (AuthorisationLocators.PLACE_ADVERTISEMENT_BUTTON))
        ActionChains(driver).move_to_element(btn).click().perform()
        print("✓ Кнопка нажата")
        # Ждем
        WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located
            (AuthorisationLocators.ADV_NAME))
        print("✓ Форма создания объявления загружена")
        # Заполнение текстовых полей
        (driver.find_element(*AuthorisationLocators.ADV_NAME).
         send_keys(data.ad_data['title']))
        print("✓ Название введено")
        #driver.find_element(*AuthorisationLocators.ADV_DESCRIPTION).send_keys(data.ad_data['description'])
        driver.execute_script("arguments[0].value = arguments[1];",
                              driver.find_element(*AuthorisationLocators.ADV_DESCRIPTION),
                              data.ad_data['description'])
        print("✓ Описание введено")
        (driver.find_element(*AuthorisationLocators.ADV_PRICE).
         send_keys(data.ad_data['price']))
        print("✓ Стоимость введена")
        # Кликаем по полю для открытия списка в dropdown «Категорию»
        driver.find_element(*AuthorisationLocators.ADV_CATEGORY_INPUT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located
            (AuthorisationLocators.ADV_CATEGORY_SELECT))
        # JS-клик
        driver.execute_script("arguments[0].click();",
                              driver.find_element(By.XPATH, "//*[contains(text(), 'Авто')][1]"))
        print("✓ Категория выбрана!")
        # Выбрать из Dropdown «Город»
        driver.find_element(*AuthorisationLocators.ADV_CITY).click()
        print("✓ Поле города открыто")

        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located
                (AuthorisationLocators.ADV_CITY_SELECT)
                )
        driver.execute_script("arguments[0].click();",
                              driver.find_element(By.XPATH, "//*[contains(text(), 'Москва')][1]"))
        print("✓ Город 'Москва' выбран!")
        # Выбрать RadioButton «Состояние товара».
        driver.find_element(By.XPATH, "//label[contains(text(), 'Новый')]").click()

        # Нажать кнопку «Опубликовать».
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable
            (AuthorisationLocators.PUBLISH_BUTTON)).click()
        print("✓ Опубликовано")
        # Перейти в профиль пользователя.
        avatar = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable
            (AuthorisationLocators.AVATAR_BUTTON))
        driver.execute_script("arguments[0].click();", avatar)
        print("✓ В профиле")
        # Проверить: в блоке «Мои объявления» отображается созданное объявление.
        ad_title = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located
            ((By.XPATH, f"//*[contains(text(), {data.ad_data['title']})]")))
        assert ad_title.is_displayed()
        print("✓ Созданное объявление найдено в 'Мои объявления'")
