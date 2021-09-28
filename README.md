# mkproj

A python script to quickly generate a project directory with boilerplate for a
variety of technologies. Also initialises an empty git repo. Think of it as
`mkdir` on steroids.

### Currently supported targets:

- `c` - A C project. Creates a `Makefile` and `main.c` file.
- `deno` - A deno project. Creates a `Makefile` and `main.ts` file.
- `html5` - An HTML5 static site.
- `node` - Uses `npm init` to initialise your project.
- `py` - A Python project.
- `ts_web` - A webapp that uses TypeScript and esbuild.
- `webapp` - An HTML5/CSS/JS webapp.

### Usage:

```sh
mkproj [-n ProjectName] [-t Target] [other options]
```

### Options:

- `-h`, `--help` shows a help message.
- `-l`, `--license` The name of a license to use.
- `-n',`--name' The name of the project. If this argument is missing mkproj will
  launch in prompt mode.
- `-r`, `--readme` Creates a README file if this option is present.
- `-s`, `--shebang` Adds a shebang for files that support it if this option is
  present.
- `-t`, `--type` The type of project to create. If this option is missing mkproj
  will launch in prompt mode.
- `-T`, `--todo` Creates a TODO file if this option is present.

### Prompt mode:

If mkproj is launched with either no options or either the name or the type
option missing, prompt mode will start, and prompt you for the values of the
various options.

### Installing:

`mkproj` is intended to be installed via a shell alias or script so that you can
supply whatever arguments you prefer to create your default project with.

For example, to create a bash alias that enables readme and todo creation and
generates the MIT license by default:

```bash
echo 'alias mkproj="/path/to/this/repo/mkproj.py -r -t -l MIT"' >> "$HOME"/.bashrc
```

The same example in fish:

<!--Yes, I know fish isn't bash, but syntax highlighting is nice.-->

```bash
alias mkproj='/path/to/this/repo/mkproj.py -r -t -l MIT'
    funcsave mkproj
```

Then you can invoke it with:

```bash
mkproj ProjectName Target
```

Alternatively, create a shell script in a location that's on your `PATH` and
call mkproj within it.

You could also create a symlink to it.

For example, to create a symlink in `$HOME/.local/bin`:

```bash
ln -s /path/to/this/repo/mkproj.py "$HOME"/.local/bin
```

### Contributing:

Feel free to make PRs to add licenses and project types of your own! I'll review
them whenever I can.

---

Copyright © 2021 Siddharth Singh
