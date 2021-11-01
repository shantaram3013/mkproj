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
                    # filename of the file containing main()
                    NAME = main
                    # C compiler
                    CC ?= gcc
                    # Compiler flags we want to use
                    CFLAGS = -Wall -Wextra -Wunreachable-code -g -ggdb
                    # DEPENDS = dep.o # dependency name, uncomment to use (object files only)
                    # DEPEND_HEADER_FILES = dep.h # header files for dependency building, uncomment to use
                    OUTPUT_FILE = a.out # Filename of the final, compiled executable

                    default: $(NAME)

                    $(NAME): $(NAME).o # $(DEPENDS)
                    	$(CC) -o $(OUTPUT_FILE) $(CFLAGS) $(NAME).o

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
        'commands': [['npm', 'init']]
    },
    'ts_node': {
        'commands': [['npm', 'init'], ['npm', 'install', 'tsc']],
        "files": {
            ".gitignore": {
                "contents": textwrap.dedent("""\
                    logs
                    *.log
                    npm-debug.log*
                    yarn-debug.log*
                    yarn-error.log*
                    lerna-debug.log*
                    .pnpm-debug.log*
                    node_modules
                    report.[0-9]*.[0-9]*.[0-9]*.[0-9]*.json
                    pids
                    *.pid
                    *.seed
                    *.pid.lock
                    node_modules/
                    *.npm
                    *.tsbuildinfo
                    *.tgz
                    .env
                    .env.test
                    .env.production
                """)
            }
        }
    },
    'ts_web': {
        'commands': [['npm', 'install', '--save-dev', 'tsc', 'esbuild']],
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
                        <script defer src='dist/main.js'></script>
                    </body>
                    </html>
                """),
            },
            "style.css": {
                "contents": ""
            },
            "src/main.ts": {
                "contents": ""
            },
            "tsconfig.json": {
                "contents": textwrap.dedent("""\
                    {
                        "compilerOptions": {
                            "outDir": "./dist",
                            "allowJs": true,
                            "target": "es6",
                            "noImplicitAny": true,
                            "strictNullChecks": true,
                            "lib": ["ES2020", "DOM"],
                            "module":"ES6",
                            "moduleResolution": "node",
                        },
                        "include": [
                            "./src/**/*"
                        ]
                    }
                    """)
            },
            'esbuild.config.js': {
                'contents': textwrap.dedent("""\
                    require('esbuild').build({
                        entryPoints: ['src/main.ts'],
                        bundle: true,
                        minify: true,
                        outfile: 'dist/main.js'
                    }).catch((err) => {
                        console.error(err)
                        process.exit(1)
                    })
                """)
            },
            "dist/": {},
            '.gitignore': {
                'contents': textwrap.dedent("""\
                    logs
                    *.log
                    npm-debug.log*
                    yarn-debug.log*
                    yarn-error.log*
                    lerna-debug.log*
                    .pnpm-debug.log*
                    node_modules
                    report.[0-9]*.[0-9]*.[0-9]*.[0-9]*.json
                    pids
                    *.pid
                    *.seed
                    *.pid.lock
                    node_modules/
                    *.npm
                    *.tsbuildinfo
                    *.tgz
                    .env
                    .env.test
                    .env.production
                """)
            }
        },
        'message': 'Run `node esbuild.config.js` to develop.'
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
    },
    'rs': {
        'commands': [['cargo', 'init', '--vcs', 'none']],
        "files": {
            ".gitignore": {
                "contents": textwrap.dedent("""\
                    target/
                """)
            }
        }
    },
    'rs_lib': {
        'commands': [['cargo', 'init', '--lib', '--vcs', 'none']],
        "files": {
            ".gitignore": {
                "contents": textwrap.dedent("""\
                    target/
                """)
            }
        }
    }
}
