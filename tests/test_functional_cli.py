from typer.testing import CliRunner

from beerlog.cli import main

runner = CliRunner()


def test_add_beer():
    result = runner.invoke(
        main, ["add", "Skol", "KornPA", "--flavor=1", "--image=1", "--cost=2"]
    )
    assert result.exit_code == 0
    assert "beer added" in result.stdout

