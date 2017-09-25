class ClosedList:
    """Generic Class that represents the closed list of a search problem.
       This list contains all the states which are already evaluated by the search algorithm
    """
       
    def add(self, state):
        raise NotImplementedError("Subclass must implement abstract method")

    def hasState(self, state):
        raise NotImplementedError("Subclass must implement abstract method")          


if __name__ == '__main__':
    closedList = ClosedList()
    print(closedList.__doc__)
