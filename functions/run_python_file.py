import os
import shutil
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        try:
            valid_target_file = (
                os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
            )
        except ValueError:
            valid_target_file = False

        if not valid_target_file:
            return (
                f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
            )

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        python_executable = shutil.which("python3") or shutil.which("python")
        if python_executable is None:
            return "Error: Python interpreter not found"

        command = [python_executable, target_file]
        if args:
            command.extend(args)

        completed = subprocess.run(
            command,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30,
        )

        output_parts = []
        if completed.returncode != 0:
            output_parts.append(f"Process exited with code {completed.returncode}")

        if completed.stdout == "" and completed.stderr == "":
            output_parts.append("No output produced")
        else:
            if completed.stdout:
                output_parts.append(f"STDOUT:{completed.stdout}")
            if completed.stderr:
                output_parts.append(f"STDERR:{completed.stderr}")

        return "\n".join(output_parts)
    except Exception as exc:
        return f"Error: executing Python file: {exc}"
