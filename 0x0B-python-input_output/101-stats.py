#!/usr/bin/python3
"""Read standard input and computes metrics."""


status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
total_size = count = 0
size = 0

def print_stats(size, status_codes):
    """accumulated metrics."""


if __name__ == "__main__":
    import sys

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
