import unittest
from selenium import webdriver
from tests import Base


class GhostDriverBenchmarkTest(Base.Base):

    def getDriver(self):
        return webdriver.PhantomJS()


if __name__ == "__main__":
    unittest.main()
