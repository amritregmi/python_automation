import os, sys
sys.path.insert(0, os.path.abspath(".."))
from Base import loggedInBaseTestCase

class createCustomerCheckingTypeTestCase(loggedInBaseTestCase.LoggedInBaseTestCase):

	def test_createCustomerCheckingType(self):
		self._caseId = 1447
		self._suiteId = 33
		self._user = "rumbu"
		self._password = "Test@123"

		driver = self.driver
		self.login()

		self.assertEqual(driver.current_url,"http://54.186.24.234/pages/dashboard")
		driver.find_element_by_xpath("//html/body/div[1]/header/div/div[2]/ul[1]/li[4]/a").click()
		driver.find_element_by_xpath("//html/body/div[1]/header/div/div[2]/ul[1]/li[4]/ul/li[2]/a").click()


		driver.find_element_by_id("CustomerCustomerName").clear()
		driver.find_element_by_id("CustomerCustomerName").send_keys("AmritRegmi")
		driver.find_element_by_id("CustomerRoutingNumber").clear()
		driver.find_element_by_id("CustomerRoutingNumber").send_keys("123456789")
		driver.find_element_by_id("CustomerAccountNumber").clear()
		driver.find_element_by_id("CustomerAccountNumber").send_keys("amrit123")
		driver.find_element_by_xpath("//input[@value='Create']").click()
		#self.assertEqual(driver.current_url,"http://54.186.24.234/customers/create")
		bodyText = self.driver.find_element_by_tag_name('body').text
		self.assertTrue("View Customers" in bodyText)



