import unittest
import os

class TestFileOpen(unittest.TestCase):
    def setUp(self):
        # Подготовка: создаём временный файл
        self.filename = 'temp_test.txt'
        with open(self.filename, 'w') as f:
            f.write('initial content')

    def tearDown(self):
        # Очистка: удаляем файл после теста
        if os.path.exists(self.filename):
            os.remove(self.filename)
        print(f"Файл {self.filename} удалён")

    def test_write_to_file(self):
        # Тест: пишем в файл
        with open(self.filename, 'a') as f:
            f.write(' added text')
        with open(self.filename, 'r') as f:
            content = f.read()
        self.assertIn('added text', content)

    def test_read_file(self):
        # Тест: читаем файл
        with open(self.filename, 'r') as f:
            content = f.read()
            self.assertEqual(content, 'initial content')

if __name__ == "__main__":
    unittest.main(verbosity=2)