from dataclasses import dataclass

"""
Every time a book is checked out or returned at the library, a log entry is created with the ID of the book, and a flag that is true for checkouts or false for returns.

Given an ordered list of log entries, write a function that returns false if: 
  * a book was checked out when it was already checked out
      or
  * a book was returned when it was not checked out.

Assume no books are checked out before the first log entry in the input.
"""

@dataclass()
class LogEntry:
    book_id: int
    is_checkout: bool  # True for checkouts, False for returns

def are_log_entries_valid(log_entries: list[LogEntry]) -> bool:
    h_map = {}

    for log in log_entries:
        print(h_map)
        if log.book_id not in h_map:
            if not log.is_checkout: 
                return False
            h_map[log.book_id] = log.is_checkout
        else:
            if h_map[log.book_id] == log.is_checkout:
                return False
            del h_map[log.book_id]
    return True

test_1 = [LogEntry(1, True), LogEntry(2, True), LogEntry(1, False), LogEntry(1, True)]
assert(are_log_entries_valid(test_1) == True)

test_2 = [LogEntry(1, True), LogEntry(2, True), LogEntry(1, True)]
assert(are_log_entries_valid(test_2) == False)

test_3 = [LogEntry(1, True), LogEntry(2, False), LogEntry(1, True)]
assert(are_log_entries_valid(test_3) == False)

test_4 = [LogEntry(1, True), LogEntry(2, True), LogEntry(1, False), LogEntry(2, False)]
assert(are_log_entries_valid(test_4) == True)

test_5 = [LogEntry(3, True), LogEntry(3, False), LogEntry(3, False)]
assert(are_log_entries_valid(test_5) == False)

test_6 = [LogEntry(1, False), LogEntry(2, True)]
assert(are_log_entries_valid(test_6) == False)

print("Passed")