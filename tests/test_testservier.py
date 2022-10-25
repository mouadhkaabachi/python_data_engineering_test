#!/usr/bin/env python

"""Tests for `testservier` package."""

import pytest

from click.testing import CliRunner

from src import cli
from src.common.common import get_config
from src.common.utils import get_top_journals
from src.loader.loader import load_csv_files


@pytest.fixture
def loaded_dataframes():
    config = get_config()
    data_source_folder = config["DATA_SOURCE_FOLDER"]
    return load_csv_files(data_source_folder)


def test_load_csv_files(loaded_dataframes):
    """Test loaded_dataframes function."""
    assert len(loaded_dataframes["drugs"]) > 0
    assert len(loaded_dataframes["clinical_trials"]) > 0
    assert "atccode" in loaded_dataframes["drugs"].columns


def test_get_top_journal():
    """Test loaded_dataframes function."""
    top_journals = get_top_journals("./tests/drug_out_test_file.json")
    assert top_journals[0][0] == "Journal of emergency nursing"


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    help_result = runner.invoke(cli.run_pipeline, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output
