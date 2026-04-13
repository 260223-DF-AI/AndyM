def word_occurance(): # we use input around here()
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())
    count = {}
    for word in words:
        count[word] = count.get(word, 0 ) + 1


    print("Distinct Words :", len(count.keys()))
    for word in count.keys():
        print(f"word:{word} count:{count[word]}")
    
if __name__ == "__main__":
    word_occurance()