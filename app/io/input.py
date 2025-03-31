import pandas as pd


def read_from_console():
    """
    Read text from console.

    Returns:
        str: Text entered by user from console.
    """
    input_text = input("Enter text: ")

    return input_text


def read_from_file_python(input_file_path):
    """
    Read text from file using built-in Python capabilities.

    Args:
        input_file_path (str): Path to the input file.

    Returns:
        str: Content of the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        TypeError: If input_file_path is not a string.
    """
    if not isinstance(input_file_path, str):
        raise TypeError("input_file_path must be a string")

    try:
        with open(input_file_path, "r", encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
        return ""
    


def read_from_file_pandas(input_file_path):
    """
    Read data from file using pandas library.

    Args:
        input_file_path (str): Path to the input file.

    Returns:
        str: data from a file located in input_file_path.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        TypeError: If input_file_path is not a string.
        ValueError: If the file is empty or has invalid format.
    """
    if not isinstance(input_file_path, str):
        raise TypeError("input_file_path must be a string")

    if not input_file_path:
        raise ValueError("input_file_path cannot be empty")

    if not input_file_path[-4:] == '.csv':
        raise ValueError("The file must have a .csv extension.")

    try:
        df = pd.read_csv(input_file_path)
        if df.empty:
            raise ValueError("The file is empty")
        return df.to_string()
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
        return pd.DataFrame()