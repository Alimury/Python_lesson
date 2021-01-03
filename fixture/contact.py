
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_new_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_edit_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def create_new(self, new):
        wd = self.app.wd
        self.open_new_page()
        # fill new firm
        self.fill_new_firms(new)
        # submit new creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_home_page()

    def fill_new_firms(self, new):
        self.change_field_value("firstname", new.firstname)
        self.change_field_value("lastname", new.lastname)
        self.change_field_value("address", new.address)
        self.change_field_value("home", new.telephone)
        self.change_field_value("email", new.email)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def test_edit_add(self, new):
        wd = self.app.wd
        self.open_edit_page()
        # Изменить данные
        self.fill_new_firms(new)
        # Нажать на Update
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_home_page()

    def test_delete_first_new(self):
        wd = self.app.wd
        # Выбрать первый контакт
        wd.find_element_by_name("selected[]").click()
        # Удалить контакт
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_home_page()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
