
import csv
import random

class Benice:
    def __init__(self, data_file, corpus_file):
        self.data_file = data_file
        self.corpus_file = corpus_file
        self.text_data = ""
        self.word_map = {}
        
        # Read text file
        try:
            with open(self.data_file, 'r') as file:
                self.text_data = file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        
        # Read CSV file
        try:
            with open(self.corpus_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    word, substitutions = row[0], row[1].split('; ')
                    self.word_map[word] = substitutions
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.corpus_file} was not found.")

    def print_file_data(self):
        print(self.text_data)
    
    def print_corpus(self):
        for word, substitutions in self.word_map.items():
            print(f"{word}: {', '.join(substitutions)}")
    
    def substitute_word(self, word):
        if word in self.word_map:
            return random.choice(self.word_map[word])
        return word
    
    def generate_new_file(self, output_file):
        words = self.text_data.split()
        new_text = []
        
        for word in words:
            stripped_word = word.strip('.,!?')
            new_word = self.substitute_word(stripped_word)
            new_text.append(new_word)
        
        new_text = ' '.join(new_text)
        
        with open(output_file, 'w') as file:
            file.write(new_text)

# Example usage
if __name__ == "__main__":
    benice = Benice("testfile2.txt", "nice_corpus.csv")
    benice.print_file_data()
    print()
    benice.generate_new_file("test2.txt")


