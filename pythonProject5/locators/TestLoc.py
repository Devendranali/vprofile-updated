class Test_loc:
    __test__ = False  # 👈 this tells pytest not to treat it as a test class

    def __init__(self, page):
        self.page = page
        self.username = page.locator('//*[@name="username"]')
        self.password = page.locator('//*[@name="password"]')
        self.submit = page.locator('//*[@class="wrap-login100-form-btn"]')
        self.forgotpassword = page.locator('//*[@class="text-right p-t-8 p-b-31"]')
