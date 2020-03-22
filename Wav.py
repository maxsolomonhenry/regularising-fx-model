import numpy as np
import h5py


def read_h5(filename):    
    with h5py.File(filename, 'r') as f:
        a_group_key = list(f.keys())[0]

        # Get the data
        y = list(f[a_group_key])
        data = np.asarray(y)

    print("train",data.shape)
    return data

def val_h5(filename):    
    with h5py.File(filename, 'r') as f:
        a_group_key = list(f.keys())[0]

        # Get the data
        y = list(f[a_group_key])
        data = np.asarray(y)
        
        data_out = data[0::2]

    print("val",data_out.shape)
    return data_out

def test_h5(filename):    
    with h5py.File(filename, 'r') as f:
        a_group_key = list(f.keys())[0]

        # Get the data
        y = list(f[a_group_key])
        data = np.asarray(y)
        
        data_out = data[1::2]

    print("test",data_out.shape)
    return data_out
