motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.insert(0,'harley')
print(motorcycles)

del motorcycles[3]
print(motorcycles)
popped_motorcycles=motorcycles.pop(2)
print(motorcycles)
print(popped_motorcycles)