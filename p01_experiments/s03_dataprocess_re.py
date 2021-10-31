# regular expression
import re


# re.finditer | Will return all results.
it = re.finditer(r"\d+","My phone number is: 702389, and my gf's number is: 781687")
for i in it:
    print(i.group())

# re.search | Only return the first result.
itt = re.search(r"\d+","My phone number is: 702389, and my gf's number is: 781687")
print(itt.group())

# preload regular expression.

#   preload number re.
obj_num = re.compile(r"\d+")
ret = obj_num.findall("My phone number is: 702389, and my gf's number is: 781687")
print(r"-------------Print preload R.E. results--------------")
print(f"The result's type is: {type(ret)}")
print(f"The results is: {ret}")


#
s = """
<div class='VPS'><spam id='1'>DMIT</spam></div>
<div class='NAT'><spam id='5'>AnyHK</spam></div>
"""

obj_css = re.compile(r"div class='(?P<Type>.*?)'><spam id='\d+'>(?P<Host>.*?)</spam></div>", re.S) # re.S: make dot(.) can find new line.
results = obj_css.finditer(s)

# temp storage
for it in results:
    print("The host is: ", {it.group("Host")}, "type is: ",it.group("Type"))