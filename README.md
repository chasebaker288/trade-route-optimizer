# trade-route-optimizer
A graph theory experiment inspired by Fallout 4's settlement system.



𝑪𝑹𝑰𝑻𝑬𝑹𝑰𝑨:
• All settlements should form a connected graph. (DONE)
	(Walks of any length are viable; there are no penalties for having a resource pass through multiple settlements.)
• Route lengths should be minimized, both individually and cumulatively. (DONE)
	(Since NPCs emulate physically travel between locations, longer routes mean a higher risk of NPCs encountering trouble.)
• Total number of edges should be minimized. (DONE)
	(See above)
• BONUS: The graph should be 2-connected. (?)*
	(Adding a layer of redundancy, such that if any one NPC encounters trouble, the network remains intact.)



𝑪𝑼𝑹𝑹𝑬𝑵𝑻 𝑴𝑶𝑫𝑬𝑳:
	1. Find the two settlements closest to each other. This is the basis for the trade network.
	2. Find whichever remaining settlement is closest to the network, then add it to the network.
	3. Repeat until all settlements are within the network.



*(In retrospect, simply doubling up on the number of NPCs along each route would largely have the desired effect.)
