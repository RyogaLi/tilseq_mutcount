# testing script for all the python scripts
import pandas as pd
import os
import argparse
import timeit

import count_mut as cm

###
# test time

class UnitTest(object):

    """Unitesting for all the python scripts"""

    def __init__(self, args):
        self.args = args

    def _test_count_mut(self):
        """
        Test count mutation class
        """
        # init all the input parameters
        # sam_r1, sam_r2, param, log_level, output_dir
        sam_r1 = "/home/rothlab1/rli/dev/tilseq_mutcount/output/SUMO_rerun_2020-05-01-15-59-22/sam_files/30_R1_joint.sam"
        sam_r2 = "/home/rothlab1/rli/dev/tilseq_mutcount/output/SUMO_rerun_2020-05-01-15-59-22/sam_files/30_R2_joint.sam"
        param = "/home/rothlab1/rli/dev/tilseq_mutcount/output/SUMO_rerun_2020-05-01-15-59-22/SUMO1_parameters.json"
        log_level = "debug"
        output_dir = "/home/rothlab1/rli/dev/tilseq_mutcount/output/SUMO_rerun_2020-05-01-15-59-22/testdel_2020-07-14-12-43-26_mut_count"
        # init read sam
        print("Testing count_mut")
        start = timeit.default_timer()
        test_readSam = cm.readSam(sam_r1, sam_r2, param, log_level, output_dir)
        test_readSam._merged_main()
        stop = timeit.default_timer()
        print(f"Linear time to read both sam files: {stop - start}")

    def _test_locaste_mut(self):
        """
        Test locate muataion class
        """
        # init all the input parameters
        # self, row, full_seq, cds_seq, seq_lookup, tile_s, tile_e, post_prob_cutoff, logging, mut_rate
        row = 
        pass


def main(args):
    ut = UnitTest(args)
    if args.mode == "count_mut":
        ut._test_count_mut()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Unit Test modules')
    # user input arguments
    parser.add_argument("-m", help="Mode of testing")
