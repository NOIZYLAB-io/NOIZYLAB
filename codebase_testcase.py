import os
import pytest
import asyncio
from unittest.mock import patch, MagicMock, AsyncMock
from itertools import chain

import pytest

import builtins

import sys

import types

import time

import concurrent.futures

from contextlib import contextmanager

from typing import AsyncGenerator

# Import the functions from the target module
from BASE.chunkers import codebase as codebase_module


@pytest.fixture
def dummy_file(tmp_path):
    file = tmp_path / "dummy.txt"
    file.write_text("print('hello')")
    return str(file)


@pytest.fixture
def dummy_large_file(tmp_path):
    file = tmp_path / "large.txt"
    file.write_bytes(b"x" * (2 * 1024 * 1024))  # 2MB file
    return str(file)


def test_get_files_needing_update_simple_newer_file(tmp_path):
    file = tmp_path / "file.txt"
    file.write_text("content")
    # Set mtime to a fixed time
    mtime = 1000
    os.utime(file, (mtime, mtime))
    timestamps = {str(file): mtime - 10}
    result = codebase_module.get_files_needing_update_simple([str(file)], timestamps)
    assert str(file) in result


def test_get_files_needing_update_simple_older_file(tmp_path):
    file = tmp_path / "file.txt"
    file.write_text("content")
    mtime = 1000
    os.utime(file, (mtime, mtime))
    timestamps = {str(file): mtime + 10}
    result = codebase_module.get_files_needing_update_simple([str(file)], timestamps)
    assert str(file) not in result


def test_get_files_needing_update_simple_file_not_exists():
    file = "/non/existent/file.txt"
    timestamps = {file: 0}
    result = codebase_module.get_files_needing_update_simple([file], timestamps)
    assert file not in result


def test_get_files_needing_update_simple_oserror(monkeypatch, tmp_path):
    file = tmp_path / "file.txt"
    file.write_text("content")
    def raise_oserror(path):
        raise OSError("fail")
    monkeypatch.setattr(os.path, "getmtime", raise_oserror)
    timestamps = {str(file): 0}
    result = codebase_module.get_files_needing_update_simple([str(file)], timestamps)
    assert str(file) in result


def test_cleanup_stale_timestamps_simple_removes_nonexistent(tmp_path):
    existing_file = tmp_path / "exist.txt"
    existing_file.write_text("content")
    timestamps = {
        str(existing_file): 123,
        "/nonexistent/file.txt": 456,
    }
    result = codebase_module.cleanup_stale_timestamps_simple(timestamps, [str(existing_file)])
    assert str(existing_file) in result
    assert "/nonexistent/file.txt" not in result


def test_update_timestamps_simple_updates(monkeypatch, tmp_path):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file1.write_text("content1")
    file2.write_text("content2")
    mtime1 = 1000
    mtime2 = 2000
    os.utime(file1, (mtime1, mtime1))
    os.utime(file2, (mtime2, mtime2))

    # Patch os.path.getmtime to return fixed values
    monkeypatch.setattr(os.path, "getmtime", lambda path: mtime1 if path == str(file1) else mtime2)
    monkeypatch.setattr(os.path, "exists", lambda path: True)

    result = codebase_module.update_timestamps_simple([str(file1), str(file2)])
    assert result[str(file1)] == mtime1
    assert result[str(file2)] == mtime2


def test_update_timestamps_simple_skips_nonexistent(monkeypatch):
    file = "/nonexistent/file.txt"
    monkeypatch.setattr(os.path, "exists", lambda path: False)
    result = codebase_module.update_timestamps_simple([file])
    assert file not in result


@pytest.mark.asyncio
async def test_process_codebase_chunks_no_files(monkeypatch):
    # Patch get_files to return empty list
    monkeypatch.setattr(codebase_module, "get_files", lambda arg: [])
    result = await codebase_module.process_codebase_chunks([])
    assert result == []


@pytest.mark.asyncio
async def test_process_codebase_chunks_no_updates(monkeypatch):
    # Setup dummy files info with size less than MAX_SIZE
    dummy_files_info = [{"path": "file1.py", "size": 100}]
    monkeypatch.setattr(codebase_module, "get_files", lambda arg: dummy_files_info)
    # Patch get_files_needing_update_simple to return empty list
    monkeypatch.setattr(codebase_module, "get_files_needing_update_simple", lambda files, timestamps: [])
    result = await codebase_module.process_codebase_chunks(["file1.py"])
    assert result == []


