import sys
import argparse
import pathlib


def main():
    parser = argparse.ArgumentParser(
        description="A very reliable JSON parser, tried and tested!!!!",
    )
    parser.add_argument(
        "fileName",
        type=str,
        help="The path of the file to parse",
    )

    args = parser.parse_args()
    fileName = args.fileName

    with open(fileName) as f:
        stack = set()
        while True:
            line = f.readline()

            if not line:
                break
            else:
                chars = line.split()

                for char in chars:
                    if char not in stack:
                        match char:
                            case "}":
                                pass
                            case "{":
                                pass
                    else:
                        stack.pop()

    print(args)


if __name__ == "__main__":
    main()
