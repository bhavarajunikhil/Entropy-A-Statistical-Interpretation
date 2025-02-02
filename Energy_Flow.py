import numpy as np
import matplotlib.pyplot as plt
import os

# Create output folder
output_dir = r'D:\Medium\energy_transfer_neighbors'
os.makedirs(output_dir, exist_ok=True)

# Grid setup: 10x16 grid (left = high-energy/red, right = low-energy/blue)
rows, cols = 10, 16
grid = np.zeros((rows, cols), dtype=int)
grid[:, :8] = 0  # Left: High-energy (red)
grid[:, 8:] = 1  # Right: Low-energy (blue)

# Plot setup
fig, ax = plt.subplots(figsize=(8, 5))
cmap = plt.cm.colors.ListedColormap(['red', 'blue'])
ax.set_xticks([])
ax.set_yticks([])
plt.title("Energy Transfer Between Neighbors")

# Save initial state
plt.imshow(grid, cmap=cmap)
plt.savefig(os.path.join(output_dir, 'frame_000.png'))
plt.close()

# Simulation parameters
num_steps = 200  # Total frames to save
swaps_per_step = 50  # Number of neighbor swaps per frame

for step in range(1, num_steps + 1):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xticks([])
    ax.set_yticks([])
    plt.title(f"Step {step}/{num_steps}")
    
    # Perform neighbor swaps
    for _ in range(swaps_per_step):
        # Pick random starting cell
        i, j = np.random.randint(0, rows), np.random.randint(0, cols)
        
        # Choose random direction (up/down/left/right)
        direction = np.random.choice(['up', 'down', 'left', 'right'])
        
        # Find neighbor coordinates
        ni, nj = i, j
        if direction == 'up' and i > 0:
            ni -= 1
        elif direction == 'down' and i < rows-1:
            ni += 1
        elif direction == 'left' and j > 0:
            nj -= 1
        elif direction == 'right' and j < cols-1:
            nj += 1
        else:
            continue  # Skip invalid moves
        
        # Swap energy with neighbor
        grid[i, j], grid[ni, nj] = grid[ni, nj], grid[i, j]
    
    # Save current state
    ax.imshow(grid, cmap=cmap)
    plt.savefig(os.path.join(output_dir, f'frame_{step:03d}.png'))
    plt.close()

print(f"Saved {num_steps + 1} frames to {output_dir}")