"""
The test task is to write a program that reads from standard input and writes to standard output.
It receives data about different geometrical 2D shapes. For each of them it should calculate perimeter and area.

Sample input:
Square TopRight 1 1 Side 1
Rectangle TopRight 2 2 BottomLeft 1 1
Circle Center 1 1 Radius 2
Triangle Point1 5 5 Point2 8 8 Point3 10 2

Sample output:
Square Perimeter 4 Area 1
Rectangle Perimeter 4 Area 1
Circle Perimeter 1 Area 2

"""
from shapes import SHAPES, Shape, get_instance


def check_attribute(value: str) -> float:
    try:
        map(lambda num: float(num), value)
        return float(value)
    except ValueError:
        raise ValueError("Value must be a number!")


def get_shape(possible_shapes: dict) -> Shape:
    print(', '.join(possible_shapes.keys()))
    name_shape = input("Enter a name of geometrical shape: ").lower().capitalize()

    if name_shape in possible_shapes.keys():
        attributes = []
        for item in possible_shapes[name_shape]:
            # Remake input to coordinates (x, y)
            value = tuple(map(check_attribute, (input(f'{item}: ').split())))
            attributes.append(value)
        return get_instance(name_shape, tuple(attributes))
    else:
        raise ValueError("You entered a wrong shape name!")


def main():
    while True:
        shape = get_shape(SHAPES)
        result = f'{shape.__class__.__name__} Perimeter: {shape.perimeter()} Area: {shape.area()}\n\n'
        print(result)


if __name__ == "__main__":
    main()
