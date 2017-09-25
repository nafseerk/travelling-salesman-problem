
class ClosedList:
    
    def add(self, state):
        raise NotImplementedError("Subclass must implement abstract method")

    def hasState(self, state):
        raise NotImplementedError("Subclass must implement abstract method")          


if __name__ == '__main__':
    openList = ClosedList()
    #openList.hasState()
