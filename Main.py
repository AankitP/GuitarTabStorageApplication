from Tab import GuitarTab
import json
import os
import subprocess

# this is to load the JSON File and fill the songDict
def onStart(songDict):

    # Load the JSON file
    with open('Tabs.json', 'r') as file:
        tabs_data = json.load(file)

    # Go through JSON file and create the song dictionary
    for song_key, song_details in tabs_data.items():
        # Ensure song_key is treated as a string
        song_key = str(song_key)

        # Create new GuitarTab object
        GT = GuitarTab()
        GT.setTitle(song_details.get('Title', ''))
        GT.setArtist(song_details.get('Artist', ''))
        GT.setLocation(song_details.get('Location', ''))
        songDict[len(songDict) + 1] = GT

    return songDict

# Iterate over songs and print
def print_tabs_list(song_dict):

    print('\033c', end='')

    for index, tab in song_dict.items():
        print(f"{index}: {tab.getTitle()}")
        print(f"\t{tab.getArtist()}\n")

# this is the options menu
def options_menu():

    print("1. View All Tabs")
    print("2. Select Tab")
    print("3. Add Tab")
    print("4. Delete Tab")
    print("0. Exit\n")

    try:
        selection = int(input())
        return selection
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

# this is to show the tab that the user wants to see
def case2(song_dict):
    print('\033c', end='')
    print_tabs_list(song_dict)

    try:
        song_index = int(input("Select The Song Index that you want: "))
        print(f"{song_dict[song_index].getTitle()}")

        location = song_dict[song_index].getLocation()

        if os.path.exists(location):
            subprocess.run(['open', location])  # Open the file in the default web browser
        else:
            print("File not found.")
        
    except (ValueError, KeyError):
        print("Invalid input or index does not exist.")

# This Creates a new Tab object and adds it to the song dictionary
def case3(song_dict):
    print('\033c', end='')
    title, artist, location = input("Title of the song: "), input("Who wrote the song: "), input("Where is it located on your drive: ")
    new_tab = GuitarTab()
    new_tab.setTitle(title)
    new_tab.setArtist(artist)
    new_tab.setLocation(location)
    song_dict[len(song_dict) + 1] = new_tab
    return song_dict

# Delete Tab
def case4(song_dict):
    print_tabs_list(song_dict)
    try:
        index_to_delete = int(input("Enter the index of the tab you want to delete: "))
        if index_to_delete in song_dict:
            del song_dict[index_to_delete]
            print(f"Tab at index {index_to_delete} deleted successfully.")
        else:
            print("Invalid index. Tab not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")

    return song_dict

# this stores the song dictionary to a
def save_tabs_to_json(song_dict):
    print("Saving Tabs to JSON...")
    serialized_tabs = {index: tab.to_dict() for index, tab in song_dict.items()}
    
    with open('Tabs.json', 'w') as json_file:
        json.dump(serialized_tabs, json_file, indent=2)
    
    print("Tabs saved successfully.")

# Main function
def main():
    # initialize song dictionary
    song_dict = {}
    # used to exit the program
    run_while = True
    # fill song_dict with the objects from the json file
    song_dict = onStart(song_dict)

    while run_while:
        selection = options_menu()

        if selection is not None:
            if selection == 1:
                print_tabs_list(song_dict)
            elif selection == 2:
                case2(song_dict)
            elif selection == 3:
                song_dict = case3(song_dict)
            elif selection == 4:
                song_dict = case4(song_dict)
            elif selection == 0:
                save_tabs_to_json(song_dict)
                run_while = False
            else:
                print("Invalid selection. Please try again.")

        print("\n")

if __name__ == "__main__":
    main()