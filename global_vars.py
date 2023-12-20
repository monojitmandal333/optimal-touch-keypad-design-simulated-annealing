import ast
import numpy as np
import utils

BIGRAM_PROBABILITY_MATRIX = utils.read_data_matrix("data/bigram_prob.txt")
BIGRAM_PROBABILITY_MATRIX = utils.normalize(BIGRAM_PROBABILITY_MATRIX)
MOVEMENT_TIME_MATRIX = utils.read_data_matrix("data/movement_time.txt")