import json


def create_json_report(results):
    return json.dumps(
        {
            "checks": results
        },
        indent=4
    )


def create_text_report(results):
    lines = []

    lines.append("Developer Environment Health Report")
    lines.append("=" * 40)
    lines.append("")

    for result in results:
        name = result["name"]
        status = result["status"]

        lines.append(f"{name}: {status}")

        for key, value in result.items():
            if key not in ["name", "status"]:
                lines.append(f"  {key}: {value}")

        lines.append("")

    overall_status = (
        "HEALTHY"
        if all(result["status"] == "PASS" for result in results)
        else "NEEDS ATTENTION"
    )

    lines.append(f"Overall Status: {overall_status}")

    return "\n".join(lines)