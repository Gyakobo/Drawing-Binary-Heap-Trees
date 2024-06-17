from math import ceil, log2

def draw_heap_on_grid(heap):
    if not heap:
        return "Heap is empty"

    # Get the height of the tree
    height_of_tree = ceil(log2(len(heap) + 1))

    # Per a math formula let's get the grid dimensions
    grid_width = (2 ** height_of_tree) * 2 - 1
    grid_height = (height_of_tree*2) - 1

    # Now let's create and fill the grid with empty cells
    # grid: grid_height x grid_width 
    grid = [[" " for _ in range(grid_width)] for _ in range(grid_height)]
    
    # Now let's start placing the nodes in the grid
    def dfs_draw_node(index, current_depth_in_tree, position_in_grid):
        if index >= len(heap):
            return

        grid[current_depth_in_tree * 2][position_in_grid] = str(heap[index]) 

        # Get the left and right children positions
        left_child_position     = position_in_grid - 2 ** (height_of_tree - current_depth_in_tree - 2)
        right_child_position    = position_in_grid + 2 ** (height_of_tree - current_depth_in_tree - 2)

        # Draw connections
        if 2 * index + 1 < len(heap):
            for i in range(1, 2 ** (height_of_tree - current_depth_in_tree - 2)+1):
                grid[current_depth_in_tree * 2 + 1][position_in_grid - i] = "/"
        if 2 * index + 2 < len(heap):
            for i in range(1, 2 ** (height_of_tree - current_depth_in_tree - 2)+1):
                grid[current_depth_in_tree * 2 + 1][position_in_grid + i] = "\\"

        # Now the recursion
        # We shall rerun and recursively place the children
        dfs_draw_node(2 * index + 1, current_depth_in_tree + 1, left_child_position)
        dfs_draw_node(2 * index + 2, current_depth_in_tree + 1, right_child_position)

    # Now let's start with the root node
    dfs_draw_node(0, 0, grid_width // 2)

    # Return the grid
    return "\n".join("".join(row) for row in grid)

heap = [1, 2, 3, 4, 5, 6] * 2 
print(draw_heap_on_grid(heap))

