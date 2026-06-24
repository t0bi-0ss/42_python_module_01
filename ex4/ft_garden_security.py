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
        self._name = name
        self._height = height
        self._age = age
        self._growth_rate = growth_rate

    @property
    def name(self) -> str:
        return self._name

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, new_height: int) -> None:
        if new_height < 0:
            print(f"{self._name.capitalize()}: ", end="")
            print("Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm")

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days")

    @property
    def growth_rate(self) -> float:
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, growth_rate: float) -> None:
        """Set plant's growth rate (cm) per day"""
        if growth_rate <= 0:
            raise ValueError("Error: growth rate must be a positive number")
        self._growth_rate = growth_rate

    def show(self) -> None:
        """Print the plant's information."""
        print(f"{self._name.capitalize()}: {self._height:.1f}cm, ", end="")
        print(f"{self._age} days old")

    def grow(self) -> None:
        """Increment plant's heigth by growth rate"""
        if self._growth_rate == 0:
            print("Error: growth_rate has not been set yet")
            return
        self._height += self._growth_rate

    def age_plant(self, days: int = 1) -> None:
        """Modify plant's age by days passed"""
        if days <= 0:
            print("Error: days must be a positive number")
            return
        self._age += days


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant_1 = Plant("rose", 15, 10)
    print("Plant created: ", end="")
    plant_1.show()
    print()
    plant_1.height = 25
    plant_1.age = 30
    print()
    plant_1.height = -1
    plant_1.age = -1
    print()
    print("Current state: ", end="")
    plant_1.show()
