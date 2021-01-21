import re


def test_phones_on_home_page(app):
    cont_from_home_page = app.contact.get_contact_list()[0]
    cont_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert cont_from_edit_page.homephone == clear(cont_from_home_page.homephone)
    assert cont_from_edit_page.mobilephone == clear(cont_from_home_page.mobilephone)
    assert cont_from_edit_page.workphone == clear(cont_from_home_page.workphone)
    assert cont_from_edit_page.secondaryphone == clear(cont_from_home_page.secondaryphone)


def clear(s):
    return re.sub("[ ]", "", s)
