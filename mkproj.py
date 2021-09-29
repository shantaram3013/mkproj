#!/usr/bin/env python3

import argparse
import os
import shutil
import subprocess
import sys
import textwrap

from pathlib import Path

from mkproj_licenses import licenses, year
from mkproj_types import types

confirm_string = """\
You have chosen to make a new project with the following options:
    * name: %s
    * type: %s
"""


def delete_path(path):
    try:
        os.remove(path)
    except IsADirectoryError:
        shutil.rmtree(path)
    except PermissionError:
        die(f"Could not remove {path}: permission denied.")


def die(*msg, exitcode=1):
    print(*msg, file=sys.stderr)
    exit(exitcode)


def write_str_to_file(file: str, string: str):
    with open(file, "a+") as fp:
        fp.write(string)


def write_line_to_file(file: str, string: str):
    write_str_to_file(file, string + "\n")


def try_shell_launch():
    init_shell = input_bool("Initialise a shell in the new dir? (yes/no) ")

    if init_shell:
        shell = os.getenv("SHELL")
        if shell:
            subprocess.run([shell])
        else:
            print("Couldn't find your shell, exiting.")
            exit(0)
    else:
        exit(0)


def get_user_input(desc, retry = True):
    rval = ""
    try:
        rval = input(f"Enter {desc}: ")
    except:
        rval = None

    while retry and rval == "":
        try:
            rval = input(f"Enter {desc}: ")
        except:
            rval = None
    return rval


def cancellable_input(prompt):
    try:
        return input(prompt)
    except:
        die("\nCanceled.")

def cancellable_input_graceful(prompt):
    try:
        return input(prompt)
    except:
        return False


def input_bool(prompt):
    try:
        return input(prompt) in ['y', 'yes']
    except:
        return False


def initialise_parser(parser):
    parser.add_argument('-n', '--name', type=str,
                        help='Name of the directory to create.')
    parser.add_argument(
        '-t', '--type', type=str, help='Type of the project to create.', choices=types.keys())
    parser.add_argument('-r', '--readme', action='store_true',
                        help='Creates a README file if this option is present.')
    parser.add_argument('-T', '--todo', action='store_true',
                        help='Creates a TODO file if this option is present.')
    parser.add_argument('-s', '--shebang', action='store_true',
                        help='Adds a shebang for supported files if this option is present.')
    parser.add_argument('-l', '--license', type=str,
                        help='The name of a license to use.', choices=set(licenses.keys()))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Create a new blank project directory with necessary boilerplate.',
        prog='mkproj',
        exit_on_error=True
    )

    initialise_parser(parser)
    args = parser.parse_args()
    lic = args.license

    if not len(sys.argv) > 1 or not args.name or not args.type:
        name = args.name
        if not name:
            name = get_user_input('a name for your project')
            if not name:
                die('Cancelled.')
        t = args.type
        if not t:
            t = get_user_input(
                'a type from [' + ', '.join(types.keys()) + '] for your project'
            )
            if t not in types.keys():
                die('Invalid type selected.')
        readme = args.readme
        if not readme:
            readme = input_bool('Create a readme? (y/N) ')
        todo = args.todo
        if not todo:
            todo = input_bool('Create a todo? (y/N) ')
        shebang = args.shebang
        if not shebang:
            shebang = input_bool('Add shebangs to supported files? (y/N) ')

        if not lic:
            lic = get_user_input(
                    'a license from [' + ', '.join(licenses.keys()) + '] for your project.'
                    '\nLeave empty to skip',
                    False
                )
            if lic != '' and lic not in licenses.keys():
                die('Invalid license selected.')
            elif lic == '':
                pass

        constructed_args = ['-n', name, '-t', t]
        if readme:
            constructed_args.append('-r')
        if todo:
            constructed_args.append('-T')
        if shebang:
            constructed_args.append('-s')
        if lic:
            if lic in licenses.keys():
                constructed_args += ['-l', lic]
            else:
                die('Invalid license selected.')
        args = parser.parse_args(constructed_args)

    args_list = []
    if (args.todo):
        args_list.append('Create todo')
    if (args.readme):
        args_list.append('Create readme')
    if (args.license):
        args_list.append(f'Create license [you picked: {lic}]')
    if (args.shebang):
        args_list.append('Add shebangs to supported files')

    args_string = ''
    if len(args_list) > 0:
        args_string += '    * ' + '\n    * '.join(args_list)

    print((confirm_string + args_string) % (args.name, args.type))
    cnf = input_bool('Is this correct? (y/N): ')
    if not cnf:
        die('Cancelled.')

    proj_dir = os.path.join(os.getcwd(), args.name)

    def get_proj_path(x): return os.path.join(proj_dir, x)

    if os.path.exists(proj_dir):
        overwrite = input_bool(
            "Cannot create project directory: a file or directory with the same name already exists. Try deleting it? (y/N) "
        )
        if not overwrite:
            die('Cancelled.')
        confirm = cancellable_input(
            f'Type "{args.name.replace("/", "")}" (without the quotes) to confirm deletion. THIS CANNOT BE UNDONE! '
        )
        if confirm != args.name:
            die("Canceled.")
        delete_path(proj_dir)

    try:
        os.mkdir(proj_dir)
    except PermissionError:
        die("Cannot create project directory: permission denied.")

    os.chdir(proj_dir)

    subprocess.run(['git', 'init'])

    proj = types[args.type]

    if 'files' in proj:
        for file in proj['files']:
            fobj = proj['files'][file]
            if (file.endswith('/')):
                Path(os.path.join(proj_dir, file)).mkdir(exist_ok=True, parents=True)
                continue
            if os.path.dirname(file) != '':
                Path(os.path.join(proj_dir, os.path.dirname(file))).mkdir(exist_ok=True, parents=True)
            fpath = get_proj_path(file)

            if args.shebang and 'shebang' in fobj:
                write_line_to_file(fpath, fobj['shebang'])

            write_str_to_file(fpath, fobj['contents'])

    if 'commands' in proj:
        for command in proj['commands']:
            subprocess.run(command)

    if args.todo:
        Path(get_proj_path('TODO')).touch()

    if args.readme:
        readme_path = get_proj_path('README.md')
        print("Creating readme...")
        pretty_name = args.name
        desc = get_user_input("a line describing your project") or "Description"

        write_line_to_file(readme_path, f"# {pretty_name}")
        write_line_to_file(readme_path, "")
        write_line_to_file(readme_path, f"{desc}")

    if args.license:
        print("Creating license...")
        name = get_user_input("your name") or "<copyright holders>"
        lic = licenses[args.license]

        for file in lic['files']:
            body_str = textwrap.dedent(lic['files'][file]['contents'])
            if file == "LICENSE":
                try:
                    body_str = body_str.replace("YYYY", year) % name
                except:
                    print("License does not need name field. Proceeding silently.")
            write_str_to_file(get_proj_path(file), body_str)

        print("License created. Be sure to read up on the terms of your license and add headers to each project file!")

    if 'message' in proj:
        print(proj['message'])

    try_shell_launch()
