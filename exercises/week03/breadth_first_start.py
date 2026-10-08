from collections import deque


class State:
    def __init__(self, name):
        self.name = name


class Node:
    def __init__(self, state):
        self.state = state
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)


def breadth_first_search(initial_node, goal_state):
    # Queue voor FIFO (First-In-First-Out) BFS traversal
    queue = deque([initial_node])
    
    # Set om bij te houden welke states al bezocht zijn (vermijdt oneindige loops)
    explored = {initial_node.state.name}
    
    # Dictionary voor parent-tracking om het pad te reconstrueren
    parent = {initial_node: None}

    while queue:
        # Haal de voorste node uit de queue
        current_node = queue.popleft()

        # Check of dit het doel is
        if current_node.state.name == goal_state.name:
            print_path(parent, current_node)
            return current_node

        # Voeg alle onbezochte kinderen toe aan de achterkant van de queue
        for child in current_node.actions:
            if child.state.name not in explored:
                explored.add(child.state.name)
                parent[child] = current_node
                queue.append(child)

    return None


def print_path(parent, goal_node):
    path = []
    current = goal_node
    
    # Loop via de parent-dictionary terug van goal naar start
    while current is not None:
        path.append(current.state.name)
        current = parent.get(current)
    
    # Draai de lijst om zodat hij van start naar goal leest
    path.reverse()
    print("Gevonden pad:", " -> ".join(path))


if __name__ == "__main__":
    # Graaf opbouwen
    state_a = State("A")
    state_b = State("B")
    state_c = State("C")
    state_d = State("D")
    state_e = State("E")
    state_f = State("F")
    state_h = State("H")

    node_a = Node(state_a)
    node_b = Node(state_b)
    node_c = Node(state_c)
    node_d = Node(state_d)
    node_e = Node(state_e)
    node_f = Node(state_f)
    node_h = Node(state_h)

    node_a.add_action(node_b)
    node_a.add_action(node_c)
    node_b.add_action(node_d)
    node_b.add_action(node_e)
    node_c.add_action(node_f)
    node_f.add_action(node_h)

    solution = breadth_first_search(node_a, state_h)
    if solution:
        print("Oplossing gevonden! Doel:", solution.state.name)
    else:
        print("Geen oplossing.")