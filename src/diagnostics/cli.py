import argparse
import sys

from diagnostics.checks import (
    check_python,
    check_disk,
    check_environment,
    check_developer_tools,
    check_configuration_path
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
    
    parser.add_argument(
        "--config",
        help="Path to the configuration file"
    )

    args = parser.parse_args()

    results = [
        check_python(),
        check_disk(),
        check_environment(),
        check_developer_tools()
    ]
    
    if args.config:
        results.append(check_configuration_path(args.config))

    if args.json:
        print(create_json_report(results))
    else:
        print(create_text_report(results))

    if all(result["status"] == "PASS" for result in results):
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()