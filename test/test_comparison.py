import re

def test_name_and_address_on_home_page(app):
    cont_from_home_page = app.contact.get_contact_list()[0]
    cont_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert cont_from_home_page.firstname == cont_from_edit_page.firstname
    assert cont_from_home_page.lastname == cont_from_edit_page.lastname
    assert cont_from_home_page.address == cont_from_edit_page.address


def test_email_on_home_page(app):
    cont_from_home_page = app.contact.get_contact_list()[0]
    cont_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert cont_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(cont_from_edit_page)



def test_phones_on_home_page(app):
    cont_from_home_page = app.contact.get_contact_list()[0]
    cont_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert cont_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(cont_from_edit_page)


def test_phones_on_contact_view_page(app):
    cont_from_view_page = app.contact.get_contact_from_view_page(0)
    cont_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert cont_from_view_page.homephone == cont_from_edit_page.homephone
    assert cont_from_view_page.mobilephone == cont_from_edit_page.mobilephone
    assert cont_from_view_page.workphone == cont_from_edit_page.workphone
    assert cont_from_view_page.secondaryphone == cont_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(add_new):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [add_new.homephone, add_new.mobilephone, add_new.workphone, add_new.secondaryphone]))))



def merge_email_like_on_home_page(add_new):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [add_new.email, add_new.email2, add_new.email3]))))