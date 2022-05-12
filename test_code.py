from unittest import TestCase, main
from armstrongNumberR import armstrongNumber

class ArmstrongNumberTest(TestCase):
    def test_armstrong_number(self):
        self.assertListEqual(armstrongNumber(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertListEqual(armstrongNumber(100, 200), [153])
        self.assertListEqual(armstrongNumber(1, 1), [1])
    
if __name__ == "__main__":
    main()
    