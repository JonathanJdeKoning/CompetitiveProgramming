numbooks = int(input())
books = sorted([int(input()) for x in range(numbooks)])
bookslen = len(books)
cheapsum = 0
for x in range(bookslen-3,-1,-3):
    cheapsum+=books[x]

print(sum(books) - cheapsum)