from model.add_new import Add_New
import re

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

    def open_edit_page_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def create_new(self, new):
        wd = self.app.wd
        self.open_new_page()
        # fill new firm
        self.fill_new_firms(new)
        # submit new creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_home_page()
        self.cont_cache = None

    def test_edit_add(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, new, index):
        wd = self.app.wd
        self.open_edit_page_by_index(index)
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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # Выбрать первый контакт
        self.select_contact_by_index(index)
        # Удалить контакт
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_home_page()
        self.cont_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def return_home_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("Number of results: ")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.return_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    cont_cache = None

    def get_contact_list(self):
        if self.cont_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.cont_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                address = cells[3].text
                all_email = cells[4].text
                all_phones = cells[5].text
                self.cont_cache.append(Add_New(id=id, firstname=firstname, lastname=lastname, address=address,
                                               all_email_from_home_page=all_email,
                                               all_phones_from_home_page=all_phones))
        return list(self.cont_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Add_New(firstname=firstname, lastname=lastname, id=id, address=address,
                       email=email, email2=email2, email3=email3,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Add_New(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)