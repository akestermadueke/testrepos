'''
Created on Mar 3, 2022
Last Edited on Mar 3, 2022
@author: Madueke Emmanuel
'''
from decimal import Decimal as dec
# Markup
wholesale_cost = 5.00
markup_percentage = 50
def calculateRetail(c, p):
    if type(c) and type(p) in (dec, int, float):
        if c and p >= 0:
            markup = c * (p/100)
            retail_price = c + markup
            return retail_price
        else:
            return 'Enter a positive number!'
    else:
        return 'Enter a number!'
retail_price = calculateRetail(wholesale_cost, markup_percentage)
print(retail_price)
# Rectangle Area
def getLength(x):
    return float(x)
def getWidth(x):
    return float(x)
length = getLength(9)
width = getWidth(4)
def getArea(x, y):
    return x * y
area = getArea(length, width)
def displayData(x=length, y=width, z=area):
    length_info = 'The length of the rectangle is: ' + str(x) + ' cm'
    width_info = 'The width of the rectangle is: ' + str(y) + ' cm'
    area_info = 'The area of the rectangle is: ' + str(z) + ' cm square'
    return length_info, width_info, area_info
data = displayData()
print('a ->', length)
print('b ->', width)
print('c ->', area)
print('d)')
for datum in data:
    print('->', datum)
# Winning Division
def getSales(sales_figure):
    if type(sales_figure) in (int, float):
        if sales_figure >= 0:
            return float(sales_figure)
        else:
            return 'Enter a positive number'
    else:
        return 'Enter a valid number'
def findHighest(**sales_figures):
    is_figure = True
    for sale_figure in sales_figures:
        if type(sales_figures[sale_figure]) in (int, float):
            if sales_figures[sale_figure] < 0:
                is_figure = False
                break
        elif type(sales_figures[sale_figure]) == str:
            is_figure = False
            break
    if is_figure:
        coy_division = 'Southeast'
        reference = float(sales_figures['Southeast'])
        for division in sales_figures:
            if reference < sales_figures[division]:
                reference = float(sales_figures[division])
                coy_division = division
        return coy_division + ' has the highest sales totaling ' + str(reference)
    else:
        return 'You might have entered a wrong data type.'
coy_division = {'Northeast':560, 'Southeast':2000, 'Northwest':150, 'Southwest':1500}
the_best_division = findHighest(**coy_division)
print(the_best_division)
sales_figure = getSales(coy_division['Southeast'])
print(sales_figure)
# Safest Driving Area
def getNumAccidents(value):
    if type(value) == int and value >= 0:
        return value
    else:
        return 'Enter an integer!'
def findLowest(**regions):
    is_region = True
    for region in regions:
        if type(regions[region]) != int or regions[region] < 0:
            is_region = False
            break
    if is_region:
        city_region = 'North'
        reference = regions['North']
        for region in regions:
            if regions[region] < reference:
                reference = regions[region]
                city_region = region
        return city_region + ' has the lowest number totaling ' + str(reference)
    else:
        return 'Enter an integer!'
major_city_accident = {
    'North': 56,
    'South': 65,
    'East': 50,
    'West': 60,
    'Central': 87
}
accident_value = getNumAccidents(major_city_accident['Central'])
the_minimum = findLowest(**major_city_accident)
print(accident_value)
print(the_minimum)