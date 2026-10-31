# Tuples
import sys

def main():
    coordinates_tuple = (42.376, -71.115)
    latitude, longitude = coordinates_tuple

    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

    coordinates_list = [42.376, -71.115]

    print(sys.getsizeof(coordinates_tuple))
    print(sys.getsizeof(coordinates_list))

main()