# mapComparison

A system for comparing two players' maptime printouts from Church of Citatsia surf servers.

----------------
|Run it Online!|
----------------

If you aren't interested in the code and just want to use this software, it can be run here:

<b> https://repl.it/EYKw/4 </b>

This link will be maintained to the best of my ability to keep it current with the sourcecode.

----------------
|compareMain.py|
----------------

This currently is tuned to work for the updated Noob and Skill servers. However, the fluctuating maplists have somewhat limited our ability to keep up with the changes. However, the Noob maplist should be 100% complete and accurate. Since nobody has 100% clear on the Skill mapset, we don't have a list for it and I am planning on implementing the ability to scrape mapnames off of "incomplete map" lists. This will allow me to combine my "completed maps" and "incomplete maps" lists to create the full Skill list without anyone beating all the maps. For the time being however, this software supports the full legacy Casual Surf and Skill Surf maplists.

How It Works:
Currently, this script takes the names of two players, and their maptime outputs. 
Once it has been fed the inputs, it gives comparison data on each map (syntax is hours:minutes:seconds, and seconds may be followed by a decimal).
It also gives a summary, which tells players how many maps each person has an advantage on, which maps each has beaten that the other has not, and which maps neither player has beaten.


----------------
|makeMapList.py|
----------------

<b>*This script is NOT needed to run compareMain.py*</b>

This script was used to generate the maps_list included in the program. This script is included so people can make their own maps lists for other servers, or to be used in updating this software to include more servers or different maps.
It takes a player's time data as input, this player should have beaten all the maps on the server for this to work as intended.