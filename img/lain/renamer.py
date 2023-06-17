import os
import random

# Check that the directory is correct
if not os.getcwd().endswith('img\\lain'):
    print('Please run this script from the img\\lain directory.')
    raise SystemExit(1)

# Rename all files in the directory to a random number in order to prevent naming conflicts
for i, file in enumerate(os.listdir()):
    file_ext = os.path.splitext(file)[1]
    if file_ext != '.py':
        os.rename(file, f'{random.randint(1000000, 9999999999)}{file_ext}')

# Then, sequentially number each file in the directory. Make sure to avoid renaming the script itself.
for i, file in enumerate(os.listdir()):
    file_ext = os.path.splitext(file)[1]
    if file_ext != '.py':
        os.rename(file, f'{i + 1}{file_ext}')