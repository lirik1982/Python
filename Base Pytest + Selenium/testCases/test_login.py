from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApllicationURL()
    useremail = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("*****************Test 001****************")
        self.logger.info("***********Test homepage Title***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
            self.logger.info("***** Homepage Title test PASSED ********")
            assert True
        else:
            self.logger.error("***** Homepage Title test FAILED ********")
            assert False

    def test_login(self, setup):
        self.logger.info("***** Verify logging test *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("***** Login test is PASSED *************")
            assert True
        else:
            self.logger.error("***** Login test is FAILED ************")
            assert False
