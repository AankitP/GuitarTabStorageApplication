from Tab import GuitarTab
import json

# Load the JSON file
with open('Tabs.json', 'r') as file:
    tabs_data = json.load(file)

# Access the Tabs object
tabs_object = tabs_data.get('Tabs', {})

# Iterate over songs
for song_key, song_details in tabs_object.items():
    print(song_key)
    print(song_details.get('Title', ''))
    # Access other details like artist and location if needed
    print(song_details.get('Artist', ''))
    print(song_details.get('Location', ''))

def Options():
    print("1. View All Tabs")
    print("2. Select Tab")
    print("3. Repeat Options")
    print("0. Exit")

    selection = int(input())

    return selection

# Thesae are the cases that the user selects
def case1(tabList):
    print('\033c', end='')
    for key in tabList:
        print(f"Song: {key}")

def case2(tabList):
    print('\033c', end='')
    print(tabList)

def case3():
    print('\033c', end='')
    return 1

# this is a switch case


def main():
    runWhile = True
    while(runWhile):
        selection = Options()
        if selection == 1:
            case1(tabList)
        elif selection == 2:
            case2(tabList)
        elif selection == 3:
            case3()
        else:
            runWhile = False

        print("\n\n")

main()