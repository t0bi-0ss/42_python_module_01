class Plant:
    """Represents a plant with basic growth metrics."""
    class Statistics:
        """Nested class that manages method call counts"""
        def __init__(
                self
        ) -> None:
            self._calls = {"grow": 0, "age": 0, "show": 0}

        def add_call(self, method_name: str) -> None:
            if method_name in self._calls:
                self._calls[method_name] += 1
            else:
                self._calls[method_name] = 1

        def get_call(self, method_name: str) -> int:
            return self._calls[method_name]

    """A decorator to intercept calls"""
    @staticmethod
    def track_call(func):
        def wrapper(self, *args, **kwargs):
            """Increment the count in the nested Statistics instance"""
            self._statistics.add_call(func.__name__)
            return func(self, *args, **kwargs)
        return wrapper

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
            self._name = name
            self._height = height
            self._age = age
            self._growth_rate = growth_rate
            self._statistics = self.Statistics()

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_growth_rate(self) -> float:
        return self._growth_rate

    def set_growth_rate(self, growth_rate: float) -> None:
        """Set plant's growth rate (cm) per day"""
        if growth_rate <= 0:
            print("Error: growth rate must be a positive number")
            return
        self._growth_rate = growth_rate

    @track_call
    def show(self) -> None:
        """Print the plant's information."""
        print(f"{self._name.capitalize()}: {self._height:.1f}cm, ", end="")
        print(f"{self._age} days old")

    @track_call
    def grow(self) -> None:
        """Increment plant's heigth by growth rate"""
        if self._growth_rate == 0:
            print("Error: growth_rate has not been set yet")
            return
        self._height += self._growth_rate

    @track_call
    def age_plant(self, days: int = 1) -> None:
        """Modify plant's age by days passed"""
        if days <= 0:
            print("Error: days must be a positive number")
            return
        self._age += days

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print(f"{self._name.capitalize()}: ", end="")
            print("Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days")

    @staticmethod
    def is_over_year(age: int) -> bool:
        if age <= 0:
            print("Error: age must be a positive number")
            return False
        return age >= 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0, 0)


