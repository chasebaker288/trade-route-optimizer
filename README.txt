# trade-route-optimizer
A graph theory experiment inspired by Fallout 4's settlement system.



𝑪𝑹𝑰𝑻𝑬𝑹𝑰𝑨:
• All settlements should form a single, connected graph. (DONE)
	(There are no penalties for having a resource pass through multiple settlements.)
• Route lengths should be minimized, both individually and cumulatively. (DONE)
• Total number of edges should be minimized. (DONE)
	(Longer routes mean a higher risk of NPCs having trouble moving between locations.)



𝑪𝑼𝑹𝑹𝑬𝑵𝑻 𝑴𝑶𝑫𝑬𝑳:
1. Find the two settlements closest to each other. This is the basis for the trade network.
2. Find whichever remaining settlement is closest to the network, then add it to the network.
3. Repeat step 2 until all settlements are within the network.



𝑨𝑭𝑻𝑬𝑹𝑻𝑯𝑶𝑼𝑮𝑯𝑻𝑺:
1. The algorithm orignally resulted in 3 cycles, rather than a simple tree. This was fixed by using more detailed data, though the issue will show up again if two or more locations are equidistant from the closest settlement in the network.
