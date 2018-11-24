a = [{"Name": "Mahesh", "age": 15,"Town": "Hyd"},
     {"Name": "Ramesh", "age": 17,"Town": "Bangalore"},
     {"Name": "somu", "age": 19, "Addr": {"city": "Chennai","street": "Main Street"}},
     {"Name": "sudha", "age": 7, "Town": ["Calcutta","Bangalore","Chennai"]},
     {"Name": "janu", "age": 10, "Town": "Mumbai"}]
#
# b = a[2]["Name"]
# c = a[2]["age"]
# d = a[2]["Addr"]['street']
print("His name is ",a[3]["Name"], "age is ",a[3]["age"], "and his town is",a[3]["Town"][1])
