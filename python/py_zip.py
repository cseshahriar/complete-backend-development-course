""" zip """
friends = ['nazmul', 'piyash']
time_since_seen  = [2000, 2001]

zip_data = zip(friends, time_since_seen)
print(zip_data)
zip_data_list = list(zip_data)
print(zip_data_list)

print('\n')
for i in zip_data:
    print(i[0])