class India():
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is the most widely spoken language")
    def type(self):
        print("India is a developing country")
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA")
    def language(self):
        print("English is the primary language of USA")
    def type(self):
        print("USA is a developed country")
odj_ind = India()
odj_USA = USA()
for country in (odj_ind,odj_USA):
    country.capital()
    country.language()
    country.type()