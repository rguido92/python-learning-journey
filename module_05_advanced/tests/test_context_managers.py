import os
import pytest
from module_05_advanced.project.context_managers import Timer, ManagedFile, ChangeDirectory


class TestTimer:
    def test_measures_time(self):
        with Timer() as timer:
            pass
        assert hasattr(timer, "elapsed")
        assert timer.elapsed >= 0

    def test_works_with_sleep(self):
        import time

        with Timer() as timer:
            time.sleep(0.01)
        assert timer.elapsed >= 0.01


class TestManagedFile:
    def test_reads_content(self, tmp_path):
        file_path = tmp_path / "test.txt"
        file_path.write_text("hello")
        with ManagedFile(str(file_path), "r") as f:
            content = f.read()
        assert content == "hello"

    def test_closes_after_exit(self, tmp_path):
        file_path = tmp_path / "test.txt"
        file_path.write_text("data")
        with ManagedFile(str(file_path), "r") as f:
            pass
        assert f.closed

    def test_writes_content(self, tmp_path):
        file_path = tmp_path / "output.txt"
        with ManagedFile(str(file_path), "w") as f:
            f.write("written")
        assert file_path.read_text() == "written"


class TestChangeDirectory:
    def test_restores_original_dir(self, tmp_path):
        original = os.getcwd()
        with ChangeDirectory(str(tmp_path)):
            assert os.getcwd() == str(tmp_path)
        assert os.getcwd() == original

    def test_returns_new_path(self, tmp_path):
        with ChangeDirectory(str(tmp_path)) as path:
            assert path == str(tmp_path)
