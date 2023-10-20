#!/usr/bin/python3

"""stdin line by line and computes metrics"""
import sys
import signal

# Variables to store the metrics
total_file_size = 0
status_code_count = {200: 0, 301: 0, 400: 0,
                     401: 0, 403: 0, 404: 0,
                     405: 0, 500: 0}


def handle_interrupt(signal, frame):
    """Function to handle keyboard interruption (CTRL + C)"""
    print_statistics()
    sys.exit(0)


def print_statistics():
    """Function to print the statistics"""
    print("Total file size: File size:", total_file_size)
    for status_code in sorted(status_code_count.keys()):
        count = status_code_count[status_code]
        if count > 0:
            print(status_code, ":", count)


# Register the keyboard interruption handler
signal.signal(signal.SIGINT, handle_interrupt)

try:
    line_count = 0

    # Read input lines from stdin
    for line in sys.stdin:
        line = line.strip()

        # Check if the line matches the expected format
        parts = line.split()
        if len(parts) != 7:
            continue

        ip_address, _, request, status_code, file_size = parts

        # Check if the status code is valid
        if not status_code.isdigit():
            continue

        status_code = int(status_code)
        file_size = int(file_size)

        # Update the metrics
        total_file_size += file_size
        if status_code in status_code_count:
            status_code_count[status_code] += 1

        line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_statistics()


except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    handle_interrupt(signal.SIGINT, None)
