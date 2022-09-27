from page.base_page import BasePage
from selenium.webdriver.common.by import By


class BuGiftCardsLocators:
    LOCATOR_GIFT_CARDS_PAR_CONTAINER = (By.CSS_SELECTOR, "div.par")
    LOCATOR_GIFT_CARD_PAR_BUTTON = (By.CSS_SELECTOR, "button.par-options__button")
    LOCATOR_GIFT_CARD_PAR_BUTTON_ACTIVE = (By.CSS_SELECTOR, "button.par-options__button--active")
    LOCATOR_GIFT_CARD_PAR_INPUT = (By.CSS_SELECTOR, ".par-input-block #range-value-input")


class BuGiftCardsPage(BasePage):
    def scroll_to_gift_cards_par(self, timeout=10):
        return self.scroll_to_element(BuGiftCardsLocators.LOCATOR_GIFT_CARDS_PAR_CONTAINER, timeout)

    def get_all_par_buttons(self, timeout=10):
        return self.find_elements(BuGiftCardsLocators.LOCATOR_GIFT_CARD_PAR_BUTTON, timeout)

    def get_all_active_par_buttons(self, timeout=10):
        return self.find_elements(BuGiftCardsLocators.LOCATOR_GIFT_CARD_PAR_BUTTON_ACTIVE, timeout)

    def get_value_from_gift_card_par_input(self, timeout=10):
        return self.find_element(BuGiftCardsLocators.LOCATOR_GIFT_CARD_PAR_INPUT, timeout).get_attribute("value")
