class Plant:
    """Represents a plant with basic growth metrics."""

    def __init__(self, name: str, height: float = 0, age: int = 0) -> None:
        """Initialize a plant with name, height (cm), and age (days)."""
        if height >= 0 and age >= 0 and name != "":
            self.__name = name
            self.__height = height
            self.__age = age
        else:
            print("Error: could not initiate class with passed values")

    def get_name(self) -> str:
        return self.__name

    def get_height(self) -> float:
        return self.__height

    def get_age(self) -> int:
        return self.__age

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


class Flower(Plant):
    """Represents a plant of type 'flower' with the ability to 'bloom'"""

    def __init__(
        self,
        name: str,
        color: str,
        height: float = 0,
        age: int = 0,
        is_blooming: bool = False,
    ) -> None:
        """Initialize flower with same data as a plant and with color"""
        if color == "":
            print("Error: color must not be an empty string")
            return
        if not (not is_blooming or is_blooming):
            print("Error: is_blooming must be either True or False")
            return
        super().__init__(name, height, age)
        self.__color = color
        self.__is_blooming = is_blooming

    def set_color(self, color: str) -> None:
        if color == "":
            print("Error: new color must not be an empty string")
            print("Color update failed")
            return
        self.__color = color

    def set_is_blooming(self, is_blooming: bool) -> None:
        if not (not is_blooming or is_blooming):
            print("Error: new is_blooming state must be either True or False")
            print("Blooming state update failed")
            return

    def get_color(self) -> str:
        return self.__color

    def get_is_blooming(self) -> bool:
        return self.__is_blooming

    def show_blooming(self) -> None:
        if self.__is_blooming:
            print(f"{(self.get_name()).capitalize()} is blooming beautifully!")
        else:
            print(f"{(self.get_name()).capitalize()} has not bloomed yet")

    def show(self) -> None:
        """Print the flower's information"""
        super().show()
        print(f"Color: {self.__color}")
        self.show_blooming()

    def bloom(self) -> None:
        if self.__is_blooming:
            print(f"{(self.get_name()).capitalize()} is already blooming")
        else:
            self.__is_blooming = True
            print(f"[asking the {self.get_name()} to bloom]")


class Tree(Plant):
    def __init__(
        self, name: str, trunk_diameter: float, height: float = 0, age: int = 0
    ) -> None:
        if trunk_diameter <= 0:
            print("Error: trunk diameter must be a positive number")
            return
        super().__init__(name, height, age)
        self.__trunk_diameter = trunk_diameter

    def set_trunk_diameter(self, trunk_diameter: float) -> None:
        if trunk_diameter <= 0:
            print("Error: trunk diameter must be a positive number")
            return
        self.__trunk_diameter = trunk_diameter

    def get_trunk_diameter(self) -> float:
        return self.__trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self.get_name()} to produce shade]")
        print(
            f"Tree {self.get_name().capitalize()} "
            + "now produces a shade "
            + "of {self.get_height:.1f}cm long "
            + "and {self.__trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: " + "{self.__trunk_diameter:.1f}cm")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower_1 = Flower("Rose", "red", 15, 10)
    flower_1.show()
    flower_1.bloom()
    flower_1.show()
    
