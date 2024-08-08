import numpy as np  # for numerical operations
import rasterio  # for reading geospatial data
from scipy.ndimage import generic_filter  # for applying filters to arrays
import matplotlib.pyplot as plt  # for creating vizzes


# function to calculate slope from elevation data
def calculate_slope(elevation, resolution):
    # calculate gradients in x and y directions
    dy, dx = np.gradient(elevation, resolution, resolution)
    # calculate slope using arctan of gradient magnitude
    slope = np.arctan(np.sqrt(dx * dx + dy * dy))
    # convert slope from radians to degrees
    return np.degrees(slope)


# function to calculate aspect (direction of slope) from elevation data
def calculate_aspect(elevation):
    # calculate gradients in x and y directions
    dx, dy = np.gradient(elevation)
    # calculate aspect using arctan2 and convert to degrees
    aspect = np.degrees(np.arctan2(-dx, dy))
    return aspect


# function to calculate Terrain Ruggedness Index (TRI)
def calculate_tri(elevation, window_size=3):
    # define TRI filter function
    def tri_filter(x):
        # get center value of window
        center = x[x.size // 2]
        # calculate TRI as square root of sum of squared differences
        return np.sqrt(np.sum((x - center) ** 2) / x.size)

    # apply TRI filter to elevation data
    return generic_filter(elevation, tri_filter, size=window_size)


# function to check and print elevation statistics
def check_elevation(file_path):
    with rasterio.open(file_path) as src:
        elevation = src.read(1)  # read first band of the raster
        print(f"\nElevation stats for {file_path}:")
        print(
            f"Min: {np.min(elevation):.2f}, Max: {np.max(elevation):.2f}, Mean: {np.mean(elevation):.2f}"
        )


# function to visualize elevation data
def visualize_elevation(file_path):
    with rasterio.open(file_path) as src:
        elevation = src.read(1)  # read first band of raster
    # create a new figure
    plt.figure(figsize=(10, 8))
    # display elevation data as an image
    plt.imshow(elevation, cmap="terrain")
    plt.colorbar(label="Elevation (m)")
    plt.title(f"Elevation Map: {file_path}")
    plt.axis("off")
    plt.show()


# function to process each section of route
def process_section(file_path):
    with rasterio.open(file_path) as src:
        elevation_data = src.read(1)  # read first band of raster
        resolution = src.res[0]  # get pixel resolution

    # convert resolution from degrees to meters (approx)
    resolution_meters = resolution * 111000  # 1 degree is approximately 111 km
    print(f"Resolution: {resolution_meters:.2f} meters")

    # calculate slope, aspect, and ruggedness
    slope = calculate_slope(elevation_data, resolution_meters)
    aspect = calculate_aspect(elevation_data)
    ruggedness = calculate_tri(elevation_data)

    # return average values and slope array
    return np.mean(slope), np.mean(aspect), np.mean(ruggedness), slope


# function to print sample slope values
def print_sample_slopes(slope):
    print("Sample slope values:")
    # print subset of slope values (every 5th value in both dimensions)
    print(slope[:: slope.shape[0] // 5, :: slope.shape[1] // 5])


# main function to run analysis
def main():
    # define sections of Washington Backcountry Discovery Route
    sections = [
        "Oregon_Border_to_Packwood",
        "Packwood_to_Ellensburg",
        "Ellensburg_to_Cashmere",
        "Cashmere_to_Chelan",
        "Chelan_to_Conconully",
        "Conconully_to_Canada",
    ]

    # process each section
    for section in sections:
        file_path = f"elevation_{section}.tif"

        # check and visualize elevation data
        check_elevation(file_path)
        visualize_elevation(file_path)

        # process section and get results
        avg_slope, avg_aspect, avg_ruggedness, slope = process_section(file_path)

        # print results
        print(f"\nResults for {section.replace('_', ' ')}:")
        print(f"Average Slope: {avg_slope:.2f} degrees")
        print(f"Average Aspect: {avg_aspect:.2f} degrees")
        print(f"Average Terrain Ruggedness Index: {avg_ruggedness:.4f}")

        # print sample slope values
        print_sample_slopes(slope)


# run main function if this script is executed directly
if __name__ == "__main__":
    main()