@pytest.mark.asyncio
async def test_process_codebase_chunks_success(monkeypatch, tmp_path):
    # Create dummy file
    file = tmp_path / "file1.py"
    file.write_text("print('hello')")
    file_path = str(file)

    # Create dummy chunk data
    dummy_chunks = [{"text": "chunk1", "metadata": {}}]

    # Patch get_files to return file info with size less than MAX_SIZE
    monkeypatch.setattr(codebase_module, "get_files", lambda arg: [{"path": file_path, "size": 100}])

    # Patch get_files_needing_update_simple to return the file path
    monkeypatch.setattr(codebase_module, "get_files_needing_update_simple", lambda files, timestamps: [file_path])

    # Patch make_chunks_from_file to return dummy chunks
    monkeypatch.setattr(codebase_module, "make_chunks_from_file", lambda f: dummy_chunks)

    # Patch update_timestamps_simple to return a dict with updated timestamp
    monkeypatch.setattr(codebase_module, "update_timestamps_simple", lambda files: {file_path: 123456})

    # Patch os.path.getsize to return size
    monkeypatch.setattr(os.path, "getsize", lambda path: 100)

    # Patch os.path.exists to True
    monkeypatch.setattr(os.path, "exists", lambda path: True)

    # Patch ThreadPoolExecutor to run synchronously
    class DummyFuture:
        def __init__(self, result):
            self._result = result
        def result(self):
            return self._result

    class DummyExecutor:
        def __init__(self, max_workers):
            pass
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc_val, exc_tb):
            pass
        def submit(self, fn, arg):
            return DummyFuture(dummy_chunks)

    monkeypatch.setattr(codebase_module, "ThreadPoolExecutor", DummyExecutor)

    # Dummy progress callback
    progress_calls = []
    async def dummy_progress_callback(progress):
        progress_calls.append(progress)

    result = await codebase_module.process_codebase_chunks([file_path], {}, dummy_progress_callback, file_metadata="meta1")

    # The result should be the dummy chunks with metadata added
    assert isinstance(result, list)
    assert len(result) == len(dummy_chunks)
    for chunk in result:
        assert "metadata" in chunk
        assert chunk["metadata"]["file"] == "meta1"

    # Progress callback should be called correct number of times
    assert len(progress_calls) == 1
    assert progress_calls[0] == 100.0 * 0 / 1  # Only one file


@pytest.mark.asyncio
async def test_process_codebase_chunks_partial_failure(monkeypatch, tmp_path):
    file1 = tmp_path / "file1.py"
    file2 = tmp_path / "file2.py"
    file1.write_text("print('hello')")
    file2.write_text("print('fail')")

    file1_path = str(file1)
    file2_path = str(file2)

    dummy_chunks = [{"text": "chunk1", "metadata": {}}]

    monkeypatch.setattr(codebase_module, "get_files", lambda arg: [{"path": file1_path, "size": 100}, {"path": file2_path, "size": 100}])
    monkeypatch.setattr(codebase_module, "get_files_needing_update_simple", lambda files, timestamps: [file1_path, file2_path])

    # Patch make_chunks_from_file to raise on file2
    def make_chunks_side_effect(f):
        if f == file1_path:
            return dummy_chunks
        else:
            raise RuntimeError("fail")

    monkeypatch.setattr(codebase_module, "make_chunks_from_file", make_chunks_side_effect)

    monkeypatch.setattr(codebase_module, "update_timestamps_simple", lambda files: {file1_path: 123456})

    monkeypatch.setattr(os.path, "getsize", lambda path: 100)
    monkeypatch.setattr(os.path, "exists", lambda path: True)

    class DummyFuture:
        def __init__(self, fn, arg):
            self.fn = fn
            self.arg = arg
        def result(self):
            return self.fn(self.arg)

    class DummyExecutor:
        def __init__(self, max_workers):
            pass
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc_val, exc_tb):
            pass
        def submit(self, fn, arg):
            return DummyFuture(fn, arg)

    monkeypatch.setattr(codebase_module, "ThreadPoolExecutor", DummyExecutor)

    progress_calls = []
    async def dummy_progress_callback(progress):
        progress_calls.append(progress)

    result = await codebase_module.process_codebase_chunks([file1_path, file2_path], {}, dummy_progress_callback)

    # The result should only contain chunks from file1
    assert isinstance(result, list)
    assert len(result) == len(dummy_chunks)

    # Progress callback should be called twice (for two files)
    assert len(progress_calls) == 2
    assert progress_calls[-1] == 100.0


