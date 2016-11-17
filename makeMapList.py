# This is a tool to keep MapCompare current with changes made to the Citatsia Maplist.
# Ideally this would be done each time a comparison is made, but there's no way of knowing that both people in a
# given comparison have beaten all of the maps between them.

import fileinput


def map_list():

    maps_list = []
    full_list = []
    for line in fileinput.input():
        if line == "\n":
            fileinput.close()
            break
        full_list = full_list + line.replace("\n", " ").replace("\t", " ").replace(":", ",").split(" ")
    for entry in full_list:
        if entry.startswith("surf_"):
            maps_list.append(entry)

    maps_list.sort()
    print(maps_list)

map_list()
