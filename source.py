"""I'm not proud of it, but it works. I foresee numerous cleanups and rewrites in the future."""
# TODO: Find an algorithm that results in a 2-connected graph.
# TODO: Improve readability.
# TODO: Make algorithm "map-size" agnostic; i.e. replace hard-coded values (e.g. "999") with ones that scale based on the inputs.

class Settlement:
	def __init__(self, y_coordinate, x_coordinate, name):  # Because changing the order the data is fed to the class is easier than changing the data itself.
		self.name = name
		self.x = x_coordinate
		self.y = 99 - y_coordinate  # There was some weirdness with how the data was obtained, resulting in the y-axis being flipped.

	def calc(self, settlement):
		if self == settlement:
			return 999
		else:
			return int(pow((pow((self.x - settlement.x), 2)+pow((self.y - settlement.y), 2)), 0.5))  # Geometric distance (a**2 + b**2 = c**2)


Sanctuary = Settlement(13, 7, "Sanctuary")
RedRocketTruckStop = Settlement(17, 11, "Red Rocket Truck Stop")
AbernathyFarm = Settlement(13, 17, "Abernathy Farm")
SunshineTidingsCoop = Settlement(8, 29, "Sunshine Tidings Co-op")
StarlightDriveIn = Settlement(30, 21, "Starlight Drive In")
TenpinesBluff = Settlement(36, 8, "Tenpines Bluff")
OutpostZimonja = Settlement(42, 2, "Outpost Zimonja")
GreyGarden = Settlement(25, 39, "GreyGarden")
Covenant = Settlement(43, 27, "Covenant")
TaffingtonBoathouse = Settlement(49, 26, "Taffington Boathouse")
GreentopNursery = Settlement(59, 17, "Greentop Nursery")
OberlandStation = Settlement(26, 49, "Oberland Station")
HangmansAlley = Settlement(37, 55, "Hangman's Alley")
BunkerHill = Settlement(55, 41, "Bunker Hill")
CountryCrossing = Settlement(64, 33, "Country Crossing")
FinchFarm = Settlement(71, 26, "Finch Farm")
TheSlog = Settlement(71, 15, "The Slog")
CoastalCottage = Settlement(78, 7, "Coastal Cottage")
BostonAirport = Settlement(69, 48, "Boston Airport")
NordhagenBeach = Settlement(75, 45, "Nordhagen Beach")
CroupManor = Settlement(87, 32, "Croup Manor")
KingsportLighthouse = Settlement(86, 20, "Kingsport Lighthouse")
EgretToursMarina = Settlement(33, 74, "Egret Tours Marina")
JamaicaPlain = Settlement(51, 75, "Jamaica Plain")
TheCastle = Settlement(68, 67, "The Castle")
SomervillePlace = Settlement(32, 86, "Somerville Place")
MurkwaterConstructionSite = Settlement(50, 89, "Murkwater Construction Site")
WarwickHomestead = Settlement(72, 79, "Warwick Homestead")
SpectacleIsland = Settlement(80, 74, "Spectacle Island")


settlements = [
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
]


connection_matrix = []
distance_matrix = []
neighbors = []
for x in range(len(settlements)):
	row1 = []
	row2 = []
	for y in range(len(settlements)):
		row1.append(0)
		row2.append(settlements[x].calc(settlements[y]))
	connection_matrix.append(row1)
	neighbors.append(row1)
	distance_matrix.append(row2)


def firstlink():
	xmin = 999
	ymin = 999
	shortest = 999
	for x in range(len(settlements)):
		for y in range(x+1, len(settlements)):
			if 0 < distance_matrix[x][y] < shortest or 0 < distance_matrix[y][x] < shortest:
				xmin = x
				ymin = y
				shortest = distance_matrix[x][y]
	connection_matrix[xmin][ymin] = 1
	connection_matrix[ymin][xmin] = 1


firstlink()

network = []
for x in range(len(connection_matrix)):
	for y in range(x+1, len(connection_matrix)):
		if connection_matrix[x][y] or connection_matrix[y][x] == 1:
			network.append(x)
			network.append(y)


def addlinks():
	candidates = []
	for x in network:
		for y in list(set(range(len(settlements)))-set(network)):
			if settlements[x].calc(settlements[y]) == min([settlements[x].calc(settlements[y]) for y in list(set(range(len(settlements)))-set(network))]):  # Surely there's a cleaner way to do this?
				candidates.append([x, y, settlements[x].calc(settlements[y])])
	for x in candidates:
		if x[2] == min([y[2] for y in candidates]):
			network.append(x[1])
			connection_matrix[x[0]][x[1]] = 1
			connection_matrix[x[1]][x[0]] = 1


for x in range(len(settlements)-2):
	addlinks()


for x in connection_matrix:  # The graph represented by an edge matrix. Columns/Rows follow the same order as the "settlements" list at the beginning of the script.
	print(x)

for x in range(len(settlements)):  # The graph represent by listing each node, followed all nodess connected to it.
	row = settlements[x].name
	row += ":"
	for y in range(len(connection_matrix[x])):
		if connection_matrix[x][y] == 1:
			row += "	"
			row += settlements[y].name
	print(row)
