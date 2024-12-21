from collections import deque
d = deque([1, 2, 3])
p = d.popleft()     
d.appendleft(5) 

dl = deque() 
dl.append(5)  
dl.appendleft(0)
dl.extend([6, 7])
dl.extendleft([-2, -1]) 
dl.pop()
dl.popleft()
dl.remove(1)
dl.reverse()

from collections import deque
d = deque(maxlen=3)
d.append(1)  
d.append(2)  
d.append(3)  
d.append(4)

from collections import deque 
def bfs(graph, root):    
    distances = {}   
    distances[root] = 0    
    q = deque([root])    
    while q:    
        current = q.popleft()        
        for neighbor in graph[current]:            
            if neighbor not in distances:                
                distances[neighbor] = distances[current] + 1                
                q.append(neighbor)    
    return distances
graph = {1:[2,3], 2:[4], 3:[4,5], 4:[3,5], 5:[]}
bfs(graph, 1)

