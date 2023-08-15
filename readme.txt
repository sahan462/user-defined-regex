This program lets you perform pattern matching using special characters (^, ., +) in patterns to search for matches in texts.

Note: Complex Patterns Combine special characters for complex matches:
Example:
    Pattern: hel.o h.w
    Text: hello how are you
    Result: Found 'hel.o h.w' pattern at line:n index:m



Follow these steps(for running):

Step 1: Prepare Input
    Inside the input folder, create pattern-text pairs(Each pair should share the same number n):
         Pattern files: pattern<n>.txt (e.g., pattern1.txt)
         Text files: text<n>.txt (e.g., text1.txt)


    Add your input to the text<n> file.

Step 2: Run the Program
    Run the provided Python script in the same directory as the input folder.


Step 3: View Results
    The program processes each pattern-text pair and saves the results in the output folder.
    Results are in the `output<n>.txt` file. Each file contains True (matched) or False (not matched).

You can create as many input, output, and pattern files as sharing the same number n.
    ex - if you create a pattern2 file, associated text file => text2, associated patternmatch file => patternmatch2

Inside the pattern<n>.txt file you can add all patterns line by line which is needed to search through the text<n>.txt file. The program will iterate through all the patterns in the pattern<n>.txt file and write output to the patternmatch<n>.txt file.

For further clarification refer to the given pattern1.txt, text1.txt, and patternmatch1.txt files. 
