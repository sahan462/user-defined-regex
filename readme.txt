This program lets you perform pattern matching using special characters (^, $, ., ?, *) in patterns to search for matches in texts.

Note: Complex Patterns Combine special characters for complex matches:
Example:
    Pattern: hel.o h.w
    Text: hello how are you
    Result: True



Follow these steps(for running):

Step 1: Prepare Input
    Inside input folder, create pattern-text pairs(Each pair should share the same number n):
         Pattern files: pattern<n>.txt (e.g., pattern1.txt)
         Text files: text<n>.txt (e.g., text1.txt)


    Add your input to text<n> file.

Step 2: Run the Program
    Runthe provided Python script in the same directory as the input folder.


Step 3: View Results
    The program processes each pattern-text pair and saves results in the output folder.
    Results are in `output<n>.txt` file. Each file contains True (matched) or False (not matched).



