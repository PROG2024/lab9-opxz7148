"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import unittest

from circle import Circle


class CircleTest(unittest.TestCase):

    def setUp(self) -> None:
        self.c0 = Circle(0)
        self.c1 = Circle(1.5)
        self.c2 = Circle(2.14)
        self.c3 = Circle(3)
        self.c4 = Circle(4)

    def test_add_area_with_typical_radius_value(self):
        """Test adding area with typical radius value """

        precise = 7

        # Test where both circle has integer radius.
        new_circle = self.c4.add_area(self.c3)
        self.assertAlmostEqual(new_circle.get_area(), self.c4.get_area() + self.c3.get_area(), precise)

        new_circle = self.c3.add_area(self.c4)
        self.assertAlmostEqual(new_circle.get_area(), self.c4.get_area() + self.c3.get_area(), precise)

        # Test where both circle has float radius
        new_circle = self.c1.add_area(self.c2)
        self.assertAlmostEqual(new_circle.get_area(), self.c1.get_area() + self.c2.get_area(), precise)

        new_circle = self.c2.add_area(self.c1)
        self.assertAlmostEqual(new_circle.get_area(), self.c1.get_area() + self.c2.get_area(), precise)

        # Test where one circle has integer radius other circle has float radius
        new_circle = self.c2.add_area(self.c3)
        self.assertAlmostEqual(new_circle.get_area(), self.c2.get_area() + self.c3.get_area(), precise)

        new_circle = self.c3.add_area(self.c2)
        self.assertAlmostEqual(new_circle.get_area(), self.c2.get_area() + self.c3.get_area(), precise)

    def test_adding_circle_that_has_0_radius(self):
        """Edge case: Test adding circle where one of circle has 0 radius"""

        # Test where adding circle with 0 radius and circle with float value  radius
        new_circle = self.c0.add_area(self.c1)
        self.assertEqual(self.c1.get_area(), new_circle.get_area())

        # Test where adding circle with 0 radius and circle with integer value  radius
        new_circle = self.c0.add_area(self.c3)
        self.assertEqual(self.c3.get_area(), new_circle.get_area())

        # Test adding 2 circle with 0 radius
        new_circle = self.c0.add_area(Circle(0))
        self.assertEqual(0, new_circle.get_area())


