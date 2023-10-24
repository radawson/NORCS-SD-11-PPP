# activity for errors
class FileManipulator:
    # The constructor should accept the name of a file to read in and should continually 
    # prompt for input if the name given causes an error. 
    # Make sure that you give an informative message if an error is raised.
    def __init__(self, file_name):
        self.file_name = file_name
        self.contents = self.read_file(file_name)

    def read_file(self, file_name):
        try:
            myfile = open(file_name, 'r') # Open a file for reading.
            contents = myfile.readlines() # Read in the content by line.
            myfile.close() # Explicitly close the file
            return contents
        except FileNotFoundError:
            print("File not found. Please try again.")
            return self.read_file(input("Enter a file name: "))

    def reverse(self, file_name):
        # This function should accept the name of a file to write to and should write each line of the original file to this new file. However, in the new file, although the line order will be the same, the string that makes each line will be reversed. So "cheese" will become "eseehc". Be careful not to add an extra newline character at the beginning of the file. 
        # Make sure that errors are handled elegantly, and appropriate error messages are given.
        # Ensure the first line is not a newline character
        try:
            new_file = open(file_name, 'w')
            for line in self.contents:
                new_line = line[::-1] + "\n"
                if new_line[0] == "\n":
                    new_line = new_line[1:]
                new_file.write(new_line)
            new_file.close()
        except Exception as e:
            print(repr(e))
            print("Error writing to file.")            

if __name__ == "__main__":

    f = FileManipulator("tmp.txt")
    print(f.contents)
    f.reverse("tmp2.txt")
