import unittest
from selenium import webdriver
from tests import Base


class FirefoxDriverBenchmarkTest(Base.Base):

    def getDriver(self):
        return webdriver.Firefox()


if __name__ == "__main__":
    unittest.main()
