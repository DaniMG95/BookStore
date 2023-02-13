#!/usr/bin/env python3

import re
import sys
from subprocess import check_output

commit_msg_filepath = sys.argv[1]
branch = check_output(["git", "symbolic-ref", "--short", "HEAD"]).decode("utf-8").strip()

regex = r"^YTG-[0-9]{1,9}"
types_branches = ("feat", "hotfix", "fix")


type = branch.split("/")[0]
branch = branch.split("/")[1]
found_obj = re.match(regex, branch)

if found_obj:
    prefix = found_obj.group(0)
    with open(commit_msg_filepath, "r+") as f:
        commit_msg = f.read()
        if commit_msg.find(prefix) == -1 and type in types_branches:
            f.seek(0, 0)
            f.write(f"{type}: {prefix} {commit_msg}")
