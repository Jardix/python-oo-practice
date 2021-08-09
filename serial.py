"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    # This is not correct, it doesn't work. Referring to solution to see how close I was.
    # def __init__(self, start):
    #     self.start = start
        
    # generated = start

    # def generate():  
    #     generated += 1      
    #     return generated

    # def reset():
    #     generated
    #     return start
    
    # So, not very. 
    def __init__(self, start=0):
        """Make a new generator, starting at 'start'"""

        # So this is like three lines of code combined into one; I think I know what we're doing here? Initializing start, and next, based on the passed in 'self'? 
        self.start = self.next = start

    def __repr__(self):
        """Show Representation."""
        # Didn't do this at all.

        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """Return next serial number."""

        self.next += 1 # Had this!
        return self.next - 1 # Okay, so the outside variable of self.next is going up by one, but we're returning that value - 1, without changing the outside value. 
        # So at the start, 
        # next = 100
        # Then it goes up one, and we return that - 1
        # next = 101, return 100
        # next = 102, return 101
        # This is an odd way of doing that. 

    def reset(self):
        """Reset Serial number to original start."""

        self.next = self.start
