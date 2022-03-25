import os
import glob

csv_files = glob.glob(os.path.join("C:\\Users\\HP\\Downloads\\csv_files", "*.csv"))

all_csv_files ={}
for i in range(len(csv_files)):
    all_csv_files[i] = csv_files[i]
print(all_csv_files)

dict_key_req = [int(x) for x in input("Enter the key of the data to be converted:  ").split()]
req_loc = []
for loc in all_csv_files:
    if loc in dict_key_req:
        req_loc.append(all_csv_files[loc])
print(req_loc)