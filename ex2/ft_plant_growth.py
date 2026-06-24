"""
Module that defines a Plant class to track plant growth metrics.
Demonstrates creating and displaying multiple plants.
"""


class Plant:
    """Represents a plant with basic growth metrics."""

    def __init__(
        self,
        name: str,
        height: float = 0,
        age: int = 0,
        growth_rate: float = 0
    ) -> None:
        """Initialize a plant with name, height (cm), age
        (days) and growth rate (cm)."""
        self.name = name
        self.height = height
        self.age = age
        self.growth_rate = growth_rate

    def show(self) -> None:
        """Print the plant's information."""
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, ", end="")
        print(f"{self.age} days old")

    def grow(self) -> None:
        """Increment plant's heigth by growth rate"""
        if self.growth_rate == 0:
            print("Error: growth_rate has not yet been set")
            return
        self.height += self.growth_rate

    def set_growth_rate(self, growth_rate: float) -> None:
        """Set plant's growth rate (cm) per day"""
        if growth_rate <= 0:
            print("Error: growth rate must be a positive number")
            return
        self.growth_rate = growth_rate

    def age_plant(self, days: int = 1) -> None:
        """Modify plant's age by days passed"""
        if days <= 0:
            print("Error: days must be a positive number")
            return
        self.age += days


if __name__ == "__main__":
    plant_1 = Plant("Rose", 25, 30, 0.8)
    original_height = plant_1.height
    print("=== Garden Plant Growth ===")
    plant_1.show()
    for day in range(1, 8):
        plant_1.age_plant()
        plant_1.grow()
        print(f"=== Day {day} ===")
        plant_1.show()
    print(f"Growth this week: {(plant_1.height - original_height):.1f}")
