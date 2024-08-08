# Python Project 1: Anagram Solver

## Description
The main goal of this project is to use four modified WordNet dictionary index files and some Python code to build an application that can solve anagram word game puzzles. The user enters a series of letters, such as "BEALF," and the code returns the word "fable" along with its word type, e.g., "noun."

## Requirements
- Python 3.x
- WordNet dictionary index files:
  - `NounsIndex.txt`
  - `VerbsIndex.txt`
  - `AdjIndex.txt`
  - `AdvIndex.txt`

## Setup
1. Clone the repository.
2. Ensure the WordNet dictionary index files (`NounsIndex.txt`, `VerbsIndex.txt`, `AdjIndex.txt`, and `AdvIndex.txt`) are in the same directory as the script.
3. Run the Python script.

## Usage
1. Execute the script in your terminal:
   ```bash
   python anagram_solver.py
   ```
2. Enter a jumbled word (e.g., "BEALF") when prompted.
3. The script will output the unscrambled word(s) along with their word type(s) (e.g., "FABLE NOUN").
4. To quit, simply press `<enter>` without typing a word.

## Functions

### `read_file(fileName)`
Reads the content of a specified file.
- **Parameters:**
  - `fileName` (str): The path to the file.
- **Returns:**
  - `str`: The content of the file as a string.

### `insert_data(word_dict, files, type)`
Inserts words and their types into a dictionary after sorting the characters in the word.
- **Parameters:**
  - `word_dict` (dict): The dictionary to store the words.
  - `files` (list): A list of lines from the WordNet index files.
  - `type` (str): The type of word (Noun, Verb, Adjective, Adverb).
- **Returns:** None

### `find_word(jumbled_word, word_dict)`
Finds the unscrambled word(s) from the dictionary that match the sorted characters of the jumbled word.
- **Parameters:**
  - `jumbled_word` (str): The input jumbled word.
  - `word_dict` (dict): The dictionary containing the sorted words as keys.
- **Returns:**
  - `list`: A list of possible unscrambled words and their types, or `None` if no match is found.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Citations
- [Python Documentation](https://docs.python.org/3/)
- WordNet: Princeton University "About WordNet." WordNet. Princeton University. 2010.
