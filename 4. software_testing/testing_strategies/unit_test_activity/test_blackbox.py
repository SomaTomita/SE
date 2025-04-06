import unittest

from t9pad import T9Pad


class TestT9Pad(unittest.TestCase):
    def setUp(self):
        self.pad = T9Pad()

    """ ==== module 1 ==== """

    def test_get_key_code(self):
        self.pad.add_key(2, "abc")
        self.pad.add_key(3, "def")
        """
        ex)
        self.pad = {
            2: {"a", "b", "c"},
            3: {"d", "e", "f"},
        }
        """

        # Positive test case to verify that each character is associated with the correct numeric key
        self.assertEqual(2, self.pad.get_key_code("a"))
        self.assertEqual(2, self.pad.get_key_code("b"))
        self.assertEqual(2, self.pad.get_key_code("c"))
        self.assertEqual(3, self.pad.get_key_code("d"))
        self.assertEqual(3, self.pad.get_key_code("e"))
        self.assertEqual(3, self.pad.get_key_code("f"))

    def test_get_key_code_error(self):
        self.pad.add_key(2, "abc")
        self.pad.add_key(3, "def")
        # Negative test case to verify that an error is raised for an invalid character
        with self.assertRaises(ValueError):
            self.pad.get_key_code("z")

    def test_get_pad_letters(self):
        self.pad.add_key(2, "abc")
        self.pad.add_key(3, "def")
        self.pad.add_key(4, "ghi")
        self.pad.add_key(5, "jkl")
        self.pad.add_key(6, "mno")
        self.pad.add_key(7, "pqrs")
        self.pad.add_key(8, "tuv")

        # Test a partially completed numeric pad
        letters = list("abcdefghijklmnopqrstuv")
        # Are all characters in letters registered in pad? (subset)
        self.assertTrue(set(letters).issubset(self.pad.get_pad_letters()))
        # Are all characters in pad registered in letters? (subset)
        self.assertTrue(set(self.pad.get_pad_letters()).issubset(letters))
        # Are all characters in pad and letters the same? (length)
        self.assertEqual(len(letters), len(self.pad.get_pad_letters()))

        # Test a fully completed numeric pad
        # add new key
        self.pad.add_key(9, "wxyz")
        letters = list("abcdefghijklmnopqrstuvwxyz")
        self.assertTrue(set(letters).issubset(self.pad.get_pad_letters()))
        self.assertTrue(set(self.pad.get_pad_letters()).issubset(letters))
        self.assertEqual(len(letters), len(self.pad.get_pad_letters()))

    def test_get_pad_letters_empty(self):
        self.assertTrue(len(self.pad.get_pad_letters()) == 0)

    def test_word_to_t9(self):
        self.pad.add_key(2, "abc")
        self.pad.add_key(3, "def")
        self.pad.add_key(4, "ghi")
        self.pad.add_key(5, "jkl")
        self.pad.add_key(6, "mno")
        self.pad.add_key(7, "pqrs")
        self.pad.add_key(8, "tuv")
        self.pad.add_key(9, "wxyz")

        # check if word1 and word2 have the same key for each letter
        self.assertTrue(self.pad.is_textonym("good", "home"))
        self.assertTrue(self.pad.is_textonym("hood", "home"))
        self.assertTrue(self.pad.is_textonym("good", "hood"))

    def test_word_to_t9_false(self):
        self.pad.add_key(2, "abc")
        self.pad.add_key(3, "def")
        self.pad.add_key(4, "ghi")
        self.pad.add_key(5, "jkl")
        self.pad.add_key(6, "mno")
        self.pad.add_key(7, "pqrs")
        self.pad.add_key(8, "tuv")
        self.pad.add_key(9, "wxyz")

        # check if word1 and word2 have different keys for each letter
        self.assertFalse(self.pad.is_textonym("good", "hogs"))
        self.assertFalse(self.pad.is_textonym("boo", "good"))
        self.assertFalse(self.pad.is_textonym("doly", "doll"))

    """ ==== module 2 ==== """

    def test_init_default(self):
        """Test initialization with no parameters (default empty pad)"""
        default_pad = T9Pad()

        self.assertEqual(set(), default_pad.key_set())
        self.assertEqual([], default_pad.get_pad_letters())
        self.assertEqual("<T9Pad:\n>", str(default_pad))

    def test_init_with_predefined_pad(self):
        """Test initialization with a pre-existing pad dictionary"""
        initial_pad = {2: {"a", "b", "c"}}
        custom_pad = T9Pad(initial_pad)

        self.assertEqual(2, custom_pad.get_key_code("a"))
        self.assertEqual({"a", "b", "c"}, custom_pad._pad[2])

    def test_add_key_validation(self):
        """Test input validation for add_key method"""
        invalid_inputs = [
            (None, "abc"),  # Invalid key
            (2, None),  # Invalid letter string
            (10, "abc"),  # Out of range key (>9)
            (-1, "abc"),  # Out of range key (<0)
        ]

        for key, letters in invalid_inputs:
            with self.assertRaises(ValueError):
                self.pad.add_key(key, letters)

    def test_add_key_duplicate_prevention(self):
        """Test prevention of duplicate letter assignments"""
        self.pad.add_key(2, "abc")

        # Attempt to add a new set containing an existing character
        with self.assertRaises(ValueError):
            self.pad.add_key(3, "aef")  # 'a' already exists

    def test_key_set_functionality(self):
        """Test the key_set method returns correct set of keys"""
        # Test empty pad key set
        self.assertEqual(set(), self.pad.key_set())

        # Test key set after adding keys
        self.pad.add_key(2, "abc")
        self.pad.add_key(5, "jkl")
        self.assertEqual({2, 5}, self.pad.key_set())

    def test_string_representation(self):
        """Test the string representation of T9Pad"""
        # Test string representation of empty pad
        self.assertEqual("<T9Pad:\n>", str(self.pad))

        # Test string representation after adding keys and characters
        self.pad.add_key(2, "abc")
        self.pad.add_key(3, "def")
        expected = "<T9Pad:\n2:abc\n3:def\n>"
        self.assertEqual(expected, str(self.pad))

    def test_word_to_t9_conversion(self):
        """Test direct word to T9 code conversion"""
        self.pad.add_key(2, "abc")
        self.pad.add_key(3, "def")
        self.pad.add_key(4, "ghi")

        # Test conversion of a word to T9 code
        self.assertEqual("234", self.pad.word_to_t9("beg"))

        # Test conversion with non-existent characters
        with self.assertRaises(ValueError):
            self.pad.word_to_t9("xyz")


if __name__ == "__main__":
    unittest.main()
