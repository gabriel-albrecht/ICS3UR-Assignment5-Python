#!/usr/bin/env python3

# Created by Gabriel A
# Created on Dec 2020
# This program calculates the sum of all 1/n


def main():
    try:
        # input
        value_n = int(input("Enter any integer (except for 0): "))
        print("")

        # process & output
        su = 0
        if value_n > 0:
            loop = 1
            while loop <= value_n:
                su += 1 / loop
                sequence = 1 / loop
                print("Added 1/{} ({}): Sum is {}".format(loop, sequence, su))
                loop += 1
            print("")
            print("Total sum is {}.".format(su))

        elif value_n < 0:
            loop = -1
            while loop >= value_n:
                su += 1 / loop
                sequence = 1 / loop
                print("Added 1/{} ({}): Sum is {}".format(loop, sequence, su))
                loop -= 1
            print("")
            print("Total sum is {}.".format(su))
        else:
            print("0 cannot be calculated in this sequence.")

    except ValueError:
        print("")
        print("That is not a number.")


if __name__ == "__main__":
    main()
