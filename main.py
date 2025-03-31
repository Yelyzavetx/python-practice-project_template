from app.io.input import input_text_from_console, read_file_builtin, read_file_with_pandas
from app.io.output import output_text_to_console, write_to_file_builtin, write_to_file_with_pandas


def main():

    text = input_text_from_console()
    file_data_builtin = read_file_builtin("data/example.txt")
    file_data_pandas = read_file_with_pandas("data/example.csv")

    #Output
    output_text_to_console(text)
    output_text_to_console(file_data_builtin)
    output_text_to_console(file_data_pandas)


    write_to_file_builtin("data/output.txt", text)
    write_to_file_with_pandas("data/output.csv", file_data_pandas)


if __name__ == "__main__":
    main()
