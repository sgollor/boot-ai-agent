from functions.write_file import write_file


def main() -> None:
    cases = [
        ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
        ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        ("calculator", "/tmp/temp.txt", "this should not be allowed"),
    ]

    for working_directory, file_path, content in cases:
        result = write_file(working_directory, file_path, content)
        print(f'write_file("{working_directory}", "{file_path}", "{content}")')
        print(result)
        print()


if __name__ == "__main__":
    main()
