#!/usr/bin/env python3

import argparse
import shutil
import os
import subprocess
import sys

from pathlib import Path

from mkproj_licenses import licenses
from mkproj_types import types

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
    with open(file, "w+") as fp:
        fp.write(string)

def write_line_to_file(file: str, string: str):
    write_str_to_file(file, string + "\n")

def try_shell_launch():
    init_shell = ""
    try:
        init_shell = input("Initialise a shell in the new dir? (yes/no) ")
    except:
        exit(0)
    if init_shell in ['n', 'no']:
        exit(0)
    else:
        shell = os.getenv("SHELL")
        if shell:
            subprocess.run([shell])
        else:
            print("Couldn't find your shell, exiting.")
            exit(0)

def get_user_input(desc):
    rval = ""
    while rval == "":
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

def initialise_parser(parser):
    parser.add_argument('name', type=str,
                      help='Name of the directory to create.')
    parser.add_argument('type', type=str, help='Type of the project to create.', choices=types.keys())
    parser.add_argument('-r', '--readme', action='store_true',
                      help='Creates a README file if this option is present.')
    parser.add_argument('-t', '--todo', action='store_true',
                      help='Creates a TODO file if this option is present.')
    parser.add_argument('-s', '--shebang', action='store_true',
                      help='Adds a shebang for supported files if this option is present.')
    parser.add_argument('-l', '--license', type=str,
                      help='The name of a license to use.', choices=set(licenses.keys()))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Create a new blank project directory with necessary boilerplate given a technology and its name.',
        prog='mkproj'
    )

    initialise_parser(parser)
    
    args = parser.parse_args()
    proj_dir = os.path.join(os.getcwd(), args.name)
    get_proj_path = lambda x: os.path.join(proj_dir, x)

    if (os.path.exists(proj_dir)):
        overwrite = cancellable_input("Cannot create project directory: a file or directory with the same name already exists. Try deleting it? (yes/no) ")
        if (overwrite in ['y', 'yes']):
            confirm = cancellable_input(f'Type "{args.name.replace("/", "")}" (without the quotes) to confirm deletion. THIS CANNOT BE UNDONE! ')
            if confirm == args.name:
                delete_path(proj_dir)
            else:
                die("Canceled.")
        else:
            die("Canceled.")

    try:
        os.mkdir(proj_dir)
    except PermissionError:
        die("Cannot create project directory: permission denied.")

    os.chdir(proj_dir)

    subprocess.run(['git', 'init'])

    proj = types[args.type]
    for file in proj['files']:
        fobj = proj['files'][file]
        fpath = get_proj_path(file)

        if args.shebang and 'shebang' in fobj:
            write_line_to_file(fpath, fobj['shebang'])
        
        write_str_to_file(fpath, fobj['contents'])

    if args.todo:
        Path(get_proj_path('TODO')).touch()

    if args.readme:
        readme_path = get_proj_path('README.md')
        print("Creating readme...")
        pretty_name = get_user_input("a name for your project") or "Project"
        desc = get_user_input("a line describing your project") or "Description line."
        write_line_to_file(readme_path, f"# {pretty_name}")
        write_line_to_file(readme_path, "")
        write_line_to_file(readme_path, f"{desc}")

    if args.license:
        print("Creating license...")
        name = get_user_input("your name") or "<copyright holders>"
        body = licenses[args.license] % (name,)
        write_str_to_file(get_proj_path('LICENSE'), body)
    
    try_shell_launch()