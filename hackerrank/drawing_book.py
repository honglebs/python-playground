# Drawing Book

# parameters (n, p)
# n, being the number of pages in the book 
# p, being the page to turn to (i.e destination page)

# return an int: the minimum numbers of pages to turn to (check front & back)

def pageCount(n, p):
    # checking our location to destination
    current_page = 0
    count = 0
    
    for i in range(1, n + 1):

        if current_page(i) != p:
            count += 1

print(pageCount(5))