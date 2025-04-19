# Function to count characters in the text
def count_chars(text):
    dictionary = {}
    words = text.lower()
    for char in words:
        if char in dictionary: 
            dictionary[char] += 1 
        else:
            dictionary[char] = 1
    return dictionary

# Sorting function: Extract the "count" value from each dictionary
def sort_characters(dictionary):
    # Build list of dicts
    list_of_dicts = [{"char": char, "count": count} 
                     for char, count in dictionary.items() if char.isalpha()]
    
    # Sort the list in place from greatest to least
    list_of_dicts.sort(key=lambda x: x["count"], reverse=True)
    
    return list_of_dicts


# Function to generate and print the report
def report(list_of_dicts, book_path, word_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in list_of_dicts:
        char = entry["char"]
        cnt  = entry["count"]
        print(f"{char}: {cnt}")
    print("============= END ===============")
    