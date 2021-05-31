# Create a class called scheme with scheme_id,
# scheme_name,outgoing_rate, and message_charge. Derive customer
# class form scheme and include cust_id, name and mobile_no
# data.Define necessary functions to read and display data.

class Scheme:
    scheme_id = 1
    scheme_name = "BSNL prepaid"
    outgoing_rate = 2.1
    message_charge = 1.5
    def display(self):
        print("scheme_id: ",self.scheme_id)
        print("scheme_name: ",self.scheme_name)
        print("outgoing_rate: ",self.outgoing_rate)
        print("message_charge: ",self.message_charge)

class Customer(Scheme):
    cust_id = 1
    name = "Het Vaghsia"
    mobile_no = 1234567890
    def display1(self):
        print("cust_id: ",self.cust_id)
        print("name: ",self.name)
        print("mobile_no: ",self.mobile_no)

cust = Customer()
cust.display()
cust.display1()
