from functions.get_files_info import get_files_info


def main() -> None:
    cases = [
        (".", "current directory"),
        ("pkg", "'pkg' directory"),
        ("/bin", "'/bin' directory"),
        ("../", "'../' directory"),
    ]

    for directory, label in cases:
        result = get_files_info("calculator", directory)
        print(f'get_files_info("calculator", "{directory}"):' )
        print(f"Result for {label}:")
        for line in result.splitlines():
            print(f"  {line}")
        print()


if __name__ == "__main__":
    main()
