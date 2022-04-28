from typer.testing import CliRunner
from beerlog.cli import main

runner = CliRunner()


def test_add_beer():
    result = runner.invoke(
        main,
        ["add", "Lagunitas", "IPA", "--flavor=8", "--image=8", "--cost=8"],
    )
    assert result.exit_code == 0
    assert "beer added" in result.stdout
