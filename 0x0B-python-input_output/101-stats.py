#!/usr/bin/python3
"""Read standard input and computes metrics."""


status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
total_size = count = 0


def print_stats():
    """accumulated metrics."""
    print(f'File size: (total_size)')
    for key, val in sorted(status_codes.items()):
        if val > 0:
            print('(:s): (:d)'.format(key, val))


try:
    for line in sys.stdin:
        spl + line.split()
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
