from diagnostics.checks import (
    check_python,
    check_disk,
    check_environment,
    check_developer_tools,
    check_configuration_path
)


def test_python_check():
    result = check_python()

    assert result["name"] == "Python"
    assert result["status"] == "PASS"


def test_disk_check():
    result = check_disk()

    assert result["name"] == "Disk Space"
    assert "free_gb" in result
    assert result["status"] in ["PASS", "WARN"]


def test_environment_check():
    result = check_environment()

    assert result["name"] == "Environment Variables"
    assert "missing" in result
    assert result["status"] in ["PASS", "WARN"]

def test_developer_tools_check():
    result = check_developer_tools()

    assert result["name"] == "Developer Tools"
    assert "available" in result
    assert "missing" in result
    assert result["status"] in ["PASS", "WARN"]


def test_missing_configuration_path():
    result = check_configuration_path("missing-config.json")

    assert result["name"] == "Configuration Path"
    assert result["status"] == "WARN"
    assert "does not exist" in result["message"]

def test_missing_configuration_path():
    result = check_configuration_path("missing-config.json")

    assert result["name"] == "Configuration Path"
    assert result["status"] == "WARN"
    assert "does not exist" in result["message"]


def test_missing_dependency(monkeypatch):
    monkeypatch.setattr(
        "shutil.which",
        lambda tool: None
    )

    result = check_developer_tools()

    assert result["status"] == "WARN"
    assert "git" in result["missing"]
    assert "code" in result["missing"]