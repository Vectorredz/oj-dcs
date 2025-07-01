import numpy as np
SUSCEPTIBLE=5
INFECTED=5
def initialize_grid(size, n_initial_infected=5):

    # TODO: Use sample WITHOUT replacement to ensure unique starting points
    grid_size=int(np.sqrt(size))
    x_random_coord=np.random.choice(grid_size,n_initial_infected) # cells with infected
    y_random_coord=np.random.choice(grid_size,n_initial_infected)
    print(x_random_coord, y_random_coord)
    grid=np.full((grid_size,grid_size), SUSCEPTIBLE)

    # randomizes the susceptible cells with infected individuals
    for i in range(n_initial_infected):
      grid[x_random_coord[i]][y_random_coord[i]]=INFECTED
    infected_count=0

    for i in range(grid_size):
      for j in range(grid_size):
        if grid[i][j]==INFECTED:
          infected_count+=1
    
    assert n_initial_infected==infected_count
    # TODO: Count the number of infected cells manually and ensure it matches n_initial_infected
    return grid


zdef initialize_grid(size, n_initial_infected=5):
    grid_size = int(np.sqrt(size))
    grid = np.full((grid_size, grid_size), SUSCEPTIBLE)

    # Generate all possible coordinates
    all_coords = [(r, c) for r in range(grid_size) for c in range(grid_size)]

    # Randomly sample unique coordinates for infected cells without replacement
    infected_coords = random.sample(all_coords, n_initial_infected)

    # Place infected individuals at the sampled unique coordinates
    for r, c in infected_coords:
        grid[r][c] = INFECTED

    # Count the number of infected cells manually and ensure it matches n_initial_infected
    infected_count = np.sum(grid == INFECTED)

    assert n_initial_infected == infected_count

    return grid
