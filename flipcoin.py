#!/usr/bin/env python

"""
Author: John D. Anderson
Email: jander43@vols.utk.edu
Description: Coin flipping simulator for command line
Usage:
    flipcoin <flips> <games>
"""

# libs
import random
import numpy


# funcs
def main(params):

    # init heads and tails counters
    heads = 0
    tails = 0

    # get matrix size
    params['total'] = params['flips'] * params['games']

    # create numpy array
    outcome = numpy.zeros((params['games'], params['flips']))

    # print table beginning
    print '-'*params['flips']

    # start simulation
    for i in range(params['games']):
        # init count and outcome
        count = 0
        for j in range(params['flips']):
            rand = random.randint(1, 2)
            # Checks if head or tail #
            if rand == 1:
                heads += 1
                outcome[i][j] = 1
            else:
                tails += 1
            count += 1

    # result
    print outcome

    # print table end
    print '-'*params['flips']

    # Basic formula for calculating percentage #
    percentage = (float(heads) / params['total']) * 100

    # Print statements #
    print "Heads = " + str(heads)
    print "Tails = " + str(tails)
    print "Percentage heads = " + str(percentage) + "%"


# executable only
if __name__ == '__main__':

    # parse args
    from docopt import docopt

    # get args
    args = docopt(__doc__)

    # parameters
    params = {'flips': int(args['<flips>']), 'games': int(args['<games>'])}

    # run
    main(params)
