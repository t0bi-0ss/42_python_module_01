class Plant:
    """Represents a plant with basic growth metrics."""

    def __init__(self, name: str, height: float = 0, age: int = 0) -> None:
        """Initialize a plant with name, height (cm), and age (days)."""
        if height >= 0 and age >= 0 and name != "":
            self.__name = name
            self.__height = height
            self.__age = age

    def show(self) -> None:
        """Print the plant's information."""
        print(f"{self.__name.capitalize()}: {self.__height:.1f}cm, ", end="")
        print(f"{self.__age} days old")

    def grow(self) -> None:
        """Increment plant's heigth by .8cm"""
        self.__height += 0.8

    def days_passed(self, days: int = 1) -> None:
        """Grow plant according to days passed"""
        if days > 0:
            self.__age += days
            for day in range(1, days + 1):
                self.grow()

    def garden_plant_growth(self, days: int = 0) -> None:
        """Display plant's growth during a given number of days"""
        original_height = self.__height
        if days > 0:
            print("=== Garden Plant Growth ===")
            self.show()
            for day in range(1, days + 1):
                self.days_passed()
                print(f"=== Day {day} ===")
                self.show()
            print(f"Growth this week: {(self.__height - original_height):.1f}")

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print(
                f"{self.__name.capitalize()}: Error, height can't be negative"
            )
            print(
                "Height update rejected"
            )
        else:
            self.__height = new_height
            print(f"Height updated: {self.__height}cm")
    
    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(
                f"{self.__name.capitalize()}: Error, age can't be negative"
            )
            print(
                "Age update rejected"
            )
        else:
            self.__age = new_age
            print(f"Age updated: {self.__age} days")


if __name__ == "__main__":
    print(
        "=== Garden Security System ==="
    )
    plant_1 = Plant("rose", 15, 10)
    print("Plant created: ", end="")
    plant_1.show()
    print()
    plant_1.set_height(25)
    plant_1.set_age(30)
    print()
    plant_1.set_height(-1)
    plant_1.set_age(-1)
    print()
    print("Current state: ", end="")
    plant_1.show()