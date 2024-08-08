import numpy as np
import rasterio
from scipy.ndimage import generic_filter, sobel
import matplotlib.pyplot as plt


def calculate_slope(elevation, resolution):
    dy, dx = np.gradient(elevation, resolution, resolution)
    slope = np.arctan(np.sqrt(dx * dx + dy * dy))
    return np.degrees(slope)


def calculate_aspect(elevation):
    dx, dy = np.gradient(elevation)
    aspect = np.degrees(np.arctan2(-dx, dy))
    return aspect


def calculate_tri(elevation, window_size=3):
    def tri_filter(x):
        center = x[x.size // 2]
        return np.sqrt(np.sum((x - center) ** 2) / x.size)

    return generic_filter(elevation, tri_filter, size=window_size)


def check_elevation(file_path):
    with rasterio.open(file_path) as src:
        elevation = src.read(1)
        print(f"\nElevation stats for {file_path}:")
        print(
            f"Min: {np.min(elevation):.2f}, Max: {np.max(elevation):.2f}, Mean: {np.mean(elevation):.2f}"
        )


def visualize_elevation(file_path):
    with rasterio.open(file_path) as src:
        elevation = src.read(1)
    plt.figure(figsize=(10, 8))
    plt.imshow(elevation, cmap="terrain")
    plt.colorbar(label="Elevation (m)")
    plt.title(f"Elevation Map: {file_path}")
    plt.axis("off")
    plt.show()


def process_section(file_path):
    with rasterio.open(file_path) as src:
        elevation_data = src.read(1)
        resolution = src.res[0]
    print(f"Resolution: {resolution} meters")

    slope = calculate_slope(elevation_data, resolution)
    aspect = calculate_aspect(elevation_data)
    ruggedness = calculate_tri(elevation_data)

    return np.mean(slope), np.mean(aspect), np.mean(ruggedness)


def main():
    sections = [
        "Oregon_Border_to_Packwood",
        "Packwood_to_Ellensburg",
        "Ellensburg_to_Cashmere",
        "Cashmere_to_Chelan",
        "Chelan_to_Conconully",
        "Conconully_to_Canada",
    ]

    for section in sections:
        file_path = f"elevation_{section}.tif"

        check_elevation(file_path)
        visualize_elevation(file_path)

        avg_slope, avg_aspect, avg_ruggedness = process_section(file_path)

        print(f"\nResults for {section.replace('_', ' ')}:")
        print(f"Average Slope: {avg_slope:.2f} degrees")
        print(f"Average Aspect: {avg_aspect:.2f} degrees")
        print(f"Average Terrain Ruggedness Index: {avg_ruggedness:.4f}")


if __name__ == "__main__":
    main()
