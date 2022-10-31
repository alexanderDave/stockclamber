import os, sys
root_path = os.path.dirname(os.path.dirname(__file__))
ado_path = os.path.join(root_path, 'ADO')
sys.path.append(root_path)
sys.path.append(ado_path)
from config import config
from dates import stockdates
import utiltool as ut

class Notices():

    def __init__(self, pickles):c
        self.cf = config()
        self.data = ut.loadpickle(os.path.join(self.cf.res_path, pickles))


    def getNotice(self):

        pass




if __name__ == '__main__':
    print('gen infos')
#     test code = 601601_20220915.pickle
    nt = Notices('601601_20220915.pickle')
    print(nt.data)
