import unittest
from selenium import webdriver
from tests import Base


class WebKitGTKDriverBenchmarkTest(Base.Base):

    def getDriver(self):
        return webdriver.WebKitGTK()


if __name__ == "__main__":
    unittest.main()
