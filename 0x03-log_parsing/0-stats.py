#!/usr/bin/python3
"""
Script that parses logs from stdin and prints statistics.
"""

import sys

# Initialize counters
total_file_size = 0
status_codes_count = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}

def print_stats():
    """
    Prints the accumulated statistics of file size and status codes.
    """
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print("{}: {}".format(code, status_codes_count[code]))

# Read log lines from stdin
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Ensure the line contains the expected number of elements
        if len(parts) > 6:
            # Parse file size
            try:
                file_size = int(parts[-1])
                total_file_size += file_size
            except Exception:
                pass

            # Parse status code
            status_code = parts[-2]
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle the Ctrl+C case, print stats
    print_stats()
    raise

# Print final stats after exiting the loop
print_stats()
