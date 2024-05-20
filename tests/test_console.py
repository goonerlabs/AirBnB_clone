import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def test_handle_unorthodox_commands(self):
        """Test handling of unorthodox commands using dot notation."""
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("User.show(\"1234\")")
            self.assertIn('** no instance found **', f.getvalue())

    def test_handle_nonexistent_class_name(self):
        """Test handling of non-existent class names."""
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("NonExistent.all()")
            self.assertIn('** class doesn\'t exist **', f.getvalue())

    def test_handle_empty_or_incorrect_input(self):
        """Test handling of empty or incorrect input."""
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("")
            self.assertEqual('', f.getvalue().strip())
            console.onecmd("SomeRandomStuff")
            self.assertIn('*** Unknown syntax:', f.getvalue())

if __name__ == '__main__':
    unittest.main()
