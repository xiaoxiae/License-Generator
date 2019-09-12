# License Generator
A script for generating project licenses.

## Usage
Running `python generate_license.py -h` gives the following:
```terminal
usage: generate_license.py [-h] [-a AUTHOR] [-y YEAR] [-d DESCRIPTION]
                           [-l LINE_WIDTH] [-o OUTPUT]
                           {Apache-2.0,GPLv3,BSD-3-Clause,BSD-2-Clause,MIT}

A script for generating project licenses.

positional arguments:
  {Apache-2.0,GPLv3,BSD-3-Clause,BSD-2-Clause,MIT}
                        the name of the license

optional arguments:
  -h, --help            show this help message and exit
  -a AUTHOR, --author AUTHOR
                        the author(s) of the project
  -y YEAR, --year YEAR  the year; if none is specified, the current year is
                        used
  -d DESCRIPTION, --description DESCRIPTION
                        the project description; optional and only used in
                        applicable licenses
  -l LINE_WIDTH, --line-width LINE_WIDTH
                        the maximum number of characters in a line of the
                        exported license (defaults to 80; is disabled for
                        negative values)
  -o OUTPUT, --output OUTPUT
                        the name of the output file (defaults to LICENSE)
```

## Examples
A MIT license with the name MIT.txt: 
```terminal
python generate_license.py -o=MIT.txt -a="Tomáš Sláma" MIT
```

An Apache-2.0 license wrapped to 60 characters: 
```terminal
python generate_license.py -l=60 -a="Tomáš Sláma" Apache-2.0
```

A GPLv3 license with the year 2008: 
```terminal
python generate_license.py -y=2008 -a="Tomáš Sláma" GPLv3
```
