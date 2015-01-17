import random
import time

LOWER_BOUND = 0
UPPER_BOUND = 65536
LENGTH = len(str(UPPER_BOUND))

def match(trainer_id):
    try:
        if (trainer_id < LOWER_BOUND or trainer_id > UPPER_BOUND - 1 or not isinstance(trainer_id,int)):
            print("Error: argument must be an integer between 0 and 65535 inclusive")
        else:
            ids = []
            for i in range(LOWER_BOUND, UPPER_BOUND):
                ids.append(str(i).zfill(LENGTH))
            
            tid = str(trainer_id).zfill(LENGTH)
            match0 = 0
            match1 = 0
            match2 = 0
            match3 = 0
            match4 = 0
            match5 = 0

            for lid in ids:
                matched = 0
                for digit in range(LENGTH):
                    if lid[digit] == tid[digit]:
                        matched += 1
                if matched == 0:
                    match0 += 1
                elif matched == 1:
                    match1 += 1
                elif matched == 2:
                    match2 += 1
                elif matched == 3:
                    match3 += 1
                elif matched == 4:
                    match4 += 1
                elif matched == 5:
                    match5 += 1

            print("Results:")
            print("0 digits:   " + str(match0).rjust(LENGTH) + " | " + calculateChance(match0).rjust(7) + "%")
            print("1 digit:    " + str(match1).rjust(LENGTH) + " | " + calculateChance(match1).rjust(7) + "%")
            print("2 digits:   " + str(match2).rjust(LENGTH) + " | " + calculateChance(match2).rjust(7) + "%")
            print("3 digits:   " + str(match3).rjust(LENGTH) + " | " + calculateChance(match3).rjust(7) + "%")
            print("4 digits:   " + str(match4).rjust(LENGTH) + " | " + calculateChance(match4).rjust(7) + "%")
            print("5 digits:   " + str(match5).rjust(LENGTH) + " | " + calculateChance(match5).rjust(7) + "%")
            print("")

            atleast1 = match1 + match2 + match3 + match4 + match5
            atleast2 = match2 + match3 + match4 + match5
            atleast3 = match3 + match4 + match5
            atleast4 = match4 + match5
            print("At least 1: " + str(atleast1).rjust(LENGTH) + " | " + calculateChance(atleast1).rjust(7) + "%")
            print("At least 2: " + str(atleast2).rjust(LENGTH) + " | " + calculateChance(atleast2).rjust(7) + "%")
            print("At least 3: " + str(atleast3).rjust(LENGTH) + " | " + calculateChance(atleast3).rjust(7) + "%")
            print("At least 4: " + str(atleast4).rjust(LENGTH) + " | " + calculateChance(atleast4).rjust(7) + "%")

    except ValueError:
        print("Error: unexpected value")
    except TypeError:
        print("Error: match given non-integer argument")

def calculateChance(matched):
    return str(round(((matched / UPPER_BOUND) * 100), 4))

def matchIds(trainer_ids):
    start_time = time.time()
    try:
        match0 = set()
        match1 = set()
        match2 = set()
        match3 = set()
        match4 = set()
        match5 = set()

        ids = []
        for i in range(LOWER_BOUND, UPPER_BOUND):
            ids.append(str(i).zfill(5))
        
        for tid in trainer_ids:
            if (tid < LOWER_BOUND or tid > UPPER_BOUND - 1 or not isinstance(tid,int)):
                print("Error: argument must be an integer between 0 and 65535 inclusive.")
            else:
                tid = str(tid).zfill(5)

                for lid in ids:
                    matched = 0
                    for digit in range(5):
                        if lid[digit] == tid[digit]:
                            matched += 1
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
