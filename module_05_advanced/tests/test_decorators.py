import pytest
from unittest.mock import patch
from module_05_advanced.project.decorators import log_call, measure_time, retry


class TestLogCall:
    def test_logs_call_and_return(self, caplog):
        @log_call
        def add(a, b):
            return a + b

        with caplog.at_level("INFO"):
            result = add(2, 3)

        assert result == 5
        assert "Calling add" in caplog.text
        assert "returned 5" in caplog.text

    def test_preserves_function_name(self):
        @log_call
        def my_func():
            pass

        assert my_func.__name__ == "my_func"


class TestMeasureTime:
    def test_logs_execution_time(self, caplog):
        @measure_time
        def fast():
            return 42

        with caplog.at_level("INFO"):
            result = fast()

        assert result == 42
        assert "took" in caplog.text

    def test_preserves_function_name(self):
        @measure_time
        def another():
            pass

        assert another.__name__ == "another"


class TestRetry:
    def test_succeeds_first_time(self):
        @retry(max_attempts=3)
        def always_works():
            return "success"

        assert always_works() == "success"

    def test_fails_all_attempts(self):
        call_count = 0

        @retry(max_attempts=3)
        def always_fails():
            nonlocal call_count
            call_count += 1
            raise ValueError("fail")

        with pytest.raises(ValueError):
            always_fails()
        assert call_count == 3

    def test_succeeds_on_second_attempt(self):
        call_count = 0

        @retry(max_attempts=3)
        def fails_then_works():
            nonlocal call_count
            call_count += 1
            if call_count < 2:
                raise ValueError("not yet")
            return "recovered"

        assert fails_then_works() == "recovered"
        assert call_count == 2

    def test_preserves_function_name(self):
        @retry(max_attempts=3)
        def retry_func():
            pass

        assert retry_func.__name__ == "retry_func"
