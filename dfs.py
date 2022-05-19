# creating tree/graph for the dfs 


# graph = {'0': ['1', '2'], '1': ['0', '3', '4'], '3': ['1'], '4': ['2', '3'],'2':['4','0']}

n = int(input('Enter no of nodes: '))

# define dictionary to store tree or graph.
graph = {}


# now iteratively store the inputs in the graph dictionary.
for _ in range(n):
    node = input('Enter value of node : ')
    print("Enter connections: ")
    # here set is used to avoid duplicate entries...
    connections = set(list(map(str,input().split())))
    # storing the entries in the dictionary.
    graph[node] = connections



# to store the visited nodes lets define the visited array. as stack data structure.
visited = []

# now dfs function is defined with parameter graph , start , visited. graph is variable storing dictorinaly
# here start indicate frome where to start traversal in tree or graph. and visited is array
def dfs(graph,start,visited):
    """
    imagined the stack data structure to rescue...
    now according to dfs if present node is not in the stack then append it first and then 
    traverse alone the next nodes which they are connected with .
    so line no 39 to append node in stack and logic behind 41 and 42 is traversing along the next.
    but here comes tricky part ... once the node is visited it will go and append next nodes irrespective
    of the iteration.. once dead end is come.. return to iteration for next node.

    """
    if start not in visited:
        visited.append(start)
        
        for neighbour in graph[start]:
            dfs(graph,neighbour,visited)
    
# calling function 
dfs(graph,'0',visited)
# printing the visited array.
print(visited)


    


