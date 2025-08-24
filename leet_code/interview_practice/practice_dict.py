"""
A simple class-based contact book where:
You can add contacts
Update phone numbers
Search by name
Delete a contact
View all contacts
"""
"""
class ContactBook:
    def __init__(self, contacts):
        self.contacts = { }

    def add_contact(self, name, phone_num):
        self.contacts[name] = phone_num


    def update_contact(self, name, new_num):
        if name in self.contacts:
            self.contacts[name] = new_num

    def search_contact(self, name):
        if name in self.contacts:
            print(name)
        

    def del_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        

    def view_all():
        pass
        
"""

s = "roshshah"
 
#   d = {
#         'h' : 1,
#         'e' : 1,
#         'l' : 2,
#         'o' : 1

#  }


d= { }
for char in s:
    if char in d:
        d[char] = d[char] + 1
    else:
        d[char] = 1
print(d)
    
    


"""
d = {
    'name' : 'Richie',
    'city' : 'Bay Area',
    'abc'  :  5,
    'd'    :  10
}


d1 = { }

#inserting key-value pairs
d1['a'] = 10
d1['b'] = 'hi'
d1['c'] = 9
d1['d'] =  'richie'

d1.update({'a' : 18})

d1['b'] = 'hey'

print(d1['a'])


#loop over key value pair:
for key, val in d1.items():
    print(f"key = {key}, val = {val}")

#delete a value 
del d1['a']
print(d1)


find = 9
if find in d1.values():
    print(find)



# def dic_practice():
#     d = {'a' : 0,
#          'b' : 4,
#          'c' : 'raxit',
#          'd' : True,
#          'e' : 5.5,  
#          'f' : ['raxit']      
#          }

#     print(d['e'])

#     d['e'] = 'raxit'

#     d['e']= d['e'] + ' rocks'
#     print(d['e'])

# if __name__ == "__main__":
#     dic_practice()

"""