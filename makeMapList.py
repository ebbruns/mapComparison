# This is a tool to keep MapCompare current with changes made to the Citatsia Maplist.
# Ideally this would be done each time a comparison is made, but there's no way of knowing that both people in a
# given comparison have beaten all of the maps between them.


def mapList():

    full_times = input("Please enter the times of someone who has beaten all the maps to generate a maplist.")
    full_list = full_times.split(" ")
    maps_list = list()

    print(full_list)

    for entry in full_list:
        if entry.startswith("surf_"):
            maps_list.append(entry)

    print(maps_list)

mapList()

