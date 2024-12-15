import coffeshop



class Paginate:
    def __init__(self, items, total_pages):
        self.items = items
        self.total_pages = total_pages  
        self.current_pages = 1  

    def next_page(self):
        # nxt = self.current_page = self.current_page +1
        self.current_pages+=1
        return self.current_pages
    
    def getVisibleItems(self):

        start_index = (self.current_pages - 1) * self.total_pages #1 -- 5 ,5--10
        end_index = start_index + self.total_pages
        return self.items[start_index:end_index]

    def current_page(self):
        return self.current_pages
    
    def previuos_page(self):
        prev = self.current_pages = self.current_pages -1
        return prev
    
    def first_page(self):
        if self.current_pages ==1:
            return "you already in the current page"
        else:
            self.current_pages = 1
            return self.current_pages
    
    def last_page(self):
        if self.current_pages == self.total_pages:
            return "you already in the current page"
        else:
            self.current_pages = self.total_pages
            return self.current_pages
    
    def to_page(self, page):
        if page <=0:
            self.current_pages = 1
            return self.current_pages
        if page >= self.total_pages:
            self.current_pages = self.total_pages
            return self.current_pages
        else:
            self.current_pages = page
            print(self.current_pages)
        
    

x = [num for num in range(100)]

p = Paginate(x,10)

# print(p.getVisibleItems())
# print(p.next_page())
# print(p.getVisibleItems())
# print(p.previuos_page())
# print(p.first_page())
# print(p.last_page())
# print(p.getVisibleItems())
p.to_page(4)
print(p.getVisibleItems())



