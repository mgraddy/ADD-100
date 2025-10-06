def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]

    def replace(user_index, user_artist): # Function to replace an element in top_artists given an index and an artist name
        try: # int(user_index) can lead to ValueError, top_artists[index] can lead to IndexError
            index = int(user_index)
            artist = user_artist.title()
            top_artists[index] = artist
        except (ValueError, IndexError): # General except block to catch multiple exceptions
            print("An input error occurred.")

    print(top_artists) # Print initial list
    
    # Ask user for index and artist name
    user_index = input("Enter the index of the artist you'd like to replace: ")
    user_artist = input("Enter the name of the artist you want to replace with: ")
    
    replace(user_index,user_artist) # Call replace function
    print(top_artists) # Print modified list
    


main()