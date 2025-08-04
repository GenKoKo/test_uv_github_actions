"""測試主程式模組."""

import pytest
from click.testing import CliRunner
from src.github_actions_practice.main import cli, hello, fetch


class TestHelloCommand:
    """測試 hello 命令."""

    def test_hello_default(self):
        """測試預設問候."""
        runner = CliRunner()
        result = runner.invoke(hello)
        assert result.exit_code == 0
        assert "Hello World!" in result.output

    def test_hello_with_name(self):
        """測試指定名字的問候."""
        runner = CliRunner()
        result = runner.invoke(hello, ["--name", "Alice"])
        assert result.exit_code == 0
        assert "Hello Alice!" in result.output

    def test_hello_with_count(self):
        """測試重複問候."""
        runner = CliRunner()
        result = runner.invoke(hello, ["--count", "3"])
        assert result.exit_code == 0
        assert result.output.count("Hello World!") == 3


class TestFetchCommand:
    """測試 fetch 命令."""

    def test_fetch_success(self):
        """測試成功取得資料."""
        runner = CliRunner()
        # 使用 httpbin.org 的測試端點
        result = runner.invoke(fetch, ["--url", "https://httpbin.org/json"])
        assert result.exit_code == 0
        assert "處理結果:" in result.output

    def test_fetch_invalid_url(self):
        """測試無效 URL."""
        runner = CliRunner()
        result = runner.invoke(
            fetch, ["--url", "https://invalid-url-that-does-not-exist.com"]
        )
        assert result.exit_code != 0
        assert "錯誤:" in result.output


class TestCLI:
    """測試 CLI 群組."""

    def test_cli_help(self):
        """測試 CLI 說明."""
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "GitHub Actions 練習程式" in result.output
