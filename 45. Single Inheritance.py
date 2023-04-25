class nokia:
    company = "Nokia India"
    website = "www.Nokia-India.com"
    def contact_details(self):
        print("Address          : Cherry Road , Near Bus Stand , Salem ")

class nokia1100(nokia):
    def __init__(self):
        self.name = "Nokia 1100"
        self.year = 1998
    def product_deatils(self):
        print("Name             : ",self.name)
        print("Year             : ",self.year)
        print("Company Name     : ",self.company)
        print("company website  : ",self.website)

mobile = nokia1100()
mobile.product_deatils()
mobile.contact_details()