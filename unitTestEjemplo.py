#!/usr/bin/python3
import unittest


class TestAserciones(unittest.TestCase):
    """
    assertEqual(a, b): Verifica si a es igual a b.
    assertNotEqual(a, b): Verifica si a no es igual a b.
    assertAlmostEqual(a, b): Verifica si a es aproximadamente igual a b (util para comparar valores de punto flotante con una tolerancia).
    assertNotAlmostEqual(a, b): Verifica si a no es aproximadamente igual a b.
    assertIs(a, b): Verifica si a es el mismo objeto que b.
    assertIsNot(a, b): Verifica si a no es el mismo objeto que b.
    assertIsNone(x): Verifica si x es None.
    assertIsNotNone(x): Verifica si x no es None.
    assertIn(a, b): Verifica si a está presente en la colección b.
    assertNotIn(a, b): Verifica si a no está presente en la colección b.
    """
    def test_assertEqual(self):
        self.assertEqual(2 + 2, 4)

    def test_assertNotEqual(self):
        self.assertNotEqual(3 * 5, 12)

    def test_assertAlmostEqual(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=5)

    def test_assertNotAlmostEqual(self):
        self.assertNotAlmostEqual(0.1 + 0.2, 0.31, places=5)

    def test_assertIs(self):
        x = [1, 2, 3]
        y = x
        self.assertIs(x, y)

    def test_assertIsNot(self):
        x = [1, 2, 3]
        y = [1, 2, 3]
        self.assertIsNot(x, y)

    def test_assertIsNone(self):
        x = None
        self.assertIsNone(x)

    def test_assertIsNotNone(self):
        x = 5
        self.assertIsNotNone(x)

    def test_assertIn(self):
        items = [1, 2, 3, 4, 5]
        self.assertIn(3, items)

    def test_assertNotIn(self):
        items = [1, 2, 3, 4, 5]
        self.assertNotIn(10, items)


if __name__ == "__main__":
    unittest.main()
