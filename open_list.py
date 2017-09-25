
class OpenList:
    
    def add(self, state):
        raise NotImplementedError("Subclass must implement abstract method")

    def getItem(self):
        raise NotImplementedError("Subclass must implement abstract method")          


if __name__ == '__main__':
    openList = OpenList()
    openList.getItem()
