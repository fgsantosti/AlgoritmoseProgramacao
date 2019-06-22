import pickle

data = "ADS Módulo I"

#f = open('mi.pickle', 'wb')

'''
with open('data.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
'''

f = open('data.pickle', 'wb')
for i in range(100):
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

f = open('data.pickle', 'rb')
for i in range(100):
    data = pickle.load(f)
    print(data)



'''
with open('data.pickle', 'rb') as f:
    data = pickle.load(f)
    print(data)
'''
