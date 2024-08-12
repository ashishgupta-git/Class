import tkinter as tk
import webbrowser
import time

# List of words to search sequentially
search_words = ["Ashish", "Python with Ashish","Python", "Programming", "Microsoft", "Waw", "Dhoni", "AshishGupta_ig", "Follow_Ashish", "MS Dhoni", "IPL", "Indian Premier League", "Mahi", "Mahi Maar Raha hai", "Bhaluu", "Aalu", "Ashish Gupta", "India Travel Thriller", "India Travel Thriller Instagram", "India travel Thriller Youtube", "ashishgupta_ig insta ID", "Gupta ji", "Akshay kumar", "Kartik Aaryan", "Cricket is love", "WWE", "Roman Raings", "Jhon Cena", "soo beautiful soo eligent", "Just looking like a waw", "Thriller Ashish"]              
current_index = 0  # Initialize the index to keep track of the current word


def search():
    global current_index

    # Get the current word from the list
    word = search_words[current_index]

    # Open Microsoft search with the current word
    url = f"https://www.bing.com/search?q={word}"
    webbrowser.open_new(url)

    # Move to the next word in the list
    current_index = (current_index + 1) % len(search_words)


def start_search():
    while True:
        search()
        time.sleep(8)  # Wait for 8 seconds between searches


# Create GUI
root = tk.Tk()
root.title("Sequential Search")

label = tk.Label(root, text="Click 'Start' to begin sequential searches on Microsoft.")
label.pack()

start_button = tk.Button(root, text="Start", command=start_search)
start_button.pack()

root.mainloop()

