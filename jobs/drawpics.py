import os, sys
root_path = os.path.dirname(os.path.dirname(__file__))
ado_path = os.path.join(root_path, 'ADO')
sys.path.append(root_path)
sys.path.append(ado_path)
from config import config
from dates import stockdates

if __name__ == '__main__':
    codes = config().watchlist

    for key,value in codes.items():
        st = stockdates(key, value)
        st.getDaily(-380)
        st.genFinance(mavs=20,duration=-100)
