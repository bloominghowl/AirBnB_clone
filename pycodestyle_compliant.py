def calculate_area(radius):
    """Calculating the area of a circle."""
    pi = 3.14159
    area = pi * radius ** 2
    return area


def main():
    """Main function to calculates the area of a circle."""
    radius = 5
    area = calculate_area(radius)
    print(f"The area of a circle with radius {radius} is {area:.2f}")


if __name__ == "__main__":
    main()

