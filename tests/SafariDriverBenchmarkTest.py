import unittest
from selenium import webdriver
from tests import Base


class SafariDriverBenchmarkTest(Base.Base):

    def getDriver(self):
        return webdriver.Safari()


if __name__ == "__main__":
    unittest.main()