@pytest.mark.asyncio
async def test_process_codebase_chunks_no_metadata(monkeypatch, tmp_path):
    file = tmp_path / "file1.py"
    file.write_text("print('hello')")
    file_path = str(file)

    dummy_chunks = [{"text": "chunk1", "metadata": {}}]

    monkeypatch.setattr(codebase_module, "get_files", lambda arg: [{"path": file_path, "size": 100}])
    monkeypatch.setattr(codebase_module, "get_files_needing_update_simple", lambda files, timestamps: [file_path])
    monkeypatch.setattr(codebase_module, "make_chunks_from_file", lambda f: dummy_chunks)
    monkeypatch.setattr(codebase_module, "update_timestamps_simple", lambda files: {file_path: 123456})
    monkeypatch.setattr(os.path, "getsize", lambda path: 100)
    monkeypatch.setattr(os.path, "exists", lambda path: True)

    class DummyFuture:
        def __init__(self, result):
            self._result = result
        def result(self):
            return self._result

    class DummyExecutor:
        def __init__(self, max_workers):
            pass
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc_val, exc_tb):
            pass
        def submit(self, fn, arg):
            return DummyFuture(dummy_chunks)

    monkeypatch.setattr(codebase_module, "ThreadPoolExecutor", DummyExecutor)

    result = await codebase_module.process_codebase_chunks([file_path])

    # The result should be the dummy chunks without metadata modification
    assert isinstance(result, list)
    assert len(result) == len(dummy_chunks)
    for chunk in result:
        # metadata dict should exist but no 'file' key added
        assert "metadata" in chunk
        assert "file" not in chunk["metadata"]


@pytest.mark.asyncio
async def test_process_codebase_chunks_exception(monkeypatch):
    # Patch get_files to raise exception
    def raise_exception(arg):
        raise RuntimeError("fail")

    monkeypatch.setattr(codebase_module, "get_files", raise_exception)

    result = await codebase_module.process_codebase_chunks(["file1.py"])
    assert result == []


def test_update_timestamps_simple_oserror(monkeypatch, tmp_path):
    file = tmp_path / "file.txt"
    file.write_text("content")
    monkeypatch.setattr(os.path, "exists", lambda path: True)
    def raise_oserror(path):
        raise OSError("fail")
    monkeypatch.setattr(os.path, "getmtime", raise_oserror)
    result = codebase_module.update_timestamps_simple([str(file)])
    assert result == {}


def test_cleanup_stale_timestamps_simple_empty():
    timestamps = {"file1": 123, "file2": 456}
    result = codebase_module.cleanup_stale_timestamps_simple(timestamps, [])
    assert result == {}


def test_get_files_needing_update_simple_empty():
    result = codebase_module.get_files_needing_update_simple([], {})
    assert result == []


@pytest.mark.asyncio
async def test_process_codebase_chunks_progress_callback(monkeypatch, tmp_path):
    file = tmp_path / "file1.py"
    file.write_text("print('hello')")
    file_path = str(file)

    dummy_chunks = [{"text": "chunk1", "metadata": {}}]

    monkeypatch.setattr(codebase_module, "get_files", lambda arg: [{"path": file_path, "size": 100}])
    monkeypatch.setattr(codebase_module, "get_files_needing_update_simple", lambda files, timestamps: [file_path])
    monkeypatch.setattr(codebase_module, "make_chunks_from_file", lambda f: dummy_chunks)
    monkeypatch.setattr(codebase_module, "update_timestamps_simple", lambda files: {file_path: 123456})
    monkeypatch.setattr(os.path, "getsize", lambda path: 100)
    monkeypatch.setattr(os.path, "exists", lambda path: True)

    class DummyFuture:
        def __init__(self, result):
            self._result = result
        def result(self):
            return self._result

    class DummyExecutor:
        def __init__(self, max_workers):
            pass
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc_val, exc_tb):
            pass
        def submit(self, fn, arg):
            return DummyFuture(dummy_chunks)

    monkeypatch.setattr(codebase_module, "ThreadPoolExecutor", DummyExecutor)

    progress_calls = []
    async def dummy_progress(progress):
        progress_calls.append(progress)

    result = await codebase_module.process_codebase_chunks([file_path], {}, dummy_progress)
    assert len(progress_calls) == 1
    assert progress_calls[0] == 0.0
    assert result == dummy_chunks


@pytest.mark.asyncio
async def test_process_codebase_chunks_empty_chunks(monkeypatch, tmp_path):
    file = tmp_path / "file1.py"
    file.write_text("print('hello')")
    file_path = str(file)

    monkeypatch.setattr(codebase_module, "get_files", lambda arg: [{"path": file_path, "size": 100}])
    monkeypatch.setattr(codebase_module, "get_files_needing_update_simple", lambda files, timestamps: [file_path])
    monkeypatch.setattr(codebase_module, "make_chunks_from_file", lambda f: [])
    monkeypatch.setattr(codebase_module, "update_timestamps_simple", lambda files: {file_path: 123456})
    monkeypatch.setattr(os.path, "getsize", lambda path: 100)
    monkeypatch.setattr(os.path, "exists", lambda path: True)

    class DummyFuture:
        def __init__(self, result):
            self._result = result
        def result(self):
            return self._result

    class DummyExecutor:
        def __init__(self, max_workers):
            pass
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc_val, exc_tb):
            pass
        def submit(self, fn, arg):
            return DummyFuture([])

    monkeypatch.setattr(codebase_module, "ThreadPoolExecutor", DummyExecutor)

    result = await codebase_module.process_codebase_chunks([file_path])
    assert result == []