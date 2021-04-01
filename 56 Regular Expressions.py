import re

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''

# findall, search, split, sub, finditer
print(r"\n") # r = raw string

# patt = re.compile(r'fass')
# patt = re.compile(r'.ad') # . means any character matches
# patt = re.compile(r'^Tata') # ^ means starts with exact same character
# patt = re.compile(r'iiii$') # $ means ends with exact same characte
# patt = re.compile(r'ta*') # * means character starts with and ends with as many match
# patt = re.compile(r't*a*') # * means character starts with and ends with as many match
# patt = re.compile(r'ta+') # + means only a single char or both char
# patt = re.compile(r'ai{2}') # It means show only two matches
# patt = re.compile(r'(ai){2}') # It means double character matches
patt = re.compile(r'ai{1}|Fax') # | means either show ai or Fax

patt = re.compile(r'\ATata') # \A means string stars with Tata
patt = re.compile(r'\bFax') # \B means character ends with Fax
patt = re.compile(r'Fax\b') # \B means ends with Fax

matches = patt.finditer(mystr)
for match in matches:
    print(match)

# patt = re.compile(r'fass')
# patt = re.compile(r'.adm')
# patt = re.compile(r'^Tata')
# patt = re.compile(r'iin$')
# patt = re.compile(r'ai{2}')
# patt = re.compile(r'(ai){1}')
# patt = re.compile(r'ai{1}|Fax')


# Special Sequences
# patt = re.compile(r'Fax\b')
# patt = re.compile(r'27\b')
# patt = re.compile(r'\d{5}-\d{4}')
# Task
# Given a string with a lot of indian phone numbers starting from +91

# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)


"""


"""
