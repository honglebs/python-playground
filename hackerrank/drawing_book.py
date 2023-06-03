# Drawing Book

# parameters (n, p)
# n, being the number of pages in the book 
# p, being the page to turn to (i.e destination page)

# return an int: the minimum numbers of pages to turn to (check front & back)

# def pageCount(n, p):
#     # checking our location to destination
#     current_page = []
#     count = 0
    
#     # iterate through the book starting from 1 to number of pages in the book 
#     for i in range(1, n + 1):

#         # conidtion if the page we are currently on is not equal to the destination page,
#         # we add +1 to counter (number of page turns)
#         if current_page(i) != p:
#             count += 1
#     return count 

# print(pageCount(5, 4))

# what other ways can this be completed

# pageCount function the minium amt of page turns to get to your desired page
def pageCount(n, p):
    # Calculate the number of pages to turn from the beginning
    pages_from_front = p // 2

    # Calculate the number of pages to turn from the end
    pages_from_back = (n // 2) - (p // 2)

    # Return the minimum number of pages to turn
    return min(pages_from_front, pages_from_back)

print(pageCount(5, 4))
