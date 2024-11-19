from apps.pages.search.search_functions import set_input, check_result
from apps.selectors.google.search_page_selectors import GoogleSearchPageSelectors
from confest import open_browser


def test_search(open_browser):
    set_input(GoogleSearchPageSelectors.INPUT, "yashaka/selene")
    check_result(GoogleSearchPageSelectors.SEARCH_RESULT,
                 "yashaka/selene: User-oriented Web UI browser tests in Python")


def test_search_empty(open_browser):
    input_value = "ysagdfag!%$#!^$@орвыафпииывфа7362"
    set_input(GoogleSearchPageSelectors.INPUT, input_value)
    check_result(GoogleSearchPageSelectors.SEARCH_EMPTY,
                 f"Your search - {input_value} - did not match any documents.")
