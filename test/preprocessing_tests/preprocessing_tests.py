import unittest
import sys
import traceback
import sml.python.actions.preprocessing as pp
import sml.python.actions.IO as io
import numpy as np
import pandas as pd
import os.path
from pandas.util.testing import assert_frame_equal



class preprocessing_tests(unittest.TestCase):
    def test_encode(self):

        pass
    def test_impute(self):
        pass
    def test_split(self):
        data = np.arange(30).reshape((6, 5))
        data_train,data_test = pp.handle_split(data,0.5)
        assert len(data_train) == 3 and len(data_test) == 3
        pass
        
    def test_to_csv(self):
        df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)),columns = ['0','1','2','3'])
        io.handle_write_csv(df, "test1.csv")
        df_test = pd.read_csv("test1.csv")
        assert_frame_equal(df, df_test,check_dtype=False,check_column_type=False)



if __name__ == '__main__':
    unittest.main()
