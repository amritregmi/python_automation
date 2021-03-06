import os, sys
sys.path.insert(0, os.path.abspath(".."))
from Base import loggedInBaseTestCase

class EmptyEntryClassMerchantTestCase(loggedInBaseTestCase.LoggedInBaseTestCase):
    def test_emptyEntryClassMerchant(self):
        self._caseId = 150
        self._suiteId = 3
        self._user = "Admin"
        self._password = "Adminpass@1"
        driver = self.driver

        self.login()
        self.assertEqual(driver.current_url, "http://54.186.24.234/pages/dashboard")

        driver.find_element_by_xpath('//*[@id="top"]/div/div[2]/ul[1]/li[3]/a').click()
        driver.find_element_by_id('merchantadd').click()

        driver.find_element_by_id("MerchantName").clear()
        driver.find_element_by_id("MerchantName").send_keys("rameshkc")

        driver.find_element_by_id("MerchantBackendMerchantId").clear()
        driver.find_element_by_id("MerchantBackendMerchantId").send_keys("789055")

        driver.find_element_by_id("MerchantPin").clear()
        driver.find_element_by_id("MerchantPin").send_keys("de2")

        driver.find_element_by_id("MerchantFederalTaxId").clear()
        driver.find_element_by_id("MerchantFederalTaxId").send_keys("3342")

        driver.find_element_by_xpath('//*[@id="MerchantCreateForm"]/fieldset/div/div/div[3]/div/input').click()

        self.assertEqual(driver.current_url, "http://54.186.24.234/merchants/create")







