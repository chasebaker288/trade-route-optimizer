# trade-route-optimizer
A graph theory experiment inspired by Fallout 4's settlement system.



𝑪𝑹𝑰𝑻𝑬𝑹𝑰𝑨:
• All settlements should form a single, connected graph.
	(The game has no penalties for having a resource pass through multiple settlements.)
• Route lengths should be minimized, both individually and cumulatively.
• Total number of edges should be minimized.
	(Longer routes mean a higher risk of NPCs having trouble moving between locations.)



𝑪𝑼𝑹𝑹𝑬𝑵𝑻 𝑴𝑶𝑫𝑬𝑳:
1. Find the two settlements closest to each other. This is the basis for the trade network.
2. Find whichever remaining settlement is closest to the network.
	(Proximity is determined using whichever member of the network is closest to the settlement in question)
3. Link that settlement to the aforementioned closest network member, adding the settlement to the network.
4. Repeat steps 2 and 3 until all settlements are in the network.



𝑨𝑭𝑻𝑬𝑹𝑻𝑯𝑶𝑼𝑮𝑯𝑻𝑺:
1. The algorithm orignally resulted in 3 cycles, rather than a simple tree. This was fixed by using more detailed data, though the issue will show up again if two or more locations are equidistant from the closest settlement in the network.
