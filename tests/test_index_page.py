import pytest
import pages
#import time

class TestFooter:

    def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
        pages.index_page.open_index_page(page)
        pages.index_page.fill_login_data(page)
        pages.index_page.press_login_button(page)
        pages.index_page.press_add_to_cart(page)
        pages.index_page.press_open_cart(page)
        pages.index_page.press_checkout(page)
        pages.index_page.fill_user_shipping_data(page)
        pages.index_page.press_submit_cart(page)
        pages.index_page.complete_order(page)
        result = pages.index_page.check_order_completion(page)
        assert result == 'Thank you for your order!', "Order wasn't placed"
        if result == 'Thank you for your order!':
            print('Test complete, order is placed!')
        #time.sleep(5)