# TODO: Improve readability; Rework matrices into an class/object?
# TODO: Add arbitration for routes of equal length.


class Settlement:
	def __init__(self, name, x_coordinate, y_coordinate):  # Because changing the order the data is fed to the class is easier than changing the data itself.
		self.name = name
		self.x = x_coordinate
		self.y = y_coordinate

	def calc(self, settlement):
		if self == settlement:
			return MAP_DIMENSIONS[0]*MAP_DIMENSIONS[1]
		else:
			return int(pow((pow((self.x - settlement.x), 2)+pow((self.y - settlement.y), 2)), 0.5))  # Geometric distance (a**2 + b**2 = c**2)


def firstlink():
	"""Finds the two closest settlements"""
	xmin = MAP_DIMENSIONS[0]
	ymin = MAP_DIMENSIONS[1]
	shortest = xmin * ymin
	for i in range(len(SETTLEMENTS)):
		for j in range(i + 1, len(SETTLEMENTS)):
			if 0 < distance_matrix[i][j] < shortest or 0 < distance_matrix[j][i] < shortest:
				xmin = i
				ymin = j
				shortest = distance_matrix[i][j]
	connection_matrix[xmin][ymin] = 1
	connection_matrix[ymin][xmin] = 1
	trade_network.append(xmin)
	trade_network.append(ymin)


def addlinks():
	"""Rework trade network and the connection matrix as an object with this as a method?"""
	candidates = []
	for i in trade_network:
		for j in list(set(range(len(SETTLEMENTS))) - set(trade_network)):  # Clunky
			if distance_matrix[i][j] == min([distance_matrix[i][j] for j in list(set(range(len(SETTLEMENTS))) - set(trade_network))]):  # Surely there's a cleaner way to do this?
				candidates.append([i, j, distance_matrix[i][j]])
	for i in candidates:
		if i[2] == min([j[2] for j in candidates]):
			trade_network.append(i[1])
			connection_matrix[i[0]][i[1]] = 1
			connection_matrix[i[1]][i[0]] = 1


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

MAP_DIMENSIONS = (max([i.x for i in SETTLEMENTS]), max([j.y for j in SETTLEMENTS]))
trade_network = []  # Tracks members of network by their index in the SETTLEMENTS tuple
connection_matrix = []
distance_matrix = []
for i in range(len(SETTLEMENTS)):  # Builds connection and distance matrices
	row1 = []
	row2 = []
	for j in range(len(SETTLEMENTS)):
		row1.append(0)
		row2.append(SETTLEMENTS[i].calc(SETTLEMENTS[j]))
	connection_matrix.append(row1)
	distance_matrix.append(row2)


firstlink()
for i in range(len(SETTLEMENTS)-2):  # 2 less than the total number off settlements, as two have already been placed in the network.
	addlinks()

for i in connection_matrix:  # The graph, as represented by an edge matrix. Columns/Rows follow the same order as the SETTLEMENTS tuple at the beginning of the script.
	print(i)

for i in range(len(SETTLEMENTS)):  # The graph, as represented by listing each settlement followed by all settlements connected to it.
	row = SETTLEMENTS[i].name
	row += ":"
	for j in range(len(connection_matrix[i])):
		if connection_matrix[i][j] == 1:
			row += "	"
			row += SETTLEMENTS[j].name
	print(row)
