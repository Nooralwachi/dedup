def dedup(filename):
    lines = []
    with open(filename, 'r') as file, open('output.txt', 'w') as fw:
        for line in file:
            if line.strip() not in lines:
                lines.append(line.strip())
        for line in lines:
            fw.write(line +'\n')

dedup('file_test.txt')