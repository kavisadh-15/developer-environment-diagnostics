import argparse
import json

from diagnostics.checks import (
    check_python,
    check_disk,
    check_environment,
    check_developer_tools
)

from diagnostics.report import (
    create_json_report,
    create_text_report
)


def main():
    parser = argparse.ArgumentParser(
        description="Developer Environment Diagnostics Tool"
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Display the report in JSON format"
    )

    args = parser.parse_args()

    results = [
        check_python(),
        check_disk(),
        check_environment(),
        check_developer_tools()
    ]

    if args.json:
        print(create_json_report(results))
    else:
        print(create_text_report(results))


if __name__ == "__main__":
    main()