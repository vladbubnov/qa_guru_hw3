from selene import browser, be, have


def set_input(element, value):
    browser.element(element).should(be.blank).type(value).press_enter()


def check_result(element, value):
    browser.element(element).should(have.text(value))
