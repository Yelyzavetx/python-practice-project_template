import unittest
from unittest.mock import mock_open, patch
import pandas as pd
from app.io.input import read_file_builtin, read_file_with_pandas

class TestFileReading(unittest.TestCase):

    # Tests for the second function read_file_builtin
    @patch("builtins.open", mock_open(read_data="Hello, world!"))
    def test_read_file_builtin_success(self):
        """Test for successful reading from a file"""
        result = read_file_builtin("data/mocked_file.txt")
        self.assertEqual(result, "Hello, world!")

    @patch("builtins.open", mock_open(read_data=""))
    def test_read_file_builtin_empty(self):
        """Test reading from an empty file"""
        result = read_file_builtin("data/mocked_empty_file.txt")
        self.assertEqual(result, "")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_file_builtin_file_not_found(self, mock_file):
        """Test for trying to read a file that doesn't exist"""
        with self.assertRaises(FileNotFoundError):
            read_file_builtin("data/non_existent_file.txt")

    # Tests for the third function read_file_with_pandas
    @patch("pandas.read_csv", return_value=pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]}))
    def test_read_file_with_pandas_success(self, mock_read_csv):
        """Test for successful reading of CSV file with pandas"""
        result = read_file_with_pandas("data/mocked_file.csv")
        expected_result = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})
        pd.testing.assert_frame_equal(result, expected_result)

    @patch("pandas.read_csv", return_value=pd.DataFrame())
    def test_read_file_with_pandas_empty(self, mock_read_csv):
        """Test reading an empty CSV file"""
        result = read_file_with_pandas("data/mocked_empty_file.csv")
        expected_result = pd.DataFrame()
        pd.testing.assert_frame_equal(result, expected_result)

    @patch("pandas.read_csv", side_effect=FileNotFoundError)
    def test_read_file_with_pandas_file_not_found(self, mock_file):
        """Test for trying to read a non-existent CSV file"""
        with self.assertRaises(FileNotFoundError):
            read_file_with_pandas("data/non_existent_file.csv")


if __name__ == "__main__":
    unittest.main()
