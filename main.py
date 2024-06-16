from math import ceil, log2

def draw_heap_on_grid(heap):

    # Get the height of the tree
    height_of_tree = ceil(log2(len(heap) + 1))

    # Per a math formula let's get the grid dimensions
    grid_height = (height_of_tree*2) - 1
    grid_width = ((2 ** height_of_tree) * 2) - 1

    # Now let's create and fill the grid with empty cells
    # grid: grid_height x grid_width 
    grid = []
    row = [' '] * grid_width 
    for _ in range(grid_height):
        grid.append(row)
    
    # Now let's start placing the nodes in the grid
    def dfs_draw_node(index, current_depth_in_tree, position_in_grid):
        grid[current_depth_in_tree * 2][position_in_grid] = str(heap[index]) 

        # Get the left and right children positions
        left_child_position     = position_in_grid - 2 ** (height_of_tree - current_depth_in_tree - 2)
        right_child_position    = position_in_grid + 2 ** (height_of_tree - current_depth_in_tree - 2)

        # Now the recursion
        # We shall rerun and recursively place the children
        dfs_draw_node(2 * index + 1, current_depth_in_tree + 1, left_child_position)
        dfs_draw_node(2 * index + 2, current_depth_in_tree + 1, right_child_position)

    # Now let's start with the root node

heap = [1, 2, 3, 4, 5, 6]
empty_grid = draw_heap_on_grid(heap)
complete_grid = 

