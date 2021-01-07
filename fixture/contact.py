from model.add_new import Add_New


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_new_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("Number of results: ")) > 0):
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
        self.cont_cache = None

    def test_edit_add(self, new):
        wd = self.app.wd
        self.open_edit_page()
        # Изменить данные
        self.fill_new_firms(new)
        # Нажать на Update
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_home_page()
        self.cont_cache = None

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


    def test_delete_first_new(self):
        wd = self.app.wd
        # Выбрать первый контакт
        wd.find_element_by_name("selected[]").click()
        # Удалить контакт
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_home_page()
        self.cont_cache = None

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.return_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    cont_cache = None

    def get_contact_list(self):
        if self.cont_cache is None:
            wd = self.app.wd
            self.return_home_page()
            self.cont_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("id")
                lastname = element.find_element_by_xpath("./td[2]").text
                firstname = element.find_element_by_xpath("./td[3]").text
                self.cont_cache.append(Add_New(id=id, firstname=firstname, lastname=lastname))
        return list(self.cont_cache)
