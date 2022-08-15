import figure_area

s1 = figure_area.square(3)
s2 = figure_area.rectangle(4, 2)

result = s1 - s2
if result > 0:
    print ('s1 > s2')
elif result < 0:
    print('s1 < s2')
else:
    print ('s1 = s2')