import random
Numbs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
names = ('bob', 'jeff', 'dylan', 'table')
emails = ('@gmail.com', 'outook.com', '@yandex.com')
Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def print_names():
    print(str(random.choice(names)))
def print_numbs():
    print(str(random.choice(Numbs)))
def print_emails():
    print(str(random.choice(emails)))
def print_usr():
    print("----------------")
    print("username below")
    print("----------------")
def print_pass():
    print("----------------")
    print("password below")
    print("----------------")
def gen_pass():
    print(str(random.choice(Letters)))
    print(str(random.choice(Numbs)))
def prnt_line():
    print("----------------")

print_usr()
for b in range(2):
    print_names()
print_numbs()
print_numbs()
print_emails()
print_pass()
gen_pass()
gen_pass()
gen_pass()
for x in range(2):
    prnt_line()

