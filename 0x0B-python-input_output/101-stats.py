import sys

total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for index, line in enumerate(sys.stdin, start=1):
        try:
            _, _, _, status_code, file_size = line.split('"')[2].split()
            status_code = int(status_code)
            file_size = int(file_size)
            total_file_size += file_size
            status_code_counts[status_code] += 1

        except (ValueError, IndexError):
            # Ignore lines that do not match the expected format
            pass

        if index % 10 == 0:
            print(f'Total file size: {total_file_size}')
            for code, count in sorted(status_code_counts.items()):
                if count > 0:
                    print(f'{code}: {count}')
            print()

except KeyboardInterrupt:
    print(f'Total file size: {total_file_size}')
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f'{code}: {count}')

except Exception as e:
    print(f'Error: {e}')