class Flower(Plant):
    """Represents a plant of type 'flower' with the ability to 'bloom'"""

    def __init__(
        self,
        name: str,
        color: str,
        height: float = 0,
        age: int = 0,
        growth_rate: float = 0
    ) -> None:
        """Initialize flower (Plant) with color"""
        if color == "":
            print("Error: color must not be an empty string")
            return
        super().__init__(name, height, age, growth_rate)
        self._color = color
        self._is_blooming = False

    def set_color(self, color: str) -> None:
        if color == "":
            print("Error: new color must not be an empty string")
            print("Color update failed")
            return
        self._color = color

    def get_color(self) -> str:
        return self._color

    def get_is_blooming(self) -> bool:
        return self._is_blooming

    def show_blooming(self) -> None:
        if self._is_blooming:
            print(f"{(self.get_name()).capitalize()} is blooming beautifully!")
        else:
            print(f"{(self.get_name()).capitalize()} has not bloomed yet")

    def show(self) -> None:
        """Print the flower's information"""
        super().show()
        print(f"Color: {self._color}")
        self.show_blooming()

    def bloom(self) -> None:
        if self._is_blooming:
            print(f"{(self.get_name()).capitalize()} is already blooming")
        else:
            self._is_blooming = True
            print(f"[asking the {self.get_name()} to bloom]")

    def grow_and_bloom(self) -> None:
        self._is_blooming = True
        self.grow()
        print(f"Asking the {self.get_name()} to grow and bloom")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        trunk_diameter: float,
        height: float = 0,
        age: int = 0,
        growth_rate: float = 0
    ) -> None:
        if trunk_diameter <= 0:
            print("Error: trunk diameter must be a positive number")
            return
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter = trunk_diameter
        self._statistics._calls["produce_shade"] = 0

    def set_trunk_diameter(self, trunk_diameter: float) -> None:
        if trunk_diameter <= 0:
            print("Error: trunk diameter must be a positive number")
            return
        self._trunk_diameter = trunk_diameter

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    @Plant.track_call
    def produce_shade(self) -> None:
        print(f"[asking the {self.get_name()} to produce shade]")
        print(
            f"Tree {self.get_name().capitalize()} "
            + "now produces a shade "
            + f"of {self.get_height():.1f}cm long "
            + f"and {self._trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print("Trunk diameter: " + f"{self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        harvest_season: str,
        height: float = 0,
        age: int = 0,
        growth_rate: float = 0,
        nutritional_value: int = 0,
    ) -> None:
        if name == "":
            print("Error: name must not be an empty string")
            return
        if harvest_season == "":
            print("Error: harvest season must not be an empty string")
            return
        if nutritional_value < 0:
            print("Error: nutritional value must not be a negative number")
            return
        super().__init__(name, height, age, growth_rate)
        self._nutritional_value = nutritional_value
        self._harvest_season = harvest_season

    def get_nutritional_value(self) -> int:
        return self._nutritional_value

    def set_nutritional_value(self, nutritional_value: int) -> None:
        if nutritional_value < 0:
            print("Error: nutritional value must not be a negative number")
            return
        self._nutritional_value = nutritional_value

    def get_harvest_season(self) -> str:
        return self._harvest_season

    def set_harvest_season(self, harvest_season: str) -> None:
        if harvest_season == "":
            print("Error: harvest season must not be an empty string")
            return
        self._harvest_season = harvest_season

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def age_and_grow(self, days: int) -> None:
        if days <= 0:
            print("Error: days must be a positive number")
            return
        print(f"[make {self.get_name()} grow and age for {days} days]")
        self.age_plant(days)
        for day in range(1, days + 1):
            super().grow()
            self._nutritional_value += 1


class Seed(Flower):
    def __init__(
        self,
        name: str,
        color: str,
        height: float = 0,
        age: int = 0,
        growth_rate: float = 0
    ) -> None:
        if name == "":
            print("Error: name must not be empty")
            return
        if color == "":
            print("Error: color must not be empty")
            return
        if age < 0 or height < 0:
            print("Error: age and height must not be negative numbers")
        super().__init__(name, color, height, age, growth_rate)
        self._seeds = 0

    def get_seeds(self) -> int:
        return self._seeds

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")

    def grow_age_bloom(self, days: int = 1) -> None:
        """Make seed bloom; grow and age for given number of days"""
        if days <= 0:
            print("Error: days must be a positive number")
            return
        print(f"[make {self.get_name()} grow, age and bloom]")
        super().grow()
        super().age_plant(days)
        self.bloom()


def show_statistics(object: Plant) -> None:
    """Displays statistics for any Plant"""
    print(f"[statistics for {object.get_name()}]")
    print(
        "Stats: "
        + f"{object._statistics.get_call("grow")} grow"
        + f", {object._statistics.get_call("age")} age"
        + f", {object._statistics.get_call("show")} show"
    )
    if "produce_shade" in object._statistics._calls:
        print(
            f"{object._statistics.get_call("produce_shade")} shade"
        )


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print("Is 30 days more than a year? -> ", end="")
    print("%s" % (Plant.is_over_year(30)))
    print("Is 400 days more than a year? -> ", end="")
    print("%s" % (Plant.is_over_year(400)))
    print("\n===Flower")
    flower_1 = Flower("rose", "red", 15, 10, 8)
    flower_1.show()
    show_statistics(flower_1)
    flower_1.grow_and_bloom()
    flower_1.show()
    show_statistics(flower_1)
    print("\n=== Tree")
    tree_1 = Tree("Oak", 5, 200, 365)
    tree_1.show()
    show_statistics(tree_1)
    tree_1.produce_shade()
    show_statistics(tree_1)
    print()
    print("=== Seed")
    seed_1 = Seed("Sunflower", "yellow", 80, 45, 30)
    seed_1.show()
    seed_1.grow_age_bloom(20)
    seed_1.show()
    show_statistics(seed_1)
    print()
    print("=== Anonymous")
    unknown_plant_1 = Plant.anonymous()
    unknown_plant_1.show()
    show_statistics(unknown_plant_1)
