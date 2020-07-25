#!/usr/bin/env python
# coding: utf-8

# In[ ]:


sudoku solver
board = [
    [0,0,0,0,8,0,6,4,0],
    [0,0,0,4,0,7,8,9,0],
    [0,6,0,0,0,0,3,0,0],
    [5,4,9,0,1,0,0,0,2],
    [2,0,0,0,0,6,0,5,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0],
    [9,0,0,0,4,2,0,0,0],
    [4,2,0,1,0,0,0,0,0]
]

def isvalid(bd,n,pos):
    for i in range(len(bd[0])):
        if bd[pos[0]][i] == n and pos[1] != i:
            return False
    for i in range(len(bd)):
        if n==bd[i][pos[1]] and pos[0]!=i:
            return False
    for i in range((pos[0]//3)*3,(pos[0]//3)*3 + 3):
        for j in range((pos[1]//3)*3,(pos[1]//3)*3 +3):
            if n==bd[i][j] and i!=pos[0] and j!=pos[1]:
                return False
    return True
def printbrd(bod):
    for i in range(len(bod)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - -")
        for j in range(len(bod[0])):
            if j%3==0 and j!=0:
                print("| ",end="")
            if j==8:
                print(bod[i][j])
            else:
                print(str(bod[i][j])+" ",end="")
def isempty(bd):
    for i in range(len(bd)):
        for j in range(len(bd[0])):
            if bd[i][j]==0:
                return (i,j)
    return None
def solve(bd):
    f=isempty(bd)
    if not f:
        return True
  
    else:
        pos=f    
        for n in range(1,10):
            if isvalid(bd,n,pos):
                bd[pos[0]][pos[1]]=n
                if solve(bd):
                    return True
                bd[pos[0]][pos[1]]=0
             
    return False
          
if solve(board)==True:
    printbrd(board)
else: 
    print("Not solvable")

