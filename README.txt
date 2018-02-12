Given a file with a list of addresses, it applies various approaches to find the best way to traverse the points. 
*Uses the Google Distance Matrix to calculate n^n distances for all points
*Currently only implements a naive solution but intended to play around with various travelling salesman approaches on real world data
*Google Distance Matrix currently times out for more than 5 points

TODO 
*Optimise calls to Google API for second half of list by pruning destinations list