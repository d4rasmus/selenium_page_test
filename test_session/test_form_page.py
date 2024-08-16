import pytest
from selenium import webdriver
from pages.form_page import FormPage

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    # yield
    # driver.quit()

@pytest.mark.usefixtures("setup")
class TestForm:
    def test_fill_form(self):
        form_page = FormPage(self.driver)
        form_page.open()
        form_page.fill_first_name("John")
        form_page.fill_last_name("Doe")
        form_page.fill_email("john.doe@example.com")
        # form_page.select_gender()
        form_page.fill_mobile("1234567890")
        form_page.fill_date_of_birth("01 Jan 2000")
        form_page.fill_subjects("Maths")
        # form_page.select_hobbies()
        form_page.upload_file("//home/rasmus/Downloads/unnamed.jpg")
        form_page.fill_address("123 Main St")
        form_page.select_state("NCR")
        form_page.select_city("Delhi")
        form_page.submit_form()

#
#
# class ="modal-title h4" id="example-modal-sizes-title-lg" > Thanks for submitting the form < / div
