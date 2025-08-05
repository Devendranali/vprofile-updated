class Test_loc:
    def __init__(self,page):
        self.page =page
        self.username = page.locator('//*[@name="username"]')
        self.password = page.locator('//*[@name="password"]')
        self.submit = page.locator('//*[@class="wrap-login100-form-btn"]')
        self.forgotpassword = page.locator('//*[@class="text-right p-t-8 p-b-31"]')