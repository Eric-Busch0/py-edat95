import argparse
from emb_edat import Edat95


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
