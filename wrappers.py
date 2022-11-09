class Engineer:
    def __init__(self, name, age, salary, companyName):
        self.name = name
        self.age = age
        self.salary = salary
        self.companyName = companyName
    @property
    def company(self):
        return self.companyName
    @company.setter
    def company(self, CompanyName):
        self.companyName = CompanyName
        
EO = Engineer("Phillip", 21, 2100,"Total oil and gas Company")
print(EO.name, "works with", EO.company,"aged",EO.age, "and earns $",EO.salary, "per month.")
EO.company = "South Africa Gold Minners"
print(EO.name, "works with", EO.company,"aged",EO.age, "and earns $",EO.salary, "per month.")

        
  


        