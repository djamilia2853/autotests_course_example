# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common import exceptions
import time


login = "отправитель1"
password = "пароль123"
name_user = "Грузоотправитель Андрей"
message_sender = "Сообщение"

browser = webdriver.Chrome()
time.sleep(2)
try:

    browser.get("https://fix-online.sbis.ru/")
    assert browser.current_url == "https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/", 'Неверно открыт сайт'
    time.sleep(2)
    login_field = browser.find_element(By.CSS_SELECTOR,
                                       '[name="Login"]')

    login_field.send_keys(login)
    login_button = \
        browser.find_element(By.CSS_SELECTOR,
                             '[data-qa="auth-AdaptiveLoginForm__checkSignInTypeButton"]')
    login_button.click()
    time.sleep(2)
    password_field = browser.find_element(By.CSS_SELECTOR,
                                          '[name="Password"]')
    password_field.send_keys(password)
    login_button = browser.find_element(By.CSS_SELECTOR,
                                        '[data-qa="auth-AdaptiveLoginForm__signInButton"]')
    login_button.click()

    time.sleep(2)

    try:
        job_choice = browser.find_element(By.CSS_SELECTOR,
                                          '.controls-Button_outlined_style-secondary')
        job_choice.click()
    except exceptions.NoSuchElementException:
        time.sleep(2)
    else:
        time.sleep(4)
    contacts_accordion_button = browser.find_element(By.CSS_SELECTOR,
                                                     '[data-qa="Контакты"]')
    contacts_accordion_button.click()
    time.sleep(2)
    contacts_button = browser.find_element(By.CSS_SELECTOR,
                                           '[data-qa="NavigationPanels-SubMenu__head"] [data-qa="Контакты"]')
    contacts_button.click()
    time.sleep(2)

    browser.execute_script("window.scrollTo(document.body.scrollWidth, 0);")

    plus_button = browser.find_element(By.CSS_SELECTOR,
                                       '[data-qa="sabyPage-addButton"]')
    plus_button.click()
    time.sleep(2)
    search_box = browser.find_element(By.CSS_SELECTOR,
                                      '[data-qa="addressee-selector-root"] [data-qa="controls-Render__field"] input')
    search_box.send_keys(name_user)
    time.sleep(2)
    list_employee = \
        browser.find_elements(By.CSS_SELECTOR,
                              '[data-qa="addressee-selector-root"] [data-qa="controls-Scroll__content"] '
                              '[data-qa="items-container"].controls-BaseControl_showActions_onhover')
    assert len(list_employee) == 1, f"ожидали найти только одного сотрудника, но странице {len(list_employee)} записей"

    list_employee[0].click()
    time.sleep(2)
    message_field = browser.find_element(By.CSS_SELECTOR,
                                         '[data-qa="textEditor_slate_Field"]')
    message_field.send_keys(message_sender)
    time.sleep(2)
    submit_button = browser.find_element(By.CSS_SELECTOR,
                                         '[data-qa="msg-send-editor__send-button"]')
    submit_button.click()
    time.sleep(2)
    if login == "отправитель":
        close_message = browser.find_element(By.CSS_SELECTOR,
                                             '[data-qa="controls-stack-Button__close"]')
        close_message.click()
        time.sleep(2)
    list_message = browser.find_elements(By.CSS_SELECTOR,
                                         '.msg-dialogs-detail [data-qa="items-container"]')
    message = list_message[0].find_element(By.CSS_SELECTOR,
                                           '.msg-entity-text p')
    message_txt = message.text
    assert message_txt == message_sender, f"ожидали первым в списке сообщение с текстом : {message_sender} \n" \
                                          f"пришло: {message_txt}"
    sender = list_message[0].find_element(By.CSS_SELECTOR,
                                          '[data-qa="msg-dialogs-item__addressee"]')
    sender_txt = sender.text
    actions = ActionChains(browser)
    actions.move_to_element(sender).perform()
    time.sleep(2)
    delete_button = list_message[0].find_element(By.CSS_SELECTOR,
                                                 '[data-qa="controls-itemActions__action deleteToArchive"]')
    delete_button.click()
    time.sleep(2)

    list_message = browser.find_elements(By.CSS_SELECTOR,
                                         '.msg-dialogs-detail [data-qa="items-container"]')
    message = list_message[0].find_element(By.CSS_SELECTOR,
                                           '.msg-entity-text p')
    message_txt = message.text

    sender = list_message[0].find_element(By.CSS_SELECTOR,
                                          '[data-qa="msg-dialogs-item__addressee"]')
    sender_txt = sender.text
    assert name_user != sender_txt.split(" ")[0] \
           or message_txt != message_sender, f"ожидали что верхнее сообщение отличается отправителем или текстом:" \
                                             f"не должен быть отправитель: '{name_user}'\n" \
                                             f"текст: '{sender_txt}'"

finally:
    browser.quit()
