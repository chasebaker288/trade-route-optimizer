class Settlement:
    def __init__(self, name, x_coordinate, y_coordinate):  # Because changing the order the data is fed to the class is easier than changing the data itself.
        self.name = name
        self.x = x_coordinate
        self.y = y_coordinate

    def calc(self, settlement):
        if self == settlement:
            return max([self.x, self.y])**2
        else:
            return int(pow((pow((self.x - settlement.x), 2)+pow((self.y - settlement.y), 2)), 0.5))  # Geometric distance (a**2 + b**2 = c**2)


class Network:
    def __init__(self, list_of_settlements=()):  # TODO: Check for list/tuple implementation issues. Shouldn't be a problem, therefore it might be.
        self.everyone = list_of_settlements
        self.size = len(list_of_settlements)
        self.map_size = [max([i.x for i in list_of_settlements]), max([i.y for i in list_of_settlements])]
        self.dists = []
        self.links = []
        self.members = []
        for i in range(len(list_of_settlements)):
            link_row = []
            dist_row = []
            for j in range(len(list_of_settlements)):
                link_row.append(0)
                dist_row.append(list_of_settlements[i].calc(list_of_settlements[j]))
            self.links.append(link_row)
            self.dists.append(dist_row)

    def begin(self):
        x_index = self.map_size[0]
        y_index = self.map_size[1]
        shortest = x_index*y_index
        for i in range(self.size):
            for j in range(i+1, self.size):
                if 0 < self.dists[i][j] < shortest or 0 < self.dists[j][i] < shortest:
                    x_index = i
                    y_index = j
                    shortest = self.dists[i][j]
                else:
                    pass
        self.links[x_index][y_index] = 1
        self.links[y_index][x_index] = 1
        self.members.append(x_index)
        self.members.append(y_index)

    def build(self):
        while set(range(self.size))-set(self.members) != set(self.members)-set(range(self.size)):  # Probably excessive, but while loops make me paranoid
            candidates = []
            for i in self.members:
                for j in set(range(self.size))-set(self.members):  # Surely there's a cleaner way to narrow the list?
                    if self.dists[i][j] == min([self.dists[i][j] for j in set(range(self.size))-set(self.members)]):
                        candidates.append([i, j, self.dists[i][j]])
                    else:
                        pass
            for i in candidates:
                if i[2] == min([j[2] for j in candidates]):
                    self.members.append(i[1])
                    self.links[i[0]][i[1]] = 1
                    self.links[i[1]][i[0]] = 1
                    break  # This way, if there's a tie, it treats the first one it encounters as the shorter one.
                else:
                    pass

    def print(self, mode="distances"):
        if mode.lower() == "links":
            for i in list(set(self.members)):
                print(self.links[i])
        elif mode.lower() == "names":
            for i in range(self.size):
                row = self.everyone[i].name + ":"
                for j in range(self.size):
                    if self.links[i][j] == 1:
                        row += "	" + self.everyone[j].name
                    else:
                        pass
                print(row)
        else:
            for i in range(self.size):
                row = []
                for j in range(self.size):
                    row.append(self.dists[i][j]*self.links[i][j])
                print(row)


Sanctuary = Settlement("Sanctuary", 134.5, 925.5)
RedRocketTruckStop = Settlement("Red Rocket Truck Stop", 176, 879)
AbernathyFarm = Settlement("Abernathy Farm", 131, 822)
SunshineTidingsCoop = Settlement("Sunshine Tidings Co-op", 82, 700)
StarlightDriveIn = Settlement("Starlight Drive In", 302, 777)
TenpinesBluff = Settlement("Tenpines Bluff", 361.5, 915.5)
OutpostZimonja = Settlement("Outpost Zimonja", 423.5, 973.5)
GreyGarden = Settlement("GreyGarden", 254, 600)
Covenant = Settlement("Covenant", 438, 723.5)
TaffingtonBoathouse = Settlement("Taffington Boathouse", 493, 728.5)
GreentopNursery = Settlement("Greentop Nursery", 595.5, 819)
OberlandStation = Settlement("Oberland Station", 264, 491)
HangmansAlley = Settlement("Hangman's Alley", 379, 433.5)
BunkerHill = Settlement("Bunker Hill", 549.5, 580.5)
CountryCrossing = Settlement("Country Crossing", 653.75, 640.25)
FinchFarm = Settlement("Finch Farm", 711.25, 726.25)
TheSlog = Settlement("The Slog", 715.5, 840)
CoastalCottage = Settlement("Coastal Cottage", 780, 923)
BostonAirport = Settlement("Boston Airport", 689.5, 503.5)
NordhagenBeach = Settlement("Nordhagen Beach", 755.75, 531.75)
CroupManor = Settlement("Croup Manor", 874, 681.5)
KingsportLighthouse = Settlement("Kingsport Lighthouse", 868, 789.5)
EgretToursMarina = Settlement("Egret Tours Marina", 336, 235.5)
JamaicaPlain = Settlement("Jamaica Plain", 519, 231)
TheCastle = Settlement("The Castle", 648.5, 307.5)
SomervillePlace = Settlement("Somerville Place", 325.5, 117.5)
MurkwaterConstructionSite = Settlement("Murkwater Construction Site", 500.5, 89)
WarwickHomestead = Settlement("Warwick Homestead", 722.75, 185.75)
SpectacleIsland = Settlement("Spectacle Island", 801, 241.5)


SETTLEMENTS = (
    AbernathyFarm,
    BostonAirport,
    BunkerHill,
    CoastalCottage,
    CountryCrossing,
    Covenant,
    CroupManor,
    EgretToursMarina,
    FinchFarm,
    GreentopNursery,
    GreyGarden,
    HangmansAlley,
    KingsportLighthouse,
    JamaicaPlain,
    MurkwaterConstructionSite,
    NordhagenBeach,
    OberlandStation,
    OutpostZimonja,
    RedRocketTruckStop,
    Sanctuary,
    SomervillePlace,
    SpectacleIsland,
    StarlightDriveIn,
    SunshineTidingsCoop,
    TaffingtonBoathouse,
    TenpinesBluff,
    TheCastle,
    TheSlog,
    WarwickHomestead
)


trade_network = Network(SETTLEMENTS)
trade_network.begin()
trade_network.build()

trade_network.print("links")  # Print network as a connection matrix.
trade_network.print("names")  # Print network as each settlement, followed by all settlements linked to it.
trade_network.print("dists")  # Print network as a connection matrix, but with distances instead of 1's.
