import sys

sys.path.append('..')

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


#1 xy_static_color
art_test.generate_img( formula = my_formula, filetype = 'png', polar = False , color = 'red', background_color='black' )  
#2 xy_static_cmap_str_V
art_test.generate_img( formula = my_formula, filetype = 'png', polar = False , background_color='black', cmap = True, cmap_color= 'plasma_r', cmap_direction= 'V' ) 
#3 xy_static_cmap_str_H
art_test.generate_img( formula = my_formula, filetype = 'png', polar = False , background_color='black', cmap = True, cmap_color= 'plasma_r', cmap_direction= 'H' ) 
#4 xy_static_cmap_list_V
art_test.generate_img( formula = my_formula, filetype = 'png', polar = False , background_color='black', cmap = True, cmap_color= ['pink','green'], cmap_direction= 'V' ) 
#5 xy_static_cmap_list_H
art_test.generate_img( formula = my_formula, filetype = 'png', polar = False , background_color='black', cmap = True, cmap_color= ['pink','green'], cmap_direction= 'H' ) 
#6 xy_notstatic_color
art_test.generate_img( formula = my_formula, filetype = 'gif', polar = False , color = 'red', background_color='black', animate=True ) 
#7 xy_notstatic_cmap_str_V
art_test.generate_img( formula = my_formula, filetype = 'gif', polar = False , background_color='black', cmap = True, cmap_color= 'plasma_r', cmap_direction= 'V', animate=True ) 
#8 xy_notstatic_cmap_str_H
art_test.generate_img( formula = my_formula, filetype = 'gif', polar = False , background_color='black', cmap = True, cmap_color= 'plasma_r', cmap_direction= 'H', animate=True ) 
#9 xy_notstatic_cmap_list_V
art_test.generate_img( formula = my_formula, filetype = 'gif', polar = False , background_color='black', cmap = True, cmap_color= ['blue','green'], cmap_direction= 'V',animate=True ) 
#10 xy_notstatic_cmap_list_H
art_test.generate_img( formula = my_formula, filetype = 'gif', polar = False , background_color='black', cmap = True, cmap_color= ['blue','green'], cmap_direction= 'H', animate=True ) 
#11 rr_static_color
art_test.generate_img( formula = my_formula, filetype = 'png', polar = True , color = 'red', background_color='black' )  
#12 rr_static_cmap_str_V
art_test.generate_img( formula = my_formula, filetype = 'png', polar = True , background_color='black', cmap = True, cmap_color= 'plasma_r', cmap_direction= 'V' ) 
#13 rr_static_cmap_str_H
art_test.generate_img( formula = my_formula, filetype = 'png', polar = True , background_color='black', cmap = True, cmap_color= 'plasma_r', cmap_direction= 'H' ) 
#14 rr_static_cmap_list_V
art_test.generate_img( formula = my_formula, filetype = 'png', polar = True , background_color='black', cmap = True, cmap_color= ['pink','green'], cmap_direction= 'V' ) 
#15 rr_static_cmap_list_H
art_test.generate_img( formula = my_formula, filetype = 'png', polar = True , background_color='black', cmap = True, cmap_color= ['pink','green'], cmap_direction= 'H' ) 
#16 rr_notstatic_color
art_test.generate_img( formula = my_formula, filetype = 'gif', polar = True , color = 'red', background_color='black', animate=True ) 
#17 rr_notstatic_cmap_str_V
art_test.generate_img( formula = my_formula, filetype = 'gif', polar = True , background_color='black', cmap = True, cmap_color= 'plasma_r', cmap_direction= 'V', animate=True ) 
#18 rr_notstatic_cmap_str_H
art_test.generate_img( formula = my_formula, filetype = 'gif', polar = True , background_color='black', cmap = True, cmap_color= 'plasma_r', cmap_direction= 'H', animate=True ) 
#19 rr_notstatic_cmap_list_V
art_test.generate_img( formula = my_formula, filetype = 'gif', polar = True , background_color='black', cmap = True, cmap_color= ['blue','green'], cmap_direction= 'V',animate=True ) 
#20 rr_notstatic_cmap_list_H
art_test.generate_img( formula = my_formula, filetype = 'gif', polar = True , background_color='black', cmap = True, cmap_color= ['blue','green'], cmap_direction= 'H', animate=True ) 

# short version
art_test.generate_img( formula = my_formula, nr_of_img = 1, filetype = 'gif', polar = False , animate = True, cmap = True, cmap_color= ['pink','red'], cmap_direction= 'V' )

#long version 
art_test.generate_img(formula = my_formula, nr_of_img = 1, polar = True, filetype = 'gif', cmap = True, cmap_color= ['pink','blue'], cmap_direction= 'V' , background_color = 'white',  s = 2, alpha = 0.2,
        lw = 0.2, image_size = (5,5), dpi = 1000, animate = True, interval = 1, num_partitions = 20 )





