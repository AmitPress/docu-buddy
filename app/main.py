from nicegui import ui
inp = ui.input("range string")

import re
import itertools

def parse_ranges(input_str):
    tokens = re.split(r'\s*,\s*', input_str.strip())
    ranges = []

    for token in tokens:
        if '-' in token:
            start, end = sorted(map(int, token.split('-')))
        else:
            start = end = int(token)
        ranges.append((start, end))

    # Step 1: Expand all ranges
    all_numbers = set(itertools.chain.from_iterable(range(start, end+1) for start, end in ranges))

    # Step 2: Sort and group into continuous ranges
    sorted_nums = sorted(all_numbers)
    merged_ranges = []
    for k, g in itertools.groupby(enumerate(sorted_nums), lambda x: x[1] - x[0]):
        group = list(g)
        merged_ranges.append((group[0][1], group[-1][1]))

#     return merged_ranges
# def range_print(e):
#     for r in range_extractor(inp.value):
#         for i in r:
#             print(i)
# ui.button("Submit", on_click=range_print)
ui.run()