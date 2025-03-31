def write_to_console(output_text):
    """
    Write text to console.

    Args:
        output_text (str): Text to be written to console.
    """
    print(output_text)


def write_to_file_python(output_file_path, output_text):
    """
    Write text to file using built-in Python capabilities.

    Args:
        output_file_path (str): Path to the output file.
        output_text (str): Text to be written to file.
    """
    try:
        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write(output_text)
    except Exception as e:
        print(f"Error writing to file: {str(e)}")