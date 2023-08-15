import os

# Function to traverse the text and pattern using the PI table
def search_traverse(txt, pat, line_number, file_):
    N = len(txt)  # Length of the text
    M = len(pat)  # Length of the pattern
    
    piTable = [0] * M  # Initialize the PI table for pattern
    repeat_len = 0     # Length of repeated characters in case of '+'
    repeating_character = ''  # Character to repeat in case of '+'
   
    getPItable(pat, M, piTable)  # Build the PI table
    
    i = 0  # Index for the text
    j = 0  # Index for the pattern
    
    while i < N:
        if pat[j] == '+':
            #handle "+" specially
            repeating_character = pat[j - 1]
            while (repeating_character == txt[i]):
                i += 1
                repeat_len += 1
            repeat_len -= 1
            j += 1
        elif j == 0 and i == 0 and pat[j] == '^':
            # Handle beginning of line pattern
            k = 1
            not_found = False;
            while k < len(pat[1:]):
                if pat[k] == '.':
                    i += 1
                    j += 1
                elif pat[k] == '+':
                    repeating_character = pat[k - 1]
                    while repeating_character == txt[i]:
                        i += 1
                        repeat_len += 1
                    repeat_len -= 1
                    j += 1
                elif pat[k] == txt[i]:
                    i += 1
                    j += 1
                else:
                    not_found = True
                    break
                k += 1
            i += 2
            j += 2
            if(not_found):
                break
        elif pat[j] == '.':
            #handle "." pattern
            i += 1
            j += 1
        else:
            if pat[j] == txt[i]:
                i += 1
                j += 1

        if j == M:
            file_.write("Found "+pat+" pattern at line:" + str(line_number) + " index:" + str(i - j - repeat_len) + "\n")
            repeat_len = 0
            j = piTable[j - 1]
            if pat[j - 1] == '^':
                break                
        elif pat[j] in ".+^":
            continue
        else:
            if i < N and pat[j] != txt[i]:
                if j != 0:
                    j = piTable[j - 1]
                else:
                    i += 1

# Build the PI table for the KMP algorithm
def getPItable(pat, M, piTable):
    len = 0 
    piTable[0] 
    i = 1

    while i < M:
        if pat[i] == pat[len]:
            len += 1
            piTable[i] = len
            i += 1
        else:
            if len != 0:
                len = piTable[len - 1]
            else:
                if pat[0] == '^':
                    piTable[i] = 1
                else:
                    piTable[i] = 0
                i += 1

# Process input and save output to a file
def process_and_save(pattern_filename, text_filename, output_filename):
    with open(f'input/{pattern_filename}', 'r') as pattern_file: 
        patterns = pattern_file.read().splitlines()
    with open(output_filename, 'a') as output_file:
        with open(f'input/{text_filename}', 'r') as text_file:
            lines = text_file.readlines()
            for j in range(0, len(patterns)):
                print(patterns[j])
                for i, line in enumerate(lines):
                    print(line,patterns[j])
                    search_traverse(line.strip(), patterns[j], i + 1, output_file)

# Main function
if __name__ == "__main__":
    input_directory = "input"  # Directory containing input files

    # List all files in the input directory
    input_files = [file for file in os.listdir(input_directory) if file.startswith("pattern") and file.endswith(".txt")]

    # Process each pattern file
    for pattern_filename in input_files:
        text_filename = pattern_filename.replace("pattern", "text")
        output_filename = pattern_filename.replace("pattern", "patternmatch").replace(".txt", ".txt")
        process_and_save(pattern_filename, text_filename, output_filename)
