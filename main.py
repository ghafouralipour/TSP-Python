from sys import maxsize
from itertools import permutations
import numpy as np

def travellingSalesmanProblem(graph, s,V): 
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
 
    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
        # store current Path weight(cost)
        current_pathweight = 0
        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        # update minimum
        min_path = min(min_path, current_pathweight)
    return min_path


menu_options = {
    1: 'Find TSP',
    2: 'Add new Vertex',
    3: 'Print Matrix',
    4: 'Delete a Vertex',
    5: 'Exit',
}

graph_2Darray=[ [0,10,15,20],
                [10,0,35,25],
                [15,35,0,30],
                [20,25,30,0]]

print(len(graph_2Darray))


def print_menu():
    print('================================')
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )
    print('================================')

def option1(graph_2Darray):
     print('You Chose: \'Find TSP 1\'')
     s=0
     V = len(graph_2Darray)
     print('The shortest tour cost: ',travellingSalesmanProblem(graph_2Darray, s,V))

def option2():
    print('Handle option \'Add new vertex\'')
    lst = []
    global graph_2Darray
    n =  len(graph_2Darray)
    # iterating till the range
    print('Insert Cost of eadge to any vertex, if there is no edge, insert 10000.')
    for i in range(0, n):
        print('Cost to vertex: ',i+1)
        ele = int(input())    
        lst.append(ele) # adding the element
    
    column_to_be_added = np.array(lst) 
    # Adding column to numpy array
    graph_2Darray = np.hstack((graph_2Darray, np.atleast_2d(column_to_be_added).T))
    
    lst.append(0)    
    graph_2Darray = np.vstack((graph_2Darray,lst))
    # printing result
    # print ("resultant array", str(graph_2Darray))    
    # print(lst)

def option3(graph_2Darray):
     print('Handle option \'Print Graph\'')
     print(graph_2Darray)

def option4():
    print('Handle option \'Delete Vertices\'')
    global graph_2Darray
    v_list=[]
    n =  len(graph_2Darray)
    for i in range(0, n):
        v_list.append(i+1) # adding the element
    print('Delete vertex candidates are:')
    print(v_list)
    try:
        option = int(input('Enter your Delete vertex choice: '))
        if(option>=2 and option<=n ):
            graph_2Darray = np.delete(graph_2Darray, option-1, 0) # Delete row
            graph_2Darray = np.delete(graph_2Darray, option-1, 1) # Delete row

    except:
        print('Wrong input')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1(graph_2Darray)
        elif option == 2:
            option2()
        elif option == 3:
            option3(graph_2Darray)
        elif option == 4:
            option4()
        
        elif option == 5:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
