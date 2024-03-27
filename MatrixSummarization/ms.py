x = [[1,3,5],[2,4,1],[1,5,7]] # We created a nested list and assign to x.

y = [[3,3,4],[2,4,1],[3,5,4]] # We created a nested list and assign to y.

result = [[0,0,0],[0,0,0],[0,0,0]] # We created a list that there are zeros and assign to result.

for i in range(len(x)):
    for j in range(len(y)):
        result[i][j] = x[i][j] + y[i][j] # Adding corresponding elements

print(result) # Print the result
