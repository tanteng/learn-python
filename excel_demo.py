import tablib
headers = ('lie1', 'lie2', 'lie3', 'lie4', 'lie5')
mylist = [('23','23','34','23','34'),('sadf','23','sdf','23','fsad')]
mylist = tablib.Dataset(*mylist, headers=headers)
with open('excel.xlsx', 'wb') as f:
    f.write(mylist.xlsx)