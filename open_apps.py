import os

# Function to open Microsoft Word
def open_word():
    # Define the path to the Word shortcut or executable
    word_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"
    
    # Check if the file exists
    if os.path.exists(word_path):
        os.startfile(word_path)
        print("Microsoft Word has been opened.")
    else:
        print(f"File not found: {word_path}")

# Main function
def main():
    # Prompt the user for input
    user_input = input("Do you want to open Microsoft Word? (yes/no): ").strip().lower()
    
    # Process the user input
    if user_input == "yes":
        open_word()
    elif user_input == "no":
        print("Okay, Microsoft Word will not be opened.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Entry point of the script
if __name__ == "__main__":
    main()
