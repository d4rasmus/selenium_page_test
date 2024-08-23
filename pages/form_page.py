from base_page import BasePage
from config.links import Links
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class FormPage(BasePage):

    url = Links.FORM_PAGE

    def open(self):
        self.driver.get(self.url)

    FIRSTNAME_FIELD = (By.ID, "firstName")
    LASTNAME_FIELD = (By.ID, "lastName")
    email_input = (By.ID, "userEmail")
    gender_radio = (By.XPATH, "//label[text()='Male']")
    mobile_input = (By.ID, "userNumber")
    date_of_birth_input = (By.ID, "dateOfBirthInput")
    subjects_input = (By.ID, "subjectsInput")
    hobbies_checkbox = (By.XPATH, "//label[text()='Sports']")
    upload_picture = (By.ID, "uploadPicture")
    address_input = (By.ID, "currentAddress")
    state_dropdown = (By.ID, "react-select-3-input")
    city_dropdown = (By.ID, "react-select-4-input")
    submit_button = (By.ID, "submit")

    def fill_first_name(self, first_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)

    def fill_last_name(self, last_name):
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    def fill_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def select_gender(self):
        self.driver.find_element(*self.gender_radio).click()

    def fill_mobile(self, mobile):
        self.driver.find_element(*self.mobile_input).send_keys(mobile)

    def fill_date_of_birth(self, dob):
        self.driver.find_element(*self.date_of_birth_input).click()
        self.driver.find_element(*self.date_of_birth_input).send_keys(dob)

    def fill_subjects(self, subjects):
        self.driver.find_element(*self.subjects_input).send_keys(subjects)

    def select_hobbies(self):
        self.driver.find_element(*self.hobbies_checkbox).click()

    def upload_file(self, file_path):
        self.driver.find_element(*self.upload_picture).send_keys(file_path)

    def fill_address(self, address):
        self.driver.find_element(*self.address_input).send_keys(address)

    def select_state(self, state):
        state_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.state_dropdown)
        )
        state_input.send_keys(state)
        state_input.send_keys("\n")

    def select_city(self, city):
        city_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.city_dropdown)
        )
        city_input.send_keys(city)
        city_input.send_keys("\n")

    def submit_form(self):
        self.driver.find_element(self.submit_button).click()
