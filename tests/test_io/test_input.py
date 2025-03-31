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


@pytest.fixture
def sample_csv_file(tmp_path):
    """
    Create a temporary CSV file with sample data.
    """
    file_path = tmp_path / "test.csv"
    df = pd.DataFrame({
        'name': ['John', 'Jane'],
        'age': [30, 25]
    })
    df.to_csv(file_path, index=False)
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


def test_read_from_file_pandas_success(sample_csv_file):
    content = read_from_file_pandas(sample_csv_file)
    assert "John" in content
    assert "Jane" in content
    assert "30" in content
    assert "25" in content


def test_read_from_file_pandas_not_found():
    content = read_from_file_pandas("nonexistent.csv")
    assert isinstance(content, pd.DataFrame)
    assert content.empty


def test_read_from_file_pandas_invalid_extension():
    with pytest.raises(ValueError, match="The file must have a .csv extension."):
        read_from_file_pandas("test.txt")
