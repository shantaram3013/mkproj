import textwrap

types = {
    'html5': {
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
                            <script defer src='main.js'></script>
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
                "shebang": "#!/usr/bin/env python3"
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
                    #	$(CC) $(CFLAGS) -c dep.c

                    run: $(NAME)
                    	./$(OUTPUT_FILE)
                """)
            }
        }
    },
    'node': {
        'commands': [['npm', 'init'], ]
    },
    'deno': {
        'files': {
            'main.ts': {
                'contents': ''
            },
            'Makefile': {
                'contents': textwrap.dedent("""\
                    MAKE_OPTIONS = --unstable
                    PERMS = --allow-env --allow-read --allow-write # Deno permissions
                    ENTRYPOINT = main.ts
                    DENO_NAME ?= cyblog # install with DENO_NAME=foo to install under a different name

                    # set DENO_MAKE_EXTRA_OPTIONS in environment to supply extra build options.
                    OPTIONS = $(MAKE_OPTIONS) $(DENO_MAKE_EXTRA_OPTIONS)

                    default: compile

                    dev:
                    	deno run $(PERMS) $(OPTIONS) --watch $(ENTRYPOINT) $(DENO_RUN_OPTIONS)

                    bundle:
                    	deno bundle $(OPTIONS) $(ENTRYPOINT) $(DENO_NAME)

                    compile:
                    	deno compile $(PERMS) $(OPTIONS) $(ENTRYPOINT)

                    install:
                    	deno install $(PERMS) $(OPTIONS) -n $(DENO_NAME)

                    run:
                    	deno run $(PERMS) $(OPTIONS) $(ENTRYPOINT) $(DENO_RUN_OPTIONS)
                """)
            }
        }
    }
}
