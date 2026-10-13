"""
Oefening 4: Dijkstra
=====================
Implementeer Dijkstra voor kortste pad in een gewogen graaf.
"""
import heapq


class State:
    def __init__(self, name):
        self.Name = name


class Node:
    def __init__(self, state):
        self.State = state
        self.Actions = []

    def add_action(self, action):
        self.Actions.append(action)


class Edge:
    def __init__(self, from_node, to_node, cost):
        self.FromNode = from_node
        self.ToNode = to_node
        self.Cost = cost


class Problem:
    def __init__(self):
        self.InitialState = None
        self.GoalState = None

    @staticmethod
    def read_from_file(filepath):
        known_nodes = {}
        with open(filepath, 'r') as file:
            from_node = file.readline().strip()
            to_node = file.readline().strip()
            initial_node = Problem.get_or_create(known_nodes, from_node)
            goal_node = Problem.get_or_create(known_nodes, to_node)

            for line in file:
                line = line.strip()
                node_name, transitions = line.split(": ")
                node = Problem.get_or_create(known_nodes, node_name)
                transitions_arr = transitions.split(" ")
                for i in range(0, len(transitions_arr), 2):
                    t_name = transitions_arr[i]
                    t_cost = float(transitions_arr[i + 1])
                    t_node = Problem.get_or_create(known_nodes, t_name)
                    node.add_action(Edge(node, t_node, t_cost))

        problem = Problem()
        problem.InitialState = initial_node
        problem.GoalState = goal_node
        return problem

    @staticmethod
    def get_or_create(nodes, node_name):
        if node_name in nodes:
            return nodes[node_name]
        node = Node(State(node_name))
        nodes[node_name] = node
        return node


class Path:
    def __init__(self, initial_state):
        self.Nodes = [initial_state]
        self.LeafNode = initial_state
        self.Cost = 0

    def __str__(self):
        node_names = [n.State.Name for n in self.Nodes]
        return "->".join(node_names) + "=" + str(self.Cost)


def dijkstra(problem):
    start_node = problem.InitialState
    goal_node = problem.GoalState
    
    initial_path = Path(start_node)
    
    counter = 0 
    queue = []
    heapq.heappush(queue, (0, counter, start_node, initial_path))
    
    visited_costs = {start_node.State.Name: 0}
    
    while queue:
        current_cost, _, current_node, current_path = heapq.heappop(queue)
        
        if current_node == goal_node:
            return current_path
            
        for edge in current_node.Actions:
            new_node = edge.ToNode
            new_cost = current_cost + edge.Cost
            
            if new_node.State.Name not in visited_costs or new_cost < visited_costs[new_node.State.Name]:
                visited_costs[new_node.State.Name] = new_cost
                
                new_path = Path(start_node)
                new_path.Nodes = current_path.Nodes.copy()
                new_path.Nodes.append(new_node)
                new_path.LeafNode = new_node
                new_path.Cost = new_cost
                
                counter += 1
                heapq.heappush(queue, (new_cost, counter, new_node, new_path))
                
    return None






# Maak een testgraafbestand aan
test_data = """A
H
A: B 2 C 3
B: D 4 E 5
C: F 1
D: H 7
E: H 6
F: H 2
"""
with open("test_graaf.txt", "w") as f:
    f.write(test_data)

problem = Problem.read_from_file("test_graaf.txt")
pad = dijkstra(problem)
print("Kortste pad:", pad)