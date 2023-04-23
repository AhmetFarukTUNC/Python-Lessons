import random

# print(dir(random))

# print(help(random))

print(random.random())

print(random.random()*100)

print(random.uniform(1,10))

print(int(random.uniform(1,10)))

print(random.randint(1,100))

names = ["Ahmet","Mahmut","Hüseyin","Mehmet"]

print(names[random.randint(0,len(names)-1)])

print(random.choice(names))

print(random.choice("Hello There!"))

print(list(range(10)))

list1 = list(range(10))

random.shuffle(list1)

print(list1)

list2 = list(range(100))

list3 = random.sample(list2,3)

print(list3)

list4 = random.sample(names,2)

print(list4)