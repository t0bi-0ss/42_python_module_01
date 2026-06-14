"""
Module that defines a Plant class to track plant growth metrics.
Demonstrates creating and displaying multiple plants.
"""


class Plant:
    """Represents a plant with basic growth metrics."""

    def __init__(self, name: str, height: int = 0, age: int = 0) -> None:
        """Initialize a plant with name, height (cm), and age (days)."""
        if height >= 0 and age >= 0 and name != "":
            self.name = name
            self.height = height
            self.age = age

    def show(self) -> None:
        """Print the plant's information."""
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        """Increment plant's heigth by .8cm"""
        self.height += .8

    def age(self, days: int = 1) -> None:
        """Grow plant according to days passed"""
        self.age += days
        for day in range(1, days + 1):
            self.grow()

if __name__ == "__main__":
    