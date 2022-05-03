from typer.testing import CliRunner

from beerlog.cli import main

runner = CliRunner()


def test_add_beer():
    result = runner.invoke(
        main, ["add", "Hocus Pocus", "APA", "--flavor=7", "--image=8", "--cost=10"]
    )
    assert result.exit_code == 0
    assert "Beer add to database" in result.stdout
