import allure
from hamcrest import assert_that, is_not, empty, greater_than, equal_to

from page.bustier_gift_cards_page import BuGiftCardsPage


@allure.feature("Подарочные карты")
@allure.story("Выбор номинала подарочной карты")
def test_gift_cards_par(browser, base_url):
    with allure.step(f"Открыть страницу"):
        bu_gift_card_page = BuGiftCardsPage(browser)
        bu_gift_card_page.navigate_to(base_url)

    with allure.step("Пролистать страницу до 'Номинал карты'"):
        bu_gift_card_page.scroll_to_gift_cards_par()

    with allure.step("Прокликать все кнопки с номиналом карт"):
        par_buttons = bu_gift_card_page.get_all_par_buttons()
        assert_that(par_buttons, is_not(empty()), "Не найдены кнопки с номиналом карт")
        for current_par_button in par_buttons:
            with allure.step(f"Кнопка {current_par_button.text}"):
                current_par_button.click()
                active_par_buttons = bu_gift_card_page.get_all_active_par_buttons()
                exp_number_of_active_buttons_after_click = 1
                assert_that(len(active_par_buttons), equal_to(exp_number_of_active_buttons_after_click),
                            f"Количество активированных кнопок не равно {exp_number_of_active_buttons_after_click}")
                assert_that(active_par_buttons[0], equal_to(current_par_button),
                            "Выбранная кнопка не активирована")
                par_card_value_from_input = bu_gift_card_page.get_value_from_gift_card_par_input()
                assert_that(current_par_button.text, equal_to(par_card_value_from_input),
                            "Выбранный номинал не отображается в поле 'Введите'")
