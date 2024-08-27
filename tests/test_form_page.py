import pytest
from selenium import webdriver
from pages.form_page import FormPage
from tests.base_test import BaseTest
from selenium.webdriver.common.by import By

# @pytest.fixture(scope="class")
# def setup(request):
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#     driver.quit()

@pytest.mark.usefixtures("setup")
class TestForm(BaseTest):
    def test_fill_form(self):
        self.form_page.open()
        self.form_page.fill_first_name("Test")
        self.form_page.fill_last_name("Testovich")
        self.form_page.fill_email("testing@ya.ru")
        self.form_page.select_gender()
        self.form_page.fill_phone("8805553535")
        self.form_page.fill_date_of_birth("01 Jan 2000")
        self.form_page.fill_subjects("Maths")
        self.form_page.select_hobbies()
        self.form_page.upload_file("//home/rasmus/Downloads/unnamed.jpg")
        self.form_page.fill_address("150000 Unnamed Street")
        self.form_page.select_state("NCR")
        self.form_page.select_city("Delhi")
        self.form_page.submit_form()
        self.form_page.success_message_display()


# class ="modal-title h4" id="example-modal-sizes-title-lg" > Thanks for submitting the form < / div
