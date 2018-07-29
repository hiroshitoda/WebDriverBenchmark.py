import unittest
from selenium import webdriver
from tests import Base


class IEDriverBenchmarkTest(Base.Base):

    def getDriver(self):
        return webdriver.Ie()


if __name__ == "__main__":
    unittest.main()
