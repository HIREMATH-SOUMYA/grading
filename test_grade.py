import subprocess
import sys

def run_script(args):
    result = subprocess.run(
        [sys.executable, "student_g.py"] + args,
        capture_output=True,
        text=True
    )
    return result


def test_grade_A():
    result = run_script(["Soumya", "90", "95", "92"])

    assert result.returncode == 0
    assert "Grade: A" in result.stdout


def test_grade_B():
    result = run_script(["Soumya", "80", "78", "85"])

    assert result.returncode == 0
    assert "Grade: B" in result.stdout


def test_grade_C():
    result = run_script(["Soumya", "60", "65", "62"])

    assert result.returncode == 0
    assert "Grade: C" in result.stdout


def test_fail_grade():
    result = run_script(["Soumya", "40", "50", "45"])

    assert result.returncode == 0
    assert "Grade: Fail" in result.stdout


def test_missing_arguments():
    result = run_script(["Soumya", "90"])

    assert result.returncode == 1
    assert "Usage: python student_g.py" in result.stdout
