import os
import psutil


class LockManager:
    """Static class for managing process locks using file-based approach."""

    @staticmethod
    def is_process_alive(pid):
        """Check if a process with the given PID is alive."""
        try:
            process = psutil.Process(pid)
            return process.is_running()
        except (psutil.NoSuchProcess, psutil.AccessDenied, ValueError):
            return False

    @staticmethod
    def get_lock_file_path():
        """Get the path to the lock file."""
        home_dir = os.path.expanduser("~")
        codemate_dir = os.path.join(home_dir, ".codemate")
        os.makedirs(codemate_dir, exist_ok=True)
        return os.path.join(codemate_dir, "codemate.lock")

    @staticmethod
    def acquire_lock():
        """Try to acquire the lock file. Returns True if successful, False if another instance is running."""
        lock_file = LockManager.get_lock_file_path()

        # Check if lock file exists
        if os.path.exists(lock_file):
            try:
                with open(lock_file, "r") as f:
                    old_pid = int(f.read().strip())

                # Check if the process with the old PID is still alive
                if LockManager.is_process_alive(old_pid):
                    print(
                        f"Another instance is already running (PID: {old_pid}). Exiting."
                    )
                    return False
                else:
                    print(
                        f"Found stale lock file for dead process (PID: {old_pid}). Removing."
                    )
                    os.remove(lock_file)
            except (ValueError, IOError) as e:
                print(f"Error reading lock file: {e}. Removing stale lock file.")
                try:
                    os.remove(lock_file)
                except OSError:
                    pass

        # Create/acquire the lock file with current PID
        try:
            with open(lock_file, "w") as f:
                f.write(str(os.getpid()))
            print(f"Lock acquired with PID: {os.getpid()}")
            return True
        except IOError as e:
            print(f"Error creating lock file: {e}")
            return False

    @staticmethod
    def release_lock():
        """Release the lock file."""
        lock_file = LockManager.get_lock_file_path()
        try:
            if os.path.exists(lock_file):
                os.remove(lock_file)
                print("Lock released.")
        except OSError as e:
            print(f"Error releasing lock: {e}")
