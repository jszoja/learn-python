
class InvalidPathNodeException(Exception):
    pass


class PathNodeInterface:

    def __init__(self) -> None:
        self.pathNode = PathNode(self)

    def getDistance(self, target):
        pass

    def getNeighbours(self, target):
        pass

    def markChecked(self):
        pass


class PathNode:

    def __init__(self, el) -> None:
        # self.globalGoal = el.getDistance(target)
        self.el = el
        self.reset()

    def reset(self):
        self.parent = None
        self.localGoal = 0
        self.globalGoal = 0
        self.checked = False

    def __str__(self) -> str:
        return self.el.__str__(), "-", self.globalGoal


class PathFinder:
    DEBUG = 0

    def __init__(self, start, end):
        if not isinstance(start, PathNodeInterface):
            raise InvalidPathNodeException(
                "The start argument has to be an instance of PathNode")
        if not isinstance(end, PathNodeInterface):
            raise InvalidPathNodeException(
                "The end argument has to be an instance of PathNode")
        self.start = start
        self.end = end
        map(lambda x: x.pathNode.reset(), [self.start, self.end])
        self.end.pathNode.checked = True
        self.bestGlobalGoal = 0.
        self.nodesToCheck = [start]
        self.bestGoal = 0
        #print(f"new path")

    def find(self):
        round = 0
        while len(self.nodesToCheck) > 0 and round < 10000:
            node = self.nodesToCheck.pop(0)
            if node.pathNode.checked:
                continue
            round += 1
            if PathFinder.DEBUG:
                print(f"----- Round {round} ------")
                print(node)
            neighbours = node.getNeighbours()
            # print(f"found ", len(neighbours), " neighbours")

            # if node not in [self.start, self.end]:
            #    node.markChecked()

            for nb in neighbours:
                # if node not in [self.start, self.end]:
                #    nb.markChecked()
                nbNode = nb.pathNode
                if nbNode.globalGoal == 0:
                    nbNode.globalGoal = nb.getDistance(self.end)
                newLocalGoal = node.pathNode.localGoal+1
                if nbNode.localGoal == 0 or newLocalGoal < nbNode.localGoal:
                    nbNode.parent = node
                    nbNode.localGoal = newLocalGoal
                    nbNode.globalGoal = nbNode.localGoal + \
                        nb.getDistance(self.end)
                    # if nb == self.end:
                    #    if nbNode.globalGoal < self.bestGoal or self.bestGoal == 0:
                    #    self.bestGoal = nbNode.globalGoal
                if PathFinder.DEBUG:
                    print(nb, ", ", end='')
                if not nbNode.checked:
                    self.nodesToCheck.append(nb)
                if nb == self.end:
                    break

            node.pathNode.checked = True
            if PathFinder.DEBUG:
                print("\n\n")
            self.nodesToCheck.sort(
                key=lambda x: x.pathNode.globalGoal, reverse=False)

        n = self.end
        limit = 1000
        route = []
        while n != self.start or limit == 0:
            n = n.pathNode.parent
            if n == None:
                break
            if n != self.start:
                route.append(n)
            limit = limit - 1
        return route
