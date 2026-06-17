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
            self.__name = name
            self.__height = height
            self.__age = age
            self.__growth_rate = growth_rate

    def get_name(self) -> str:
        return self.__name

    def get_height(self) -> float:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def get_growth_rate(self) -> float:
        return self.__growth_rate

    def set_growth_rate(self, growth_rate: float) -> None:
        """Set plant's growth rate (cm) per day"""
        if growth_rate <= 0:
            print("Error: growth rate must be a positive number")
            return
        self.__growth_rate = growth_rate

    def show(self) -> None:
        """Print the plant's information."""
        print(f"{self.__name.capitalize()}: {self.__height:.1f}cm, ", end="")
        print(f"{self.__age} days old")

    def grow(self) -> None:
        """Increment plant's heigth by growth rate"""
        if self.__growth_rate == 0:
            print("Error: growth_rate has not been set yet")
            return
        self.__height += self.__growth_rate

    def age_plant(self, days: int = 1) -> None:
        """Modify plant's age by days passed"""
        if days <= 0:
            print("Error: days must be a positive number")
            return
        self.__age += days

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print(f"{self.__name.capitalize()}: ", end="")
            print("Error, height can't be negative")
            print("Height update rejected")
        else:
            self.__height = new_height
            print(f"Height updated: {self.__height}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.__name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.__age = new_age
            print(f"Age updated: {self.__age} days")


if __name__ == "__main__":
    print("=== Garden Security System ===")
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
