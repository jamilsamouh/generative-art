from GenerativeArt import GenerativeArt
import numpy as np
import time

IMG_DIR = "img/"
IMG_SUBDIR = "everything/"
IMG_SUBDIR2 = "handpicked/"

LOGFILE_DIR = "logfile/"
LOGFILE = "logfile.xlsx"

art_test = GenerativeArt()

art_test.setup_directories(IMG_DIR,IMG_SUBDIR,IMG_SUBDIR2,LOGFILE_DIR, LOGFILE)

def transform_x(x_i,y_i,seed):

    seed = int (seed)
    
    rng = np.random.RandomState(seed)

    return rng.uniform(-1,1,1) * x_i**4 - np.sin(y_i**2)

def transform_y(x_i,y_i,seed):
    
    seed = int (seed)
    
    rng = np.random.RandomState(seed)
            
    return rng.uniform(-1,1,1) * y_i**2 - np.sin(x_i**3)

my_formula = [transform_x,transform_y]


# short version
art_test.generate_img( formula = my_formula, nr_of_img = 1, filetype = 'gif', polar = True , animate = True, cmap = True, cmap_color= 'plasma_r', cmap_direction= 'V' )






