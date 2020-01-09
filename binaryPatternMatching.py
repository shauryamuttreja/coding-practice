def binaryPatternMatching(pattern, s):
    new = ""
    for letter in s:
        if letter in ["a", "e", "i", "o", "u", "y"]:
            new = new + "0"
        else:
            new = new + "1"
            
    print(new)
    count = 0
    for i in range(len(new)):
        if new[i:i+len(pattern)] == pattern:
            count += 1

    return count