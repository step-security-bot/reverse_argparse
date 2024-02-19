#!/usr/bin/env python3
"""
How ``reverse_argparse`` handles default values.

© 2024 National Technology & Engineering Solutions of Sandia, LLC
(NTESS).  Under the terms of Contract DE-NA0003525 with NTESS, the U.S.
Government retains certain rights in this software.

SPDX-License-Identifier: BSD-3-Clause
"""
from argparse import ArgumentParser

from reverse_argparse import ReverseArgumentParser

# Construct the `ArgumentParser`.
parser = ArgumentParser()
parser.add_argument("--foo")
parser.add_argument("--bar", default="spam")
parser.add_argument("--baz", type=int, default=42)

# Parse the command line arguments.
args = parser.parse_args()

# Insert the body of your script here.

# Unparse the arguments to tell the user what they ran.
print("The effective command line invocation was:")
unparser = ReverseArgumentParser(parser, args)
print(unparser.get_effective_command_line_invocation())
