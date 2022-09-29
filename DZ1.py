import numpy as np

# first
a = np.matrix([[1, 1, 1], [0.05, 0.07, 0], [0.05, 0, 0.06]])
b = np.matrix([[50000], [2250], [1400]])
x, y, z = np.linalg.solve(a, b)
#total = np.linalg.solve(a, b)
#print(total)
print("Ответ на задачу №1")
print(f"В первый банк вкладчик положил {x[0,0]} условных едениц.\nВо втрой банк вкладчик положил {y[0,0]} условных едениц.\nВ третий банк вкладчик положил {z[0,0]} условных едениц.\n")

# second
a = np.matrix([[1, 1, 1], [1, -1, 0], [1, 0, -1]])
b = np.matrix([[1328], [-120], [100]])
x, y, z = np.linalg.solve(a, b)
print("Ответ на задачу №2")
print(f"Количество Iphone6 {x[0,0]} штук.\nIphone11 {y[0,0]} штук.\nIphone12 {z[0,0]} штук.\n")

#third
a = np.matrix([[3, 0, 3], [6, 0.25, 0], [1, 1/3, 1]])
b = np.matrix([[1], [1], [1]])
row_data = np.linalg.solve(a, b)

x, y, z = 1/row_data

print("Ответ на задачу №3")
print(f"a2={np.round(x[0,0])} .\nb2={np.round(y[0,0], 4)}.\nc2={np.round(z[0,0])}.\n")

#fouth
a = np.matrix([[1, 1, 1], [9, 3, 1], [1, -1, 1]])
b = np.matrix([[12], [54], [2]])
x, y, z = np.linalg.solve(a, b)

print("Ответ на задачу №4")
print(f"a={np.round(x[0,0], 5)} .\nb={np.round(y[0,0], 4)}.\nc={np.round(z[0,0], 4)}.\n")

#5
def get_polynom(coords):
    a =[]
    b = []
    #print(len(coords))
    for j in coords:       
        local_a=[]
        b.append([j[1]])

        for elem in range(len(coords)):
            local_a.append(j[0]**elem)
        a.append(local_a)
    
    #print (a)
    #print (b)
    A=np.matrix(a)
    B=np.matrix(b)
    #print (A)
    #print (B)          
    return np.linalg.solve(A,B)

f = get_polynom([(2,52), (-3,767), (1,11), (-2,104), (-1, 1), (0,2)])
print(f.flatten())