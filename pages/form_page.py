# from base_page import BasePage
import time
import random
from config.links import Links
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        self.driver.get(self.url)

    url = Links.FORM_PAGE

    FIRSTNAME_FIELD = (By.ID, "firstName")
    LASTNAME_FIELD = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "userEmail")
    GENDER_CHECKBOX = (By.XPATH, "//label[text()='Male']")
    PHONE_NUMBER_INPUT = (By.ID, "userNumber")
    DOB_INPUT = (By.ID, "dateOfBirthInput")
    SUBJECTS_INPUT = (By.ID, "subjectsInput")
    HOBBIES_CHECKBOX = (By.XPATH, f'//label[@for="hobbies-checkbox-{random.randint(1,3)}"]')
    PICTURE_UPLOAD = (By.ID, "uploadPicture")
    ADDRESS_INPUT = (By.ID, "currentAddress")
    STATE_DROPDOWN = (By.ID, "react-select-3-input")
    CITY_DROPDOWN = (By.ID, "react-select-4-input")
    SUBMIT_BUTTON = (By.ID, "submit")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".modal-title.h4")

    def fill_first_name(self, first_name):
        self.driver.find_element(*self.FIRSTNAME_FIELD).send_keys(first_name)

    def fill_last_name(self, last_name):
        self.driver.find_element(*self.LASTNAME_FIELD).send_keys(last_name)

    def fill_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def select_gender(self):
        self.driver.find_element(*self.GENDER_CHECKBOX).click()

    def fill_phone(self, phone):
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(phone)

    def fill_date_of_birth(self, dob):
        self.driver.find_element(*self.DOB_INPUT).click()
        self.driver.find_element(*self.DOB_INPUT).send_keys(dob)

    def fill_subjects(self, subjects):
        subjects = self.driver.find_element(*self.SUBJECTS_INPUT)
        subjects.send_keys(subjects)
        subjects.send_keys(Keys.ENTER)

    def select_hobbies(self):
        select_hobbies = self.wait.until(EC.element_to_be_clickable(self.HOBBIES_CHECKBOX))
        time.sleep(5)
        select_hobbies.click()

    def upload_file(self, file_path):
        self.driver.find_element(*self.PICTURE_UPLOAD).send_keys(file_path)

    def fill_address(self, address):
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)

    def select_state(self, state):
        state_input = self.driver.find_element(*self.STATE_DROPDOWN)
        state_input.send_keys(state)
        state_input.send_keys(Keys.ENTER)

    def select_city(self, city):
        city_input = self.driver.find_element(*self.CITY_DROPDOWN)
        city_input.send_keys(city)
        city_input.send_keys(Keys.ENTER)

    def submit_form(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        time.sleep(5)

    def success_message_display(self):
        success_message = self.driver.find_element(*self.SUCCESS_MESSAGE)
        assert success_message.is_displayed()
        assert success_message.text == "Thanks for submitting the form"