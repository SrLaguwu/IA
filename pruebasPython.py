class World:
    def __init__(self, grid):
        self.grid = grid
        self.start = None
        self.grogu = None
        self.ship = None
        self.enemies = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    self.start = (i, j)
                elif grid[i][j] == 5:
                    self.grogu = (i, j)
                elif grid[i][j] == 3:
                    self.ship = (i, j)
                elif grid[i][j] == 4:
                    self.enemies.append((i, j))

# Asegurarse de que el combustible de la nave se maneje correctamente
class Agent:
    def __init__(self, world):
        self.world = world
        self.position = world.start
        self.ship_fuel = 10
        self.cost = 0

    def move(self, direction):
        x, y = self.position
        if direction == 'up':
            new_position = (x-1, y)
        elif direction == 'down':
            new_position = (x+1, y)
        elif direction == 'left':
            new_position = (x, y-1)
        elif direction == 'right':
            new_position = (x, y+1)

        if new_position[0] < 0 or new_position[0] >= len(self.world.grid) or new_position[1] < 0 or new_position[1] >= len(self.world.grid[0]):
            return False # No se puede mover fuera de los límites del mundo

        if self.world.grid[new_position[0]][new_position[1]] == 1:
            return False # No se puede mover a un muro
        elif self.world.grid[new_position[0]][new_position[1]] == 4:
            if self.ship_fuel > 0:
                self.ship_fuel -= 1
                self.cost += 0.5
            else:
                self.cost += 5
        else:
            if self.ship_fuel > 0:
                self.ship_fuel -= 1
                self.cost += 0.5
            else:
                self.cost += 1

        self.position = new_position
        return True



from collections import deque

from collections import deque

def bfs(agent):
    queue = deque([(agent.position, agent.cost, agent.ship_fuel)])
    visited = set([agent.position])

    while queue:
        position, cost, fuel = queue.popleft()
        if position == agent.world.grogu:
            return cost

        for direction in ['up', 'down', 'left', 'right']:
            new_agent = Agent(agent.world)
            new_agent.position = position
            new_agent.cost = cost
            new_agent.ship_fuel = fuel
            if new_agent.move(direction):
                if new_agent.position not in visited:
                    visited.add(new_agent.position)
                    # Asegurarse de que el combustible de la nave se maneje correctamente
                    if new_agent.ship_fuel < 0:
                        new_agent.ship_fuel = 0
                    queue.append((new_agent.position, new_agent.cost, new_agent.ship_fuel))

    return -1 # No se encontró a Grogu

# Ejemplo de uso
grid = [
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 5],
    [0, 1, 1, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 4, 4, 4, 0, 1, 0],
    [2, 0, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 4, 4, 0, 0, 1, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 3, 0],
    [1, 1, 1, 0, 0, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
]

world = World(grid)
agent = Agent(world)
print(bfs(agent)) # Debería imprimir el costo total para encontrar a Grogu
