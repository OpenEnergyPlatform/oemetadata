#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2025 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2025 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT

"""
Title: Create latest folder
Description: Copy the current version to the latest folder
"""

# Import
import logging
import os
import re
import shutil

from settings import LATEST_PATH, LOG_FORMAT, VERSION_PATH


# Configuration
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


def clear_latest_folder():
    """Delete latest folder and recreate latest folder."""
    if os.path.exists(LATEST_PATH):
        shutil.rmtree(LATEST_PATH)
    os.makedirs(LATEST_PATH)
    logger.info(f"Clear latest folder: {LATEST_PATH}")


def copy_current_version(source_files):
    """Copies selected files into latest folder."""
    if os.path.exists(LATEST_PATH):
        for file in source_files:
            shutil.copy(VERSION_PATH / file, LATEST_PATH)
        shutil.copy(VERSION_PATH / "example.json", LATEST_PATH)
        shutil.copy(VERSION_PATH / "example.py", LATEST_PATH)
        shutil.copy(VERSION_PATH / "metadata_key_description.md", LATEST_PATH)
        shutil.copy(VERSION_PATH / "README.md", LATEST_PATH)
        shutil.copy(VERSION_PATH / "schema.json", LATEST_PATH)
        shutil.copy(VERSION_PATH / "schema.py", LATEST_PATH)
        shutil.copy(VERSION_PATH / "template.json", LATEST_PATH)
        shutil.copy(VERSION_PATH / "template.py", LATEST_PATH)
    logger.info("Copy files to latest folder.")


def replace_in_files(pattern, replacement):
    """Replaces pattern in all files within latest folder."""
    folder = LATEST_PATH
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            with open(file_path, encoding="utf-8") as f:
                content = f.read()
            content = re.sub(pattern, replacement, content)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
    logger.info(f"Replace {pattern} with {replacement}.")


if __name__ == "__main__":
    logger.info("Create OEMetadata latest version.")
    clear_latest_folder()
    files = {
        "context.json",
        "example.json",
        "example.py",
        "metadata_key_description.md",
        "README.md",
        "schema.json",
        "schema.py",
        "template.json",
        "template.py",
        "__init__.py",
    }
    copy_current_version(files)
    replace_in_files("v2/v20", "latest")
    replace_in_files("V20", "LATEST")
    logger.info("OEMetadata latest version created!")
