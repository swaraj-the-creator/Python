class B_details:
    def __init__(self,title,author,is_borrowed,date,re_date):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        self.date = date
        self.re_date = re_date
        
        
Borrow1 = B_details("Percy Jackson","Rick Riordan","No","12-7-2026","12-8-2026")
Borrow2 = B_details("Dragonball Z","Akira Toriyama","Yes","23-11-2026","22-12-2026")
Borrow3 = B_details("Geronimo Stilton","?UNKOWN?","No","1-2-2026","2-3-2026")
print("\nFirst book details: ")
print("Title: ",Borrow1.title)
print("Author: ",Borrow1.author)
print("Is borrowed now: ",Borrow1.is_borrowed)
print("Date of borrow: ",Borrow1.date)
print("Date of return: ",Borrow1.re_date)

print("\nSecond book details: ")
print("Title: ",Borrow2.title)
print("Author: ",Borrow2.author)
print("Is borrowed now: ",Borrow1.is_borrowed)
print("Date of borrow: ",Borrow2.date)
print("Date of return: ",Borrow2.re_date)

print("\nThird book details: ")
print("Title: ",Borrow3.title)
print("Author: ",Borrow3.author)
print("Is borrowed now: ",Borrow1.is_borrowed)
print("Date of borrow: ",Borrow3.date)
print("Date of return: ",Borrow3.re_date)