"""Word Finder: finds random words from a dictionary."""
import random

# I have a very, very vague idea of what needs to happen and where; I'm going to refer to the solution to see how its done and then recreate it. 

# So apparently Python has the random module which does 95% of the work I was doing in my head; good to know.

class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """


    def __init__(self, file_path):
        """Read dictionary and reports number of items read."""

        dict_file = open(file_path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read.")

    def parse(self, dict_file):
        """Parse dict_file into a list of words."""
        # So this returns a list, stripped of the newline characters, in a for loop of the dict_file that's passed in. Which, in the case of words.txt, would be thousands, if not millions.
        # Update: it's 235,886 words in that file!
        return [w.strip() for w in dict_file]

    def random(self):
        """Return a random word."""
        # Mighty brave, in my opinion, using the Library 'random', the function 'random', and the function in random, called random. I think I'd have done some my_random's somewhere in there. 
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """
    # And we're not using super() because we're just replacing the functionality with a new function, right?
    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        # so the if w.strip() checks to see if it's a blank line, which would return anything but True, and the 'and not' part checks to make sure it's not a commented line. 
        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
    
