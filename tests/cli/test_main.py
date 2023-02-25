import nxscli
import pytest  # type: ignore
from click.testing import CliRunner
from nxscli.cli.main import main


@pytest.fixture
def runner(mocker):
    mocker.patch.object(nxscli.cli.main, "wait_for_plugins", autospec=True)
    return CliRunner()


def test_main_pnpsave(runner):
    args = ["chan", "1", "pnpsave", "1", "./test"]
    result = runner.invoke(main, args)
    assert result.exit_code == 2

    # args = ["dummy", "pnpsave", "1", "./test"]
    # result = runner.invoke(main, args)
    # assert result.exit_code == 1

    with runner.isolated_filesystem():
        args = ["dummy", "chan", "1", "pnpsave", "1", "./test"]
        result = runner.invoke(main, args)
        assert result.exit_code == 0

    with runner.isolated_filesystem():
        args = ["dummy", "chan", "1", "pnpsave", "1000", "./test"]
        result = runner.invoke(main, args)
        assert result.exit_code == 0

    with runner.isolated_filesystem():
        args = ["dummy", "chan", "5", "pnpsave", "1", "./test"]
        result = runner.invoke(main, args)
        assert result.exit_code == 0


def test_main_pnpmem(runner):
    args = ["chan", "1", "pnpmem", "1", "./test", "100"]
    result = runner.invoke(main, args)
    assert result.exit_code == 2

    # args = ["dummy", "pnpmem", "1", "./test"]
    # result = runner.invoke(main, args)
    # assert result.exit_code == 1

    with runner.isolated_filesystem():
        args = ["dummy", "chan", "1", "pnpmem", "10", "./test", "100"]
        result = runner.invoke(main, args)
        assert result.exit_code == 0

    with runner.isolated_filesystem():
        args = ["dummy", "chan", "1", "pnpmem", "10", "./test", "100"]
        result = runner.invoke(main, args)
        assert result.exit_code == 0

    with runner.isolated_filesystem():
        args = ["dummy", "chan", "5", "pnpmem", "400", "./test", "200"]
        result = runner.invoke(main, args)
        assert result.exit_code == 0
