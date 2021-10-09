#This program convert the fahrenhiet to celsius:

def convert(s):
    f = float(s)
    c = (f-32)*5/9
    return c

print(convert(78))