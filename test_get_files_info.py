from functions.get_files_info import get_files_info


def main() -> None:
    calls = [
        ("calculator", "."),
        ("calculator", "/bin"),
        ("calculator", "../"),
        ("calculator", "main.py"),
    ]

    for working_directory, directory in calls:
        result = get_files_info(working_directory, directory)
        print(f"get_files_info({working_directory!r}, {directory!r}) -> {result}")


if __name__ == "__main__":
    main()
