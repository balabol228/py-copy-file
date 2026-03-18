import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    file_name = parts[1]
    new_file_name = parts[2]

    if file_name == new_file_name or not os.path.isfile(file_name):
        return

    try:
        with open(file_name, "rb") as file_in, open(new_file_name, "wb") as f_out:
            f_out.write(file_in.read())
    except (PermissionError, OSError):
        return
