import platform
import shutil
import os


def check_python():
    return {
        "name": "Python",
        "version": platform.python_version(),
        "status": "PASS"
    }


def check_disk():
    total, used, free = shutil.disk_usage("/")

    free_gb = free / (1024 ** 3)

    return {
        "name": "Disk Space",
        "free_gb": round(free_gb, 2),
        "status": "PASS" if free_gb >= 5 else "WARN"
    }


def check_environment():
    important_variables = [
        "PATH",
        "TEMP"
    ]

    missing = [
        variable
        for variable in important_variables
        if not os.environ.get(variable)
    ]

    return {
        "name": "Environment Variables",
        "missing": missing,
        "status": "PASS" if not missing else "WARN"
    }
def check_developer_tools():
    tools = ["git", "code"]

    available = []
    missing = []

    for tool in tools:
        if shutil.which(tool):
            available.append(tool)
        else:
            missing.append(tool)

    return {
        "name": "Developer Tools",
        "available": available,
        "missing": missing,
        "status": "PASS" if not missing else "WARN"
    }