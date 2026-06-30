import os
import time


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"Time elapsed: {self.elapsed:.4f}s")
        return False


class ManagedFile:
    def __init__(self, path: str, mode: str = "r"):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self, "file") and self.file:
            self.file.close()
        return False


class ChangeDirectory:
    def __init__(self, new_path: str):
        self.new_path = new_path
        self.original_path = None

    def __enter__(self):
        self.original_path = os.getcwd()
        os.chdir(self.new_path)
        return self.new_path

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.original_path)
        return False
