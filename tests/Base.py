import unittest
import time
from logging import basicConfig, getLogger, INFO


class Base(unittest.TestCase):

    def getDriver(self):
        raise Exception()

    def setUp(self):
        basicConfig(level=INFO)
        self.logger = getLogger(__name__)
        self.millis = [0] * 9
        self.limit = 100
        self.driver = self.getDriver()

    def tearDown(self):
        self.driver.quit()
        self.logger.info('get: {:.0f} millisec.'.format(self.millis[0] / self.limit))
        self.logger.info('findElementById: {:.0f} millisec.'.format(self.millis[1] / self.limit))
        self.logger.info('WebElement.clear: {:.0f} millisec.'.format(self.millis[2] / self.limit))
        self.logger.info('WebElement.sendKeys: {:.0f} millisec.'.format(self.millis[3] / self.limit))
        self.logger.info('findElementByXPath: {:.0f} millisec.'.format(self.millis[4] / self.limit))
        self.logger.info('WebElement.click: {:.0f} millisec.'.format(self.millis[5] / self.limit))
        self.logger.info('findElementByCSS: {:.0f} millisec.'.format(self.millis[6] / self.limit))
        self.logger.info('WebElement.click: {:.0f} millisec.'.format(self.millis[7] / self.limit))
        self.logger.info('getScreenshot: {:.0f} millisec.'.format(self.millis[8] / self.limit))

    def testSample(self):

        for index in range(self.limit):

            self.logger.info(str(index))

            start_time = time.time()
            self.driver.get('http://example.selenium.jp/reserveApp/')
            end_time = time.time()
            self.millis[0] += (end_time - start_time) * 1000

            start_time = time.time()
            reserve_year = self.driver.find_element_by_id('reserve_year')
            end_time = time.time()
            self.millis[1] += (end_time - start_time) * 1000

            start_time = time.time()
            reserve_year.clear()
            end_time = time.time()
            self.millis[2] += (end_time - start_time) * 1000

            start_time = time.time()
            reserve_year.send_keys('2014')
            end_time = time.time()
            self.millis[3] += (end_time - start_time) * 1000

            """
            start_time = time.time()
            breakfast_off = self.driver.find_element_by_xpath('//input[@id=breakfast_off]')
            end_time = time.time()
            self.millis[4] += (end_time - start_time) * 1000

            start_time = time.time()
            breakfast_off.click()
            end_time = time.time()
            self.millis[5] += (end_time - start_time) * 1000
            """

            start_time = time.time()
            plan_b = self.driver.find_element_by_css_selector ('#plan_b')
            end_time = time.time()
            self.millis[6] += (end_time - start_time) * 1000

            start_time = time.time()
            plan_b.click()
            end_time = time.time()
            self.millis[7] += (end_time - start_time) * 1000

            start_time = time.time()
            self.driver.get_screenshot_as_base64()
            end_time = time.time()
            self.millis[8] += (end_time - start_time) * 1000
