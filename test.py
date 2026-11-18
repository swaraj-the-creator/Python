class B_details:
    def __init__(self,title,author,is_borrowed,date,re_date):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        self.date = date
        self.re_date = re_date

books = {"Dragonball Super Pt 4":"Akira Toriyama","Dragonball Z Pt 18":"Akira Toriyama","Geronimo Stilton Pt 11":"Elisabetta Dami","Dog man Pt1":"Dav Pilkey","Goosebumps Pt 3":"R.L. Stine"}

books2 ={"Dragonball Super Pt 4":"Dragonball Super Pt 4","Dragonball Z Pt 18":"Dragonball Z Pt 18","Geronimo Stilton Pt 11":"Geronimo Stilton Pt 11","Dog man Pt1":"Dog man Pt1","Goosebumps Pt 3":"Goosebumps Pt 3"}

B = ("Dragonball Super Pt 4","Dragonball Z Pt 18","Geronimo Stilton Pt 11","Dog man Pt1","Goosebumps Pt 3")        

while True:
    try:
        print("\nBooks available : ",B)
        titl = input("\nEnter the book name which you want to borrow : ")
        B1 = books2.get(titl)
        dat = int(input("\nEnter the borrow date without slash or dash (ex for 1-01-0001 = 1010001): "))
        toda_dat = int(input("\nEnter the today's date without slash or dash (ex for 12-8-2026 : 1282026): "))

        if toda_dat > dat:
            boo_subm = input("Have you submitted your book")
            avail = "No"
        else:    
            if toda_dat == dat or toda_dat >= dat:    
                avail = "Yes"
            else:
                avail = "No"        
        
        Borrow1 = B_details(titl,B1,avail,dat,dat + 100)
        print(f"\n======= {B1} book details: =======")
        
        if titl == B1 :
            print("\nTitle: ",Borrow1.title)
            print("Author: ",Borrow1.author)
            print("Is Available now: ",Borrow1.is_borrowed)
            print("Date of borrow: ",Borrow1.date)
            print("Date of return: ",Borrow1.re_date)
        
        else:            
            print("\nNot in stock")
        print("\n======================================")
    except ValueError:
            print("Wrong value")
            continue    
    break
    
    