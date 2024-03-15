"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
from counter import Counter
import unittest


class TestCounter(unittest.TestCase):
    """Unittest for counter singleton"""

    def test_count_increment(self):
        """Test counter increment method"""

        # After invoke increment() count must increase by 1
        c = Counter()
        count = c.count
        c.increment()
        self.assertEqual(count + 1, c.count)

        count = c.count

        for i in range(99):
            c.increment()

        self.assertEqual(count + 99, c.count)
        print(c.count)

    def test_is_counter_remain_same_count_after_invoke_constructor_again(self):
        """Counter count must remain the same even after new instance was create"""

        # After create new reference to counter. Count should remain the same
        c1 = Counter()
        count = c1.count
        c2 = Counter()
        self.assertEqual(count, c1.count)
        self.assertEqual(count, c2.count)

    def test_increment_from_different_reference(self):
        """Every counter reference must refer to same counter instance and return same count"""

        c1 = Counter()
        c2 = Counter()

        count = c1.count

        c1.increment()
        self.assertEqual(count + 1, c1.count)
        self.assertEqual(c2.count, c1.count)

        count = c1.count

        for i in range(99):
            c2.increment()
        self.assertEqual(count + 99, c2.count)
        self.assertEqual(c1.count, c2.count)



