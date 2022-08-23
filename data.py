
from slicer import Slicer

# list data
data = [
    106, 1589, 175, 145, 8888, 1258
]
#2 is amount to split
data_slice = Slicer.cut(data, 2)
print(data_slice)


data = [
    {
        "foodname": "Rasmalai",
        "price": 900
    }, 
    {
        "foodname": "Gulab Jamun",
        "price": 890
    },
    {
        "foodname": "Jalebi",
        "price": 489
    },
    {
        "foodname": "Chicken Biryani",
        "price": 7890
    },
    {
        "foodname": "Shahi Tukda",
        "price": 745
    },
]
print(Slicer.cut(data, 2))


