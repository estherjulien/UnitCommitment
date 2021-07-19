import numpy as np


class Network:
    def __init__(self, T, unc_perc):
        self.T = T
        self.unc_perc = unc_perc
        # create matrices
        self.matrices = self.create_matrices()

    def change_settings(self, T=None, unc_perc=None):
        if T is not None:
            self.T = T
        if unc_perc is not None:
            self.unc_perc = unc_perc

    def data_convert(self):

        return None

    def create_matrices(self):
        data = self.data_convert(self.T, self.unc_perc)

        return matrices

