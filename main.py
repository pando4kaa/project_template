from app.io.input import read_from_console, read_from_file_python, read_from_file_pandas
from app.io.output import write_to_console, write_to_file_python


def main():
    # Read from console and process the result
    console_text = read_from_console()
    write_to_console(console_text)
    write_to_file_python("data/console_input.txt", console_text)

    # Read from file
    python_file_text = read_from_file_python("data/sample.txt")
    write_to_console(python_file_text)
    write_to_file_python("data/python_read.txt", python_file_text)

    pandas_data = read_from_file_pandas("input/data.csv")
    write_to_console(str(pandas_data))
    write_to_file_python("data/pandas_read.txt", str(pandas_data))


if __name__ == "__main__":
    main() 