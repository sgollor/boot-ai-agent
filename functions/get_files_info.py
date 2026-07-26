import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        try:
            valid_target_dir = (
                os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
            )
        except ValueError:
            valid_target_dir = False

        if not valid_target_dir:
            return (
                f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            )

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        try:
            entries = sorted(os.listdir(target_dir))
        except OSError as exc:
            return f'Error: {exc}'

        lines = []
        for entry in entries:
            entry_path = os.path.join(target_dir, entry)
            try:
                size = os.path.getsize(entry_path)
            except OSError as exc:
                return f'Error: {exc}'

            is_dir = os.path.isdir(entry_path)
            lines.append(f"- {entry}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(lines)
    except Exception as exc:
        return f'Error: {exc}'