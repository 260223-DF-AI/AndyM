punctuation = [".",",","'","\"","!"]
def main():
    s = input() # get input from program
    #s = str
    #print("S:",s)
    count = 0
    if s == "":
        return 0

    words = s.split(" ")

    for word in words:
        #print("word:",word)
        word = word.lower()

        if len(word) == 1: # this is true, no need to continue working
            count += 1
            continue

        sanitized_word = word
        # check for punctuation, and cut it off if it exists
        if word[len(word)-1] in punctuation:
            sanitized_word = word[:len(sanitized_word)-2]
        elif word[0]in punctuation:
            sanitized_word = word[1:]

        # check to see if last == first letter
        if sanitized_word[0] == sanitized_word[len(sanitized_word)-1]:
            count +=1
    print(count)
    return count
main()




"""
"Bob baked a big banana bread."
2

2
"Anna went to vote in the civic center."
2

2
"Hello world! No matching words here."
0

0
"A I U E O"
Traceback (most recent call last):
  File "main.py", line 31, in <module>
    main()
  File "main.py", line 27, in main
    if sanitized_word[0] == sanitized_word[len(sanitized_word)-1]:
IndexError: string index out of range

5
"Did dad see Eve and Otto today?"
4

4
"Wow! Hannah and Anna went kayaking at noon."
3

4
"""