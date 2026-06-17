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
        if height >= 0 and age >= 0 and name != "":
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
            print("Error: growth_rate has not been set yet")
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
    plants_list = [
        Plant("rose", 25, 30),
        Plant("oak", 200, 365),
        Plant("cactus", 5, 90),
        Plant("sunflower", 80, 45),
        Plant("fern", 15, 120),
    ]
    print("=== Plant Factory Output ===")
    for plant in plants_list:
        print("Created: ", end="")
        plant.show()
