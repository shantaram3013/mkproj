import textwrap

types = {
    'html5_static': {
        'files': {
            'index.html': {
                "contents": textwrap.dedent("""\
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Document</title>
                        <link rel='stylesheet' href='style.css'>
                    </head>
                    <body>

                    </body>
                    </html>
                """)
            },
            "style.css": {
                "contents": ""
            },
        },
    },
    'webapp': {
        'files': {
            'index.html': {
                    "contents": textwrap.dedent("""\
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta http-equiv="X-UA-Compatible" content="IE=edge">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>Document</title>
                            <link rel='stylesheet' href='style.css'>
                        </head>
                        <body>
                            <script defer src='main.js'>
                        </body>
                        </html>
                    """),
            },
            "style.css": {
                "contents": ""
            },
            "main.js": {
                "contents": ""
            }
        }
    },
    'py': {
        'files': {
            "main.py": {
                "contents": textwrap.dedent("""\
                    if __name__ == "__main__":
                        pass
                """),
                "shebang": "/usr/bin/env python3"
            },
        }
    },
    'c': {
        'files': {
            "main.c": {
                "contents": textwrap.dedent("""\
                    #include <stdio.h>
                    #include <stdlib.h>

                    int main() {
                        return 0;
                    }
                """)
            },
            "Makefile": {
                "contents": textwrap.dedent("""\
                    NAME = main # filename of the file containing main()
                    CC ?= gcc # C compiler
                    CFLAGS = -Wall -Wextra -Wunreachable-code # Compiler flags we want to use
                    # DEPENDS = dep.o # dependency name, uncomment to use (object files only)
                    # DEPEND_HEADER_FILES = dep.h # header files for dependency building, uncomment to use
                    OUTPUT_FILE = a.out # Filename of the final, compiled executable

                    default: $(NAME)

                    $(NAME): $(NAME).o # $(DEPENDS)
                        $(CC) -o $(OUTPUT_FILE) $(CFLAGS) $(NAME).o # $(DEPENDS)

                    $(NAME).o: $(NAME).c # $(DEPEND_HEADER_FILES) 
                        $(CC) -c $(NAME).c

                    # Add each dependency like this:
                    # dep.o: dep.h dep.c
                    #    $(CC) $(CFLAGS) -c dep.c

                    run: $(NAME)
                        ./$(OUTPUT_FILE)
                """)
            }
        }
    },
}