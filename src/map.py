import xml.dom.minidom
world1xml = xml.dom.minidom.parse("world1.xml")

class World(object):

    def __init__(self, attrs):
        self.size= map(int,attrs['size'].split())
        self.name = attrs['name']
        self.desc = attrs['desc']
        self.grid = [[None for _ in range(self.size[0])]for _ in range(self.size[1])]

    def appendRegion(self, regionattrs):
        loc = map(int,regionattrs['loc'].split())
        self.grid[loc[0]][loc[1]] = Region(self,regionattrs)

class Region(object):

    def __init__(self,parent,attrs):
        self.parent = parent
        self.loc = map(int,attrs['loc'].split())
        self.size= map(int,attrs['size'].split())
        self.name = attrs['name']
        self.desc = attrs['desc']
        self.grid = [[[None for _ in range(self.size[0])]for _ in range(self.size[1])]for _ in xrange(self.size[2])]

    def appendRoom(self, roomattrs):
        loc = map(int,roomattrs['loc'].split())
        self.grid[loc[0]][loc[1]][loc[2]] = Room(self,roomattrs)

    def getRoom(self, x,y,z):
        return self.grid[x][y][z]

class Room(object):
    contents = [None]
    directions = {'north':'0','south':'1','east':'2','west':'3','up':'4','down':'5'}
    def __init__(self, parent,attrs):
        self.parent = parent
        self.loc = map(int,attrs['loc'].split())

        self.name = attrs['name']
        self.desc = attrs['desc']
        self.exits = map(bool,map(int,attrs['exits'].split()))

    def canExit(self,exit):
        if (exit == "north") and self.exits[0]:
            return True

        if (exit == "south") and self.exits[1]:
            return True

        if (exit == "east")  and self.exits[2]:
            return True

        if (exit == "west")  and self.exits[3]:
            return True

        if (exit == "up")    and self.exits[4]:
            return True

        if (exit == "down")  and self.exits[5]:
            return True

        else:
            return False





