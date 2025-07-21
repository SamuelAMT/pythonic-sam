# with

"""
The with statement is used to wrap the execution of a block with methods defined by a context manager.
Context managers are used to access files, network connections, database, etc.
Some examples are: __enter__ and __exit__ methods, which are used to set up and tear down resources automatically.
"""

with open("file.txt", "w") as f:
    f.write("Hello") # basic with statement to write to a file


class Dummy:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

with Dummy():
    print("Inside dummy block") # with statement using a manuel context manager


from contextlib import contextmanager

@contextmanager
def dummy_context():
    print("Entering context")
    yield
    print("Exiting context")

with dummy_context():
    print("Inside dummy block") # with statement using equivalent @contextmanager


def write_log(path, text):
    try:
        with open(path, "a") as f:
            f.write(text + "\n")
    except IOError:
        print("Failed to write to file")
    finally:
        print("Log attempt completed")

write_log("app.log", "Server started") # practical use, simulating file access


from contextlib import contextmanager

@contextmanager
def mock_socket():
    print("Connecting to socket")
    yield
    print("Closing socket")

def send_data():
    try:
        with mock_socket():
            print("Sending data to server")
    except Exception:
        print("Failed to send")
    finally:
        print("Finished socket operation")

send_data() # practical use, simulating a network socket connection with @contextmanager


@contextmanager
def mock_db():
    print("Opening DB connection")
    yield
    print("Closing DB connection")

def run_query():
    try:
        with mock_db():
            print("Running SELECT query")
    except Exception:
        print("Query failed")
    finally:
        print("Finished DB access")

run_query() # practical use, simulating a database connection with @contextmanager
