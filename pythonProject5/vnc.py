from playwright.sync_api import sync_playwright
from locators.TestLoc import Test_loc


class Login(Test_loc):
    def __init__(self,page):
        super().__init__(page)
        self.page = page
        self.loc = Test_loc(page)

    def login(self):
        self.page.goto("http://192.168.1.55:8080/")
        self.loc.username.fill("adminvp")
        self.loc.password.fill("admin_vp")
        self.loc.submit.click()

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        log = Login(page)
        log.login()