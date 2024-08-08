import numpy as np
import rasterio
from scipy.ndimage import generic_filter


def calculate_slope(elevation, resolution):
    dx, dy = np.gradient(elevation)
    slope = np.sqrt(dx**2 + dy**2) / resolution
    return np.degrees(np.arctan(slope))


def calculate_aspect(elevation):
    dx, dy = np.gradient(elevation)
    aspect = np.degrees(np.arctan2(-dx, dy))
    return aspect


def calculate_tri(elevation, window_size=3):
    def tri_filter(x):
        center = x[x.size // 2]
        return np.sqrt(np.sum((x - center) ** 2) / x.size)

    return generic_filter(elevation, tri_filter, size=window_size)


def process_section(file_path):
    with rasterio.open(file_path) as src:
        elevation_data = src.read(1)
        resolution = src.res[0]
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
        avg_slope, avg_aspect, avg_ruggedness = process_section(file_path)
        print(f"\nResults for {section.replace('_', ' ')}:")
        print(f"Average Slope: {avg_slope:.2f} degrees")
        print(f"Average Aspect: {avg_aspect:.2f} degrees")
        print(f"Average Terrain Ruggedness Index: {avg_ruggedness:.4f}")


if __name__ == "__main__":
    main()
