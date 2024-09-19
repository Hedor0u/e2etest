from playwright.sync_api import Page
import config
import random

class IndexPage:
  
  def open_index_page(self, page: Page) -> None:
    page.goto(config.url.DOMAIN)
    
  def press_login_button(self, page: Page):
    page.get_by_text("Login").click()
    
  def fill_login_data(self, page: Page):
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    
  def press_add_to_cart(self, page: Page):
    all_items = page.get_by_text("Add to cart").all()
    if page.get_by_text("Remove").all() != 0:
      for item in all_items:
        if item.is_visible() and item.inner_text() == "Add to cart":
          if random.choice([True, False]):
            item.click()
      
  def press_open_cart(self, page:Page):
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    
  def press_checkout(self, page:Page):
    page.locator("[data-test=\"checkout\"]").click()
    
  def fill_user_shipping_data(self, page:Page):
    UFirstName = "John"
    ULastName = "Abrams"
    ZipCode = "100500"
    page.get_by_placeholder("First Name").fill(UFirstName)
    page.get_by_placeholder("Last Name").fill(ULastName)
    page.get_by_placeholder("Zip/Postal Code").fill(ZipCode)
    
  def press_submit_cart(self, page:Page):
    page.get_by_text("Continue").click()
    
  def complete_order(self, page:Page):
    page.get_by_text("Finish").click()
    
  def check_order_completion(self, page:Page):
    return page.locator("[data-test=\"complete-header\"]").inner_text()