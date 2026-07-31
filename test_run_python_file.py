from functions.run_python_file import run_python_file


def main() -> None:
    cases = [
        ("calculator", "main.py"),
        ("calculator", "main.py", ["3 + 5"]),
        ("calculator", "tests.py"),
        ("calculator", "../main.py"),
        ("calculator", "nonexistent.py"),
        ("calculator", "lorem.txt"),
    ]

    for case in cases:
        if len(case) == 2:
            working_directory, file_path = case
            result = run_python_file(working_directory, file_path)
            print(f'run_python_file("{working_directory}", "{file_path}")')
        else:
            working_directory, file_path, args = case
            result = run_python_file(working_directory, file_path, args)
            print(f'run_python_file("{working_directory}", "{file_path}", {args})')

        print(result)
        print()


if __name__ == "__main__":
    main()
