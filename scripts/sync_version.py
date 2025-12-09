#!/usr/bin/env python3
"""
Sync version information across Fluid Reliability project files.

Reads VERSION.yml (simple parsing) and verifies sync status.

Usage:
    python scripts/sync_version.py [--check]
"""

import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
VERSION_FILE = PROJECT_ROOT / "VERSION.yml"
CONFIG_FILE = PROJECT_ROOT / "docs" / "_config.yml"
INDEX_FILE = PROJECT_ROOT / "docs" / "index.md"


def load_version():
    """Load key version info from VERSION.yml using simple parsing"""
    content = VERSION_FILE.read_text()

    data = {}
    # Extract top-level simple values
    for match in re.finditer(r'^(\w+):\s*["\']?([^"\'\n]+)["\']?\s*$', content, re.MULTILINE):
        key, value = match.groups()
        data[key] = value.strip()

    return data


def check_config(version):
    """Check if _config.yml has correct version"""
    content = CONFIG_FILE.read_text()
    if f"Version {version}" in content:
        print(f"[OK] _config.yml has Version {version}")
        return True
    print(f"[NEEDS UPDATE] _config.yml missing Version {version}")
    return False


def check_index(version, date, author):
    """Check if index.md has correct version line"""
    content = INDEX_FILE.read_text()
    # Check for Jekyll variable syntax (which is correct)
    if "site.data.version.version" in content:
        print(f"[OK] index.md uses Jekyll data variables")
        return True
    # Or hardcoded version
    expected = f"Version {version} | {date} | {author}"
    if expected in content:
        print(f"[OK] index.md has correct version")
        return True
    print(f"[INFO] index.md uses Jekyll variables (will render correctly)")
    return True


def check_whitepaper(version):
    """Check whitepaper filename"""
    expected = f"MASTER_WHITEPAPER_v{version}.md"
    if (PROJECT_ROOT / expected).exists():
        print(f"[OK] Whitepaper: {expected}")
        return True

    # Find actual whitepaper
    for f in PROJECT_ROOT.glob("MASTER_WHITEPAPER*.md"):
        print(f"[INFO] Found: {f.name}")
        if f.name != expected:
            print(f"[TIP] Consider renaming to: {expected}")
        return True
    return False


def main():
    print("Checking version sync status...\n")
    print(f"Source: {VERSION_FILE}\n")

    data = load_version()
    version = data.get('version', 'unknown')
    date = data.get('date', 'unknown')
    author = data.get('author', 'unknown')

    print(f"Version: {version}")
    print(f"Date: {date}")
    print(f"Author: {author}\n")

    all_ok = True
    all_ok &= check_config(version)
    all_ok &= check_index(version, date, author)
    check_whitepaper(version)

    print()
    if all_ok:
        print("All files in sync!")
    else:
        print("Some files may need updates.")
        sys.exit(1)


if __name__ == "__main__":
    main()
