import unittest
from selenium import webdriver
from tests import Base


class ChromeDriverBenchmarkTest(Base.Base):

    def getDriver(self):
        return webdriver.Chrome()


if __name__ == "__main__":
    unittest.main()
