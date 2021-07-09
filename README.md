# mkproj

A python script to quickly generate a project directory with boilerplate for a variety of technologies.

### Currently supported targets:
* `c` - A C project. Creates a `Makefile` and `main.c` file.
* `deno` - A deno project. Creates a `Makefile` and `main.ts` file.
* `html5` - An HTML5 static site.
* `node` - Uses `npm init` to initialise your project.
* `py` - A Python project.
* `webapp` - An HTML5/CSS/JS webapp.

### Usage:

```sh
    mkproj [options] ProjectName Target
```

### Options:
  * `-h`, `--help`            shows a help message.
  * `-l`, `--license`         The name of a license to use.
  * `-r`, `--readme`          Creates a README file if this option is present.
  * `-s`, `--shebang`         Adds a shebang for files that support it if this option is present.
  * `-t`, `--todo`            Creates a TODO file if this option is present.

### Installing:
`mkproj` is intended to be installed via a shell alias or script so that you can supply whatever arguments you prefer to create your default project with.

In bash, you can create an alias for mkproj with:
```bash
    echo 'alias mkproj="/path/to/this/repo/mkproj.py -r -t -l MIT"' >> $HOME/.bashrc
```

In fish:

<!--Yes, I know fish isn't bash, but syntax highlighting is nice.-->
```bash
    alias mkproj='/path/to/this/repo/mkproj.py -r -t -l MIT'
    funcsave mkproj
```

and invoke it with:
```bash
    mkproj ProjectName Target
```

Alternatively, create a shell script in a location that's on your `PATH` and call mkproj within it.

You could also create a symlink to it:
```bash
    ln -s /path/to/this/repo/mkproj.py "$HOME"/.local/bin
```

### Contributing:

Feel free to make PRs to add licenses and project types of your own! I'll review them whenever I can.

---
Copyright © 2021 Siddharth Singh