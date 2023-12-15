from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if value.isnumeric() and len(value) ==10:
            super().__init__(value)
        else:
           raise ValueError ("Phone number must contains only 10 numbers")        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def check_phone_exist(self,phone):
        phone_record = [record for record in self.phones if record.value == phone]
        if len(phone_record) >0:
            return phone_record
        else:
            raise ValueError(f"Phone number {phone} was not found")   

    def add_phone(self,phone):
        self.phones.append(Phone(phone))
    

    def find_phone(self,phone):
        for phone in self.check_phone_exist(phone):
            return phone
        
    def edit_phone(self,phone_to_replace,new_phone):
        to_edit = self.remove_phone(phone_to_replace)        
        for i in range(to_edit):            
            self.add_phone(new_phone)
      
    
    def remove_phone(self, phone):
        to_remove = self.check_phone_exist(phone)           
        for phone in to_remove:
            self.phones.remove(phone)     
        return len(to_remove)        
        
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict,Record):

    def add_record(self,record=Record):
        self.data[record.name.value] = record     

    def find(self,name):
        return self.data[name]
    
    def delete(self,name):
        self.data.pop(name)
