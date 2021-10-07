symbols = {"-", ",", ".", "!", "?", "'", ":", ";", "_", '"'}

with open("text.txt", "r") as file, open("output.txt", "w") as result:
    index_count = 1
    letters_count = 0
    punctuation_marks_count = 0
    while True:
        line = file.readline().strip()
        if not line:
            break
        for i in line:
            if i == " ":
                continue
            elif i in symbols:
                punctuation_marks_count += 1
            else:
                letters_count += 1
        result.write(f"Line {index_count}: {line} ({letters_count})({punctuation_marks_count})")
        result.write("\n")
        index_count += 1
        letters_count = 0
        punctuation_marks_count = 0
