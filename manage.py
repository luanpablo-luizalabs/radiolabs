#!/usr/bin/env python
import os
import sys

from radiolabs.boot import fix_path


fix_path()


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "radiolabs.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
