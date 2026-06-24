"""
Module that defines a Plant class to track plant growth metrics.
Demonstrates creating and displaying multiple plants.
"""


class Plant:
    """Represents a plant with basic growth metrics."""

    def __init__(self, name: str, height: int = 0, age: int = 0) -> None:
        """Initialize a plant with name, height (cm), and age (days)."""
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        """Print the plant's information."""
        print(f"{self.name.capitalize()}: {self.height}cm, ", end="")
        print(f"{self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant_1 = Plant("Rose", 25, 30)
    plant_2 = Plant("Sunflower", 80, 45)
    plant_3 = Plant("Cactus", 15, 120)
    plant_1.show()
    plant_2.show()
    plant_3.show()
