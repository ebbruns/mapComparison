# This is a tool to keep MapCompare current with changes made to the Citatsia Maplist.
# Ideally this would be done each time a comparison is made, but there's no way of knowing that both people in a
# given comparison have beaten all of the maps between them.


def mapList():
    isDiscord = input("Do you want to copy times from discord or the server?")
    print("Please enter the times of someone who has beaten all the maps to generate a maplist.")
    if isDiscord.lower() == "discord":
        full_times = input()
    else:
        sentinel = ''  # ends when this string is seen
        for line in iter(input, sentinel):
            full_times = '\n'.join(iter(input, sentinel))
    full_list = full_times.replace("\n", " ").split(" ")
    maps_list = list()

    print(full_list)

    for entry in full_list:
        if entry.startswith("surf_"):
            maps_list.append(entry)

    print(maps_list)

mapList()

