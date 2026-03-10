import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def create_iris_image(species_name, filename):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    if species_name == "setosa":
        # Small petals, wide sepals
        colors = ['#FFB6C1', '#FF69B4', '#98FB98', '#90EE90']
        # Petals (small)
        for i, angle in enumerate([0, 90, 180, 270]):
            rad = np.radians(angle)
            x = 5 + 1.5 * np.cos(rad)
            y = 5 + 1.5 * np.sin(rad)
            petal = patches.Ellipse((x, y), 1.2, 0.6, angle=angle, 
                                   color=colors[0], ec='darkred', linewidth=2)
            ax.add_patch(petal)
        # Center
        center = patches.Circle((5, 5), 0.5, color='yellow', ec='orange', linewidth=2)
        ax.add_patch(center)
        ax.text(5, 1, 'Iris Setosa', ha='center', fontsize=20, fontweight='bold', color='#FF1493')
        
    elif species_name == "versicolor":
        # Medium petals
        colors = ['#DDA0DD', '#BA55D3', '#98FB98', '#90EE90']
        for i, angle in enumerate([0, 72, 144, 216, 288]):
            rad = np.radians(angle)
            x = 5 + 2 * np.cos(rad)
            y = 5 + 2 * np.sin(rad)
            petal = patches.Ellipse((x, y), 1.8, 0.8, angle=angle, 
                                   color=colors[1], ec='purple', linewidth=2)
            ax.add_patch(petal)
        center = patches.Circle((5, 5), 0.6, color='#FFD700', ec='orange', linewidth=2)
        ax.add_patch(center)
        ax.text(5, 1, 'Iris Versicolor', ha='center', fontsize=20, fontweight='bold', color='#8B008B')
        
    else:  # virginica
        # Large petals
        colors = ['#9370DB', '#6A5ACD', '#98FB98', '#90EE90']
        for i, angle in enumerate([0, 60, 120, 180, 240, 300]):
            rad = np.radians(angle)
            x = 5 + 2.5 * np.cos(rad)
            y = 5 + 2.5 * np.sin(rad)
            petal = patches.Ellipse((x, y), 2.2, 1, angle=angle, 
                                   color=colors[0], ec='indigo', linewidth=2)
            ax.add_patch(petal)
        center = patches.Circle((5, 5), 0.7, color='gold', ec='orange', linewidth=2)
        ax.add_patch(center)
        ax.text(5, 1, 'Iris Virginica', ha='center', fontsize=20, fontweight='bold', color='#4B0082')
    
    plt.savefig(f'static/{filename}', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

# Generate images
create_iris_image("setosa", "iris_setosa.png")
create_iris_image("versicolor", "iris_versicolor.png")
create_iris_image("virginica", "iris_virginica.png")

print("Flower images created successfully!")
