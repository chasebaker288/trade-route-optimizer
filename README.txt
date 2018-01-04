# trade-route-optimizer
A graph theory experiment inspired by Fallout 4's settlement system.



𝑪𝑹𝑰𝑻𝑬𝑹𝑰𝑨:
• All settlements should form a single, connected graph. (DONE)
	(There are no penalties for having a resource pass through multiple settlements.)
• Route lengths should be minimized, both individually and cumulatively. (DONE)
	(Longer routes mean a higher risk of NPCs having trouble moving between locations.)
• Total number of edges should be minimized. (DONE)
	(See above)
• BONUS: The graph should be 2-connected. (?)*
	(Simple redundancy failsafe.)



𝑪𝑼𝑹𝑹𝑬𝑵𝑻 𝑴𝑶𝑫𝑬𝑳:
1. Find the two settlements closest to each other. This is the basis for the trade network.
2. Find whichever remaining settlement is closest to the network, then add it to the network.
3. Repeat step 2 until all settlements are within the network.



*(In retrospect, simply doubling up on the number of NPCs along each route would largely have the desired effect.)
