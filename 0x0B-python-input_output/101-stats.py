#!/usr/bin/python3
"""Read standard input and computes metrics."""
import sys


status_codes = {
        '200': 0, '301': 0,
        '400': 0, '401': 0,
        '403': 0, '404': 0,
        '405': 0, '500': 0
        }
total_size = count = 0


def print_stats():
    """accumulated metrics."""
    print(f'File size: {total_size}')
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print('{:s}: {:d}'.format(key, value))


try:
    for line in sys.stdin:
        spl = line.split()
        if len(spl) >= 2:
            stats = spl[-2]
            total_size += int(spl[-1])
            if stats in status_codes:
                status_codes[stats] += 1
        count += 1

        if count % 10 == 0:
            print_stats()
    print_stats()
except KeyboardInterrupt as e:
    print_stats()
