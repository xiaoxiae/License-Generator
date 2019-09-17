import argparse
import datetime
import os


def get_argument_parser(licenses: [str]):
    """Return the Argument Parser."""
    parser = argparse.ArgumentParser(
        description="A script for generating project licenses."
    )

    parser.add_argument("license", choices=licenses, help="the name of the license")

    parser.add_argument(
        "-a", "--author", dest="author", help="the author(s) of the project"
    )

    parser.add_argument(
        "-y",
        "--year",
        dest="year",
        type=int,
        help="the year; if none is specified, the current year is used",
    )

    parser.add_argument(
        "-d",
        "--description",
        dest="description",
        help="the project description; optional and only used in applicable licenses",
    )

    parser.add_argument(
        "-l",
        "--line-width",
        dest="line_width",
        default=-1,
        type=int,
        help="the maximum number of characters in a line of the exported license "
        + "(disabled by default)",
    )

    parser.add_argument(
        "-i",
        "--include-license-name",
        dest="include_license_name",
        action="store_true",
        help="whether to include the license name at the beginning of the license file",
    )

    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        default="LICENSE",
        help="the name of the output file (defaults to LICENSE)",
    )

    return parser


def wrap_strings(lines: [str], line_width: int):
    """Return a list of strings, wrapped to the specified length."""
    i = 0
    while i < len(lines):
        # if a line is over the limit
        if len(lines[i]) > line_width:
            # (try to) find the rightmost occurrence of a space in the first 80 chars
            try:
                split_index = lines[i][:line_width].rindex(" ")
            except ValueError:
                return None

            # split the line by the found space and add it to the next one
            lines.insert(i + 1, lines[i][split_index + 1 :])
            lines[i] = lines[i][:split_index]

        i += 1

    return lines


# licenses (to give as options)
script_path = os.path.dirname(os.path.abspath(__file__))
templates_folder = os.path.join(script_path, "templates")

licenses = os.listdir(templates_folder)

# get the parser and parse the commands
arguments = get_argument_parser(licenses).parse_args()

# check if an author has been specified
if arguments.author is None:
    exit("No author specified!")

# if the year hasn't been specified, set it to the current one
if arguments.year is None:
    arguments.year = datetime.datetime.now().year

# read the template file
with open(os.path.join(templates_folder, arguments.license), "r") as f:
    contents = f.read()

    # replace the template with contents
    for pattern, replacement in {
        "author": arguments.author,
        "year": arguments.year,
        "description": "" if arguments.description is None else arguments.description,
    }.items():
        contents = contents.replace(f"<<{pattern}>>", str(replacement))

    # split by lines
    contents = contents.splitlines()

    # possibly include license name
    if arguments.include_license_name:
        contents = [f"{arguments.license} License", ""] + contents

    # possibly wrap the contents
    if arguments.line_width >= 0:
        contents = wrap_strings(contents, arguments.line_width)

        if contents is None:
            exit("Line width too low!")

    # remove empty lines at the beginning of the license
    while len(contents[0]) == 0:
        contents.pop(0)

# create the license file
with open(arguments.output, "w") as f:
    f.write("\n".join(contents))
