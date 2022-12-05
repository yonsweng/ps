from glob import glob
from sys import argv
import os

problem_num = argv[1]

for file in glob(f"./input{problem_num}/*.txt"):
    output_path = f"output{problem_num}"
    os.makedirs(output_path, exist_ok=True)
    os.system(
        f"python {problem_num}.py < {file} "
        f"> {output_path}/{os.path.basename(file)}"
    )
