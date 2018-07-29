import unittest
from selenium import webdriver
from tests import Base


class EdgeDriverBenchmarkTest(Base.Base):

    def getDriver(self):
        return webdriver.Edge()


if __name__ == "__main__":
    unittest.main()
