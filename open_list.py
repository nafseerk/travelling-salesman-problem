class OpenList:
    """Generic Class that represents the open list of a search problem.
       This list contains all the states that can be considered next by the search algorithm
    """
    def add(self, state):
        raise NotImplementedError("Subclass must implement abstract method")

    def getItem(self):
        raise NotImplementedError("Subclass must implement abstract method")          


if __name__ == '__main__':
    openList = OpenList()
    print(openList.__doc__)
