import pytest
import re
from shapes import SHAPES
from main import get_shape


class TestGetShape:
    # Square Testing
    @pytest.mark.parametrize("shape, topRight, side, expected", [
        ('Square', '1 1', '1', 'Square'),
        ('square', '1 1', '1.1', 'Square'),
        ('SqUaRe', '1 1', '1', 'Square'),
        ('lalala', '1 1', '1', ValueError),
        ('Square', '1 1', 'abc 1', ValueError)
    ])
    def test_get_square(self, monkeypatch, shape, topRight, side, expected):
        inputs_square = iter([shape, topRight, side])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs_square))

        if expected == ValueError:
            if not side.isdigit() and not bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', side)):
                with pytest.raises(expected, match="Value must be a number!"):
                    get_shape(SHAPES)
            else:
                with pytest.raises(expected, match="You entered a wrong shape name!"):
                    get_shape(SHAPES)
        else:
            assert get_shape(SHAPES).__class__.__name__ == expected

    # Triangle Testing
    @pytest.mark.parametrize("shape, point1, point2, point3, expected", [
        ('Triangle', '1 1', '2 2', '5 5', 'Triangle'),
        ('trIanGLe', '1 1', '2 2', '5 5', 'Triangle'),
        ('riangle', '1 1', '2 2', '5 5', ValueError),
    ])
    def test_get_triangle(self, monkeypatch, shape, point1, point2, point3, expected):
        inputs_triangle = iter([shape, point1, point2, point3])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs_triangle))

        if expected == ValueError:
            with pytest.raises(expected, match="You entered a wrong shape name!"):
                get_shape(SHAPES)
        else:
            assert get_shape(SHAPES).__class__.__name__ == expected
