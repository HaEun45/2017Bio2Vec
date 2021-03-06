import pandas as pd
pd.options.mode.chained_assignment = None
import numpy as np
import re
import nltk

from sklearn.manifold import TSNE
import matplotlib
import matplotlib.pyplot as plt

import pickle
import os

class BioTsne:
    def __init__(self):
        print 'TSNE is running..'

        
    # making tsne
    def make_tsne(self,file_path,path):
        
        if not os.path.isfile(file_path):
            # make tsne # have to use csv file
            #protein csv parsing
            print "Loading protvec"

            vectors_float = []
            with open(path) as protein_vector:
                for line in protein_vector:
                    uniprot_id, vector = line.rstrip().split('\t', 1)
                    vectors_float.append(map(float, vector.split()))

            vectors_array = np.array(vectors_float,ndmin=2,dtype=np.float32)
            vectors_float = None

            print vectors_array
            print "... OK\n"

            vectors_array=np.nan_to_num(vectors_array)
            
            print "Making tsne"
            tsne = TSNE(n_components=2)
            X_tsne = tsne.fit_transform(vectors_array)
            print "... OK\n"

            print "Saving tsne"
            # save X_tsne
            
            f = open(file_path,"wb")
            pickle.dump(X_tsne , f)
            f.close()
            print "... OK\n"

    def visualization( self, disprot_path , pdb_path ):
        # load X_tsne data
        
        f = open( disprot_path , "rb")
        disprot = pickle.load(f)
        f.close()

        f = open( pdb_path , "rb")
        pdb = pickle.load(f)
        f.close()

        fig , ax = plt.subplots()

        d = ax.scatter(disprot[:,0], disprot[:, 1],c='r')
        p = ax.scatter(pdb[:,0], pdb[:, 1] , c='b')
        
        l = ax.legend([d, p], ['disprot', 'pdb'], scatterpoints=1,
               numpoints=1, handler_map={tuple: HandlerTuple(ndivide=None)})
        plt.show()

        return 0

