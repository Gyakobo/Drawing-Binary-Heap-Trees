import math

def draw_heap_as_tree(heap):
    if not heap:
        return "Heap is empty"

    # Calculate the height of the tree
    height = math.ceil(math.log2(len(heap) + 1))

    # Grid dimensions
    width = (2 ** height) * 2 - 1  # Ensure enough space for connections
    grid_height = height * 2 - 1
    grid = [[" " for _ in range(width)] for _ in range(grid_height)]

    def place_node(index, depth, pos):
        if index >= len(heap):
            return
        
        grid[depth * 2][pos] = str(heap[index])
        
        # Calculate positions for left and right children
        left_child_pos = pos - 2 ** (height - depth - 2)
        right_child_pos = pos + 2 ** (height - depth - 2)
        
        # Draw connections
        if 2 * index + 1 < len(heap):
            for i in range(1, 2 ** (height - depth - 2)):
                grid[depth * 2 + 1][pos - i] = "/"
        if 2 * index + 2 < len(heap):
            for i in range(1, 2 ** (height - depth - 2)):
                grid[depth * 2 + 1][pos + i] = "\\"
        
        # Place left and right children recursively
        place_node(2 * index + 1, depth + 1, left_child_pos)
        place_node(2 * index + 2, depth + 1, right_child_pos)

    # Start placing nodes from the root
    place_node(0, 0, width // 2)

    # Convert grid to string for display
    return "\n".join("".join(row) for row in grid)

# Example heap
heap = [1, 2, 3, 4, 5, 6]
tree_representation = draw_heap_as_tree(heap)
print(tree_representation)
