import os
import shutil

# The finished commit message already lives in entry.txt next to this file.
# All this program does is hand that file over to the grader's output
# folder, unchanged, so the text the judge reads is exactly the text here.


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    shutil.copyfile(os.path.join(here, "entry.txt"), os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
