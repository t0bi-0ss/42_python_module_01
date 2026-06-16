class Plant:
    """Represents a plant with basic growth metrics."""

    def __init__(self, name: str, height: float = 0, age: int = 0) -> None:
        """Initialize a plant with name, height (cm), and age (days)."""
        if height >= 0 and age >= 0 and name != "":
            self.name = name
            self.height = height
            self.age = age

    def show(self) -> None:
        """Print the plant's information."""
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, ", end="")
        print(f"{self.age} days old")

    def grow(self) -> None:
        """Increment plant's heigth by .8cm"""
        self.height += 0.8

    def days_passed(self, days: int = 1) -> None:
        """Grow plant according to days passed"""
        if days > 0:
            self.age += days
            for day in range(1, days + 1):
                self.grow()

    def garden_plant_growth(self, days: int = 0) -> None:
        """Display plant's growth during a given number of days"""
        original_height = self.height
        if days > 0:
            print("=== Garden Plant Growth ===")
            self.show()
            for day in range(1, days + 1):
                self.days_passed()
                print(f"=== Day {day} ===")
                self.show()
            print(f"Growth this week: {(self.height - original_height):.1f}")


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
