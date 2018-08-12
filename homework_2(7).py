date = '06.13.1985'
mm_idx = date.find('.')
dd_idx = date.find('.', mm_idx+1)


mm = int(date[:mm_idx])
dd = int(date[mm_idx+1:dd_idx])
yy = int(date[dd_idx+1:])

print("US date format is:", date)
print("EU date format is: %02d.%02d.%04d" %(dd, mm, yy))

