# creating tree/graph for the bfs 


# graph = {'0': ['1', '2'], '1': ['0', '3', '4'], '3': ['1'], '4': ['2', '3'],'2':['4']}

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


# to store the visited nodes lets define the visited array.
visited = []


q = []
# here start indicate frome where to start traversal in tree or graph. and visited is array and q is for queue datastructue (array)
# this is iterative code.
def bfs(graph,start,visited,q):
    """
    at initial phase if start is not in the queue then append it over there 
    Now let's move to iteration part. so base condition for the same is iterate till queue is not empty.
    first pop initial element from queue. and append it over visited stack.
    and traverse through its edges to find next node.
    if node is not in visited. and also not in queue then only append it into the queue.
    and the loop goes continueue untill the terminating condition htis.

    """
    q.append(start)
    while(len(q)!=0):
        element = q.pop(0)
        visited.append(element)
        for node in graph[element]:
            if node not in visited and node not in q:
                q.append(node)


bfs(graph,'0',visited,q)

print(visited)