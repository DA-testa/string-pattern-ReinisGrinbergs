
def read_input():
    data = input()
    if data[0]=="I":
        pattern=input()
        text = input()
    elif data[0]=="F":
        inputf = '06'
        inputf = "tests/" + inputf
       
        with open(inputf, 'r') as file:
                pattern, text = file.read().splitlines()
    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))
def get_occurrences(pattern, text):
    lP = len(pattern)
    lT = len(text)
    hP = hash(pattern)
    hT = hash(text[:lP])
    output = []
    for i in range(lT-lP+1):
        if hP == hT:
            if pattern == text[i:i+lP]:
                output.append(i)
            else:
                for j in range(lP):
                    if text[i+j] != pattern[j]:
                        break
                else:
                    output.append(i)
        if i < lT-lP:
            hT = hash(text[i+1:i+lP+1])
    return output

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
