# generativeart

Create Generative Art with Python.

## Description

The `Python` package `GenerativeArt` let's you create images based on many thousand points.

In order to make an image reproducible, `generative art` implements a log file that saves the `file_name`, the `seed` and the `formula`.

## Install

**Note:** There is no package to install yet (work in progress) but will make a setup file so you can pip install GenerativeArt for Python to use it easily.

To install locally: 
```bash
git clone https://github.com/jamilsamouh/generative-art.git
cd generative-art
```

## Usage

**Steps to use:**

1- Install the package locally from the `install` section and navigate to `spirals` directory. 

2- Use the terminal to install the requirements file by running the following command to make sure you have all the libraries installed
```bash
pip install -r requirements.txt
```
3- Open up `GenerativeArtRun.py` using any Python IDE (Visual Studio Code/ Pycharm) and run the python script and it will plot 1 animated plot with unique shapes inside the `./img/everything` direcotry

4- To custom change the code for example to change the color and number of images..etc. This is the main code to generate the art inside `GenerativeArtRun.py`

```Python
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
art_test.generate_img( formula = my_formula, nr_of_img = 1, filetype = 'gif', polar = True , cmap = True, cmap_color= 'plasma_r', cmap_direction= 'V', animate = True )
```
**You can change the following to be custom made:**
* You can change the formula that you used to trasnfer your data on, and to do that change the following two functions `transform_x` and `transform_y` (**NOTE:** Always make sure to have the seed as the third parameter to make sure random variables are fixed based on the seed number)
* You can create as many images as you want by setting `nr_of_img`.
* You can define whether you want to plot it on Polar coordinates `polar = True` or Cartesian coordinates `polar = False`
* You can save the output image/animation in various formats. Default is ` filetype = "png" `.
* You can choose the dots colors with ` color = "blue" ` or use a cmap with `cmap = True` and `cmap_colors = "plasma_r" ` and `cmap_direction = "V" `  (**NOTE:** for cmap_color you can either pass a cmap color that is builtin or a list of colors you want to interpolate between)
* you can choose the background color ` background_color = "white" `
* define the plot info such as dots size `s = 1`, transperancy `alpha = 0.1`, line width `lw = 0.1`, image size `image_size = (5,5)`, resolution `dpi = 1000`
* Anime the plot using `animate = False`, the interval between partitions `interval = 1`, and number of partitions `num_partitions = 20`

5- Open up `GenerativeArtRun.py` using any Python IDE (Visual Studio Code/ Pycharm) and run the python script after the custom changes you did

6- you can regenerate an image from the logfile if you know the file name for example 

```Python
art_test.regenerate_img( filename )
```


The corresponding log file looks like that:

| file_name                      | seed | formula_x                            | formula_y                            | 
|--------------------------------|------|--------------------------------------|--------------------------------------| 
| 2018-11-16-17-13_seed_1821.png | 1821 | def transform_x(x_i,y_i,seed): ..... | def transform_y(x_i,y_i,seed): ..... | 

## Examples

1-  **Image** in Cartesian Coordinates `polar = False`, with fixed color and background color 

```Python
art_test.generate_img( formula = my_formula, filetype = 'png', polar = False , color = 'red', background_color='black' )  
```

2-  **Image** in Polar  Coordinates `polar = True`, with continuous color using `cmap = True`, `cmap_color = "plasma_r" ` and change the color vertically `cmap_direction = "V" ` 

```Python
art_test.generate_img( formula = my_formula, filetype = 'png', polar = True , background_color='black', cmap = True, cmap_color= 'plasma_r', cmap_direction= 'V' ) 
```

3-  **Image** in Cartesian Coordinates `polar = False`, with continuous color using `cmap = True`, `cmap_color = ['red', 'green] ` and change the color horizontally `cmap_direction = "H" ` and it wil change the color from red to green with different shades horizontally 

```Python
art_test.generate_img( formula = my_formula, filetype = 'png', polar = False , background_color='black', cmap = True, cmap_color= ['pink','green'], cmap_direction= 'H' ) 
```

4-  **Animation** in Cartesian Coordinates `polar = False`, with fixed color 

```Python
art_test.generate_img( formula = my_formula, filetype = 'gif', polar = False , color = 'red', background_color='black', animate=True )
```

5-  **Animation** in Polar Coordinates `polar = True`, with continuous color using `cmap = True`, `cmap_color = ['blue', 'green] ` and change the color vertically `cmap_direction = "V" ` and it wil change the color from blue to green with different shades vertically

```Python
art_test.generate_img( formula = my_formula, filetype = 'gif', polar = True , background_color='black', cmap = True, cmap_color= ['blue','green'], cmap_direction= 'V', animate=True ) 
```




## Limitations

1- Some plots/animations will looks almost identical because of the uniform random variable as if it has a similar value it will almost create an identical plot/animation

2- Animating an image with cmap will take 1 minute for each animation (before used to be 5 minutes but optimized it)

3- This repo has been tested **only** on Windows OS

## Credits

The basic concept is heavily inspired by [Fronkonstin's great blog](https://fronkonstin.com/) and by the implementation for [generativeart](https://github.com/jamilsamouh/generativeart) in `R` Langauge .
