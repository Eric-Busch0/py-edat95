# BSD 2-Clause License

# Copyright (c) 2024, Eric

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import argparse
from edat95 import Edat95


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-g", "--get", action="store_true", help="Get current attenuation"
    )
    parser.add_argument("-s", "--set", help="Set current attenuation")
    parser.add_argument(
        "-n", "--name", action="store_true", help="get name of attenuator"
    )
    parser.add_argument("--set-loss", default=0, help="Set current attenuation")


    dat = Edat95()

    args = parser.parse_args()

    if args.name:
        print(dat.get_name())

    if args.get:
        print(dat.get_attenuation())

    if args.set:
        dat.set_attenuation(int(args.set))


    if args.set_loss:
        dat.set_insertion_loss(int(args.set_loss), store_non_volatile=True)

if __name__ == "__main__":
    main()
