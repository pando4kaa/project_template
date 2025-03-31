import pytest
import pandas as pd
from app.io.input import read_from_file_python, read_from_file_pandas


@pytest.fixture
def sample_text_file(tmp_path):
    """
    Create a temporary text file with sample content.
    """
    file_path = tmp_path / "test.txt"
    file_path.write_text("Hello, World!\nThis is a test file.")
    return str(file_path)


def test_read_from_file_python_success(sample_text_file):
    content = read_from_file_python(sample_text_file)
    assert content == "Hello, World!\nThis is a test file."


def test_read_from_file_python_not_found():
    content = read_from_file_python("nonexistent.txt")
    assert content == ""


def test_read_from_file_python_invalid_type():
    with pytest.raises(TypeError):
        read_from_file_python(123)
