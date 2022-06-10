from abc import abstractmethod


class DriverManager:
    @abstractmethod
    def createDriver(self):
        pass

    @abstractmethod
    def getDriver(self):
        pass
