def main():
    s = input()
    list(s).sort()
    from collections import Counter
    c = Counter(s)
    for num in c.most_common(3):
        print(num[0], num[1])


if __name__ == '__main__':
    main()