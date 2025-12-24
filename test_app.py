# test_app.py
"""Pytest-based test for app.py."""

import subprocess

def test_key_generation():
    """Verify app.py prints expected key format."""
    result = subprocess.run(
        ["python", "app.py"],
        capture_output=True,
        text=True
    )

    output = result.stdout
    assert "Public Key:" in output
    assert "Private Key:" in output
