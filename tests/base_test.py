import pytest

from pages.form_page import FormPage
# from pages.book_store_page import BookStorePage

class BaseTest:

    form_page: FormPage
    # book_store_page: BookStorePage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.form_page = FormPage(driver)
        # request.cls.book_store_page = BookStorePage(driver)