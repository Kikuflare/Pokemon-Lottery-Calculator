import random
import time
import sys
import argparse


# Minimum and maximum values of valid trainer ids
LOWER_BOUND = 0
UPPER_BOUND = 65536
LENGTH = len(str(UPPER_BOUND))


def match_ids(trainer_ids):
    # Takes a list of trainer ids and calculates the odds of winning each tier of lottery prize in the Pokemon games.
    # Prints out the results of the calculations at the end.
    start_time = time.time()
    try:
        # Sets that contain unique lotto numbers that match 0 to 5 digits.
        match0 = set()
        match1 = set()
        match2 = set()
        match3 = set()
        match4 = set()
        match5 = set()

        # Create a list containing all possible lottery numbers in string form with padded 0s if the number
        # has less than 5 digits.
        ids = []
        for i in range(LOWER_BOUND, UPPER_BOUND):
            ids.append(str(i).zfill(5))
        
        for tid in trainer_ids:
            if (tid < LOWER_BOUND or tid > UPPER_BOUND - 1 or not isinstance(tid,int)):
                print("Error: argument must be an integer between 0 and 65535 inclusive.")
                sys.exit()
            else:
                tid = str(tid).zfill(5)

                for lid in ids:
                    matched = 0
                    for digit in reversed(range(LENGTH)):
                        if lid[digit] == tid[digit]:
                            matched += 1
                        else:
                            break
                    
                    # Promote ids to a higher set by discarding the value in lower sets when a better match is found
                    if matched == 5:
                        match5.add(lid)
                        match4.discard(lid)
                        match3.discard(lid)
                        match2.discard(lid)
                        match1.discard(lid)
                        match0.discard(lid)
                    elif matched == 4:
                        if lid not in match4 and lid not in match5:
                            match4.add(lid)
                            match3.discard(lid)
                            match2.discard(lid)
                            match1.discard(lid)
                            match0.discard(lid)
                    elif matched == 3:
                        if lid not in match3 and lid not in match4 and lid not in match5:
                            match3.add(lid)
                            match2.discard(lid)
                            match1.discard(lid)
                            match0.discard(lid)
                    elif matched == 2:
                        if lid not in match2 and lid not in match3 and lid not in match4 and lid not in match5:
                            match2.add(lid)
                            match1.discard(lid)
                            match0.discard(lid)
                    elif matched == 1:
                        if lid not in match1 and lid not in match2 and lid not in match3 and lid not in match4 and lid not in match5:
                            match1.add(lid)
                            match0.discard(lid)
                    elif matched == 0:
                        if lid not in match0 and lid not in match1 and lid not in match2 and lid not in match3 and lid not in match4 and lid not in match5:
                            match0.add(lid)

        # Print out results of calculations
        print("Results:")
        print("0 digits:   " + str(len(match0)).rjust(LENGTH) + " | " + calculateChance(len(match0)).rjust(7) + "%")
        print("1 digit:    " + str(len(match1)).rjust(LENGTH) + " | " + calculateChance(len(match1)).rjust(7) + "%")
        print("2 digits:   " + str(len(match2)).rjust(LENGTH) + " | " + calculateChance(len(match2)).rjust(7) + "%")
        print("3 digits:   " + str(len(match3)).rjust(LENGTH) + " | " + calculateChance(len(match3)).rjust(7) + "%")
        print("4 digits:   " + str(len(match4)).rjust(LENGTH) + " | " + calculateChance(len(match4)).rjust(7) + "%")
        print("5 digits:   " + str(len(match5)).rjust(LENGTH) + " | " + calculateChance(len(match5)).rjust(7) + "%")
        print("")

        atleast1 = len(match1) + len(match2) + len(match3) + len(match4) + len(match5)
        atleast2 = len(match2) + len(match3) + len(match4) + len(match5)
        atleast3 = len(match3) + len(match4) + len(match5)
        atleast4 = len(match4) + len(match5)

        print("At least 1: " + str(atleast1).rjust(LENGTH) + " | " + calculateChance(atleast1).rjust(7) + "%")
        print("At least 2: " + str(atleast2).rjust(LENGTH) + " | " + calculateChance(atleast2).rjust(7) + "%")
        print("At least 3: " + str(atleast3).rjust(LENGTH) + " | " + calculateChance(atleast3).rjust(7) + "%")
        print("At least 4: " + str(atleast4).rjust(LENGTH) + " | " + calculateChance(atleast4).rjust(7) + "%")

        elapsed_time = time.time() - start_time
        print("Calculated in " + str(format(elapsed_time, '.3f')) + " seconds")

    except ValueError:
        print("Error: unexpected value")
    except TypeError:
        print("Error: matchIds given list containing non-integer element")

def generate(n):
    return random.sample(range(LOWER_BOUND, UPPER_BOUND), n)
    
def calculateChance(matched):
    # Calculate the percentage of matched values out of 65535, returns result rounded to 4 digits as a string.
    return str(round(((matched / UPPER_BOUND) * 100), 4))

def main():
    # Command line interface
    parser = argparse.ArgumentParser(description="Calculate the odds of winning each tier of lottery prize in the Pokemon games.")
    parser.add_argument('--generate',
                        dest='generate',
                        help="Automatically generate ids.",
                        action='store_true')
    parser.add_argument('N',
                        help="If --generate flag is set, N is a single argument that specifies how many random ids to automatically generate. Otherwise, N is any number of user specified ids between 0 ad 65535 inclusive.",
                        type=int,
                        nargs='+')
    
    # Parse the command line arguments
    args = parser.parse_args()
    
    # Generate random ids or use command line supplied values
    if args.generate:
        if len(args.N) == 1:
            if args.N[0] < 0:
                print("Error: N must be a positive integer.")
            else:
                match_ids(generate(args.N[0]))
        else:
            print("Error: --generate expected 1 argument, got {}".format(len(args.N)))
        
    else:
        match_ids(args.N)
    
if __name__ == "__main__":
    main()