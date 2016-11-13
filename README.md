# mapComparison

A system for comparing player's maptimes printouts from Church of Citatsia surf servers.

----------------
|compareMain.py|
----------------

This currently is tuned to work for Noob Surf, but changes might be made to add Casual Surf.
Currently, this script takes the names of two players, and their maptime outputs. 
Once it has been fed the inputs, it gives comparison data on each map (syntax is hours:minutes:seconds, and seconds may be followed by a decimal).
It also gives a summary, which tells players how many maps each person has an advantage on, which maps each has beaten that the other has not, and which maps neither player has beaten.


----------------
|makeMapList.py|
----------------

*This script is NOT needed to run compareMain.py*
This script was used to generate the maps_list included in the program. This script is included so people can make their own maps lists for other servers, or to be used in updating this software to include more servers or different maps.
It takes a player's time data as input, this player should have beaten all the maps on the server for this to work as intended.
