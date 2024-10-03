numBooks, numWant = map(int, input().split())
books = []
for _ in range(numBooks):
    title, author = input().split(", ")
    books.append((author, title))

books.sort()
idx = {}
for i, (author, title) in enumerate(books):
    idx[title] = i+1
#print(idx)
for _ in range(numWant):
    print(idx.get(input(), -1))