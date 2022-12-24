data1 = ['react', 'angular', 'public', 'general', 'ar or']
data2 = ['React', 'Angular', 'Public', 'General', 'aror']

data1 = str(data1).replace(' ', '').replace('doc', '').replace('.','').lower()
data2 = str(data1).replace(' ', '').replace('doc', '').replace('.','').lower()

print(data1)
print(data2)

assert data1 == data2
