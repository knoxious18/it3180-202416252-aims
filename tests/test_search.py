import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title

class TestSearch(unittest.TestCase):
    def test_search_case_insensitive(self):
        dvds = [DigitalVideoDisc("The Lion King")]
        self.assertEqual(len(search_by_title(dvds, "lion")), 1)

if __name__ == "__main__":
    unittest.main()