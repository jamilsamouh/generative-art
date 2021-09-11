import os
from random import sample
import matplotlib.pyplot as plt
import time
import math
import pandas as pd
import numpy as np
import seaborn as sns
import itertools
import inspect
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import matplotlib

class GenerativeArt:

    pi_positive = round (math.pi,9) 
    
    pi_minus = round (-math.pi,9) 

    pi_ranges = np.arange(pi_minus, pi_positive, 0.01).tolist()

    product = list( itertools.product( pi_ranges, pi_ranges ) )

    pi_grid = np.round ( product, 9)

    pi_grid[:,[0, 1]] = pi_grid[:,[1, 0]]
    
    fixed_df = pd.DataFrame( pi_grid, columns = ['x_i','y_i'] )
    
    def __init__(self):
        """This class lets you create images based on many thousand points. The position of every single point is calculated by a formula,
         which has random parameters. Because of the random numbers, every image looks different.

        """
        self.img_path = None
        
        self.logfile_path = None
            
    def setup_directories(self, img_path, img_subdir, img_subdir2, logfile_dir,logfile):
        """Setup a directory structure for image creation

        Args:
            img_path (str): the images main directory path that you want to save the images to
            img_subdir (str): the images subdirectory path that you want to save the images to and it will contain all the images you want to
            img_subdir2 (str): the images subdirectory path that you want to save the images that is picked manually by the user
            logfile_dir (str): the logfile directory where you will save the log file into
            logfile (str): the name of the logfile you will create
        """
        
        if not os.path.isdir( os.path.join( os.getcwd(), img_path) ):
            
            os.makedirs( os.path.join( os.getcwd(), img_path) ) 
            
        if not os.path.isdir( os.path.join( os.getcwd(), img_path, img_subdir) ):
            
            os.makedirs( os.path.join( os.getcwd(), img_path, img_subdir) ) 
            
        if not os.path.isdir( os.path.join( os.getcwd(), img_path, img_subdir2) ):
            
            os.makedirs( os.path.join( os.getcwd(), img_path, img_subdir2) )        
            
        if not os.path.isdir( os.path.join( os.getcwd(), logfile_dir) ):
            
            os.makedirs( os.path.join( os.getcwd(), logfile_dir) ) 
      
        self.img_path = os.path.join( os.getcwd(), img_path, img_subdir)
        
        self.logfile_path = os.path.join( os.getcwd(), logfile_dir,logfile)
        
            
    def generate_img (self, formula, nr_of_img = 1, polar = True, filetype = 'png', s = 1, alpha = 0.1, lw = 0.1, image_size = (5,5), dpi = 1000, color = 'black', cmap = False, cmap_color = 'plasma_r', cmap_direction = 'V', background_color = 'white', animate = False, interval = 1, num_partitions = 20 ):
        """This is the main function that triggers most of the other functions and it is built to generate images/animations with differnt shapes

        Args:
            formula (list): a list of length 2 and each index has a function to transform the data
            nr_of_img (int, optional): the amount of images you want to regenerate. Defauls to 1
            polar (bool, optional): Whether you want to plot in the Cartesian or Polor coordincates where True = Polar and False = Cartesian. Defaults to False.
            filetype (str, optional): define the file type of the image you want to save to. Defaults to "png".
            s (int, optional): the size of the dots in the image. Defauls to 1
            alpha (int, optional): the transperancy of the plot. Defaults to 0.1
            lw (int, optional): is the line width of the plot. Defaults to 0.1
            image_size (tuple, optional): the size of the image. Defaults to (5,5)
            dpi (int, optional): the resolution of the plot. Defaults to 1000
            color (str, optional): the color of the dots on the plot. Defaults to 'black.
            cmap (bool, optional): if you want the color to be continuous. Defaults to False
            cmap_color (str/list, optional): this can be a string for a builtin cmap or you can pass a multiple colors and it will create the cmap for you. Defaults to 'plasma_r'  
            cmap_direction (str, optional): the direction in which you want the color to propogate can be either H for horizontal or V for vertical. Defaults to V
            background_color (str, optional): the color of the background of the plot. Defaults to 'white'.
            animate (bool, optional): whether you want to animate the plot or not. Defaults to False
            interval (int, optional): the interval time in milliseconds in which you want to plot. Defaults to 1
            num_partitions (int, optional): the amount of transitions you want to have in your animation. Defaults to 20

        """            

        seeds = self.generate_seeds(nr_of_img)
        
        for num, seed in enumerate ( seeds ):
            
            print(f"\nImage # :" + str(num + 1) )
            
            file_name, file_name_path = self.generate_filename(seed, filetype)
            
            logfile = self.check_logfile_existence()
            
            logfile = self.generate_logfile_entry(logfile, formula, seed, file_name)
            
            df = self.generate_data(formula,seed)

            if animate == False:
                        
                plot = self.generate_plot(df, file_name_path, polar, filetype, s, alpha , lw, image_size, dpi, color, cmap, cmap_color, cmap_direction ,background_color )
            
            elif animate == True:

                animation = self.generate_animation(df, file_name_path, polar, filetype, s, alpha , lw, image_size, dpi, color, cmap, cmap_color, cmap_direction ,background_color, interval, num_partitions)
                    
    def generate_seeds (self, nr_of_img ):
        """generate random seed for each image

        Args:
            nr_of_img ([type]): [description]

        Returns:
            int : random seed between 1-100000
        """
        
        print("generate seeds")

        seeds = sample( range(1,10001), nr_of_img)
        
        return seeds
    
    def generate_filename (self, seed, filetype):
        """generate the file name based on the seed and timestamp to save the plot under

        Args:
            seed (int): the seed number
            filetype (str): the name of the file type you want to save to

        Returns:
            str: the file name you want to save the plot to
        """
        
        print("generate file name")

        file_name = time.strftime("%Y-%m-%d-%H-%M-%S") + "_seed_" + str(seed) + "." + filetype

        file_name_path = os.path.join( self.img_path, file_name)
        
        return file_name, file_name_path
                                      
    def check_logfile_existence (self):
        """check wheter a log file exists or no

        Returns:
            bool: return True if there is a logfile or False if there is not
        """
                                      
        if os.path.isfile(self.logfile_path):
            
            print("load logfile")
                
            
            df = pd.read_excel(self.logfile_path)
        
        else:
                                      
            print("create logfile")
            
            
            df = pd.DataFrame(columns= ['file_name', 'seed', 'formula_x', 'formula_y'])
        
        return df
    
    def generate_logfile_entry (self, logfile, formula, seed, file_name):
        """Append to the logfile with the new metadate from each run for each image such as formula/seed/file_name

        Args:
            logfile (DataFrame): the dataframe that contains the logfile entities
            formula (list): a list of length 2 and each index has a function to transform the data
            seed (int): the seed number
            file_name (str): the file name you want to save the plot to 
        """
        
        data = {
               'file_name':[file_name],
               'seed':[seed],
               'formula_x':[ inspect.getsource(formula[0]) ],
               'formula_y':[ inspect.getsource(formula[1]) ]
               }
        
        logfile_temp = pd.DataFrame ( data )
        
        logfile = pd.concat([logfile, logfile_temp])
        
        logfile.to_excel(self.logfile_path,index=False)
        
        print("logfile saved")
        
    
    def generate_data (self, formula, seed ):
        """generate the data for the plotting

        Args:
            formula (list): a list of length 2 and each index has a function to transform the data
            seed (int): the seed number

        Returns:
            DataFrame: return the data that is ready to be plotted
        """
        
        print("generate data")
        
        df = GenerativeArt.fixed_df.copy()
                        
        df['x'] = formula[0](df['x_i'].values,df['y_i'].values,seed)

        df['y'] = formula[1](df['x_i'].values,df['y_i'].values,seed)

        x_temp = df['x'].to_numpy()
        y_temp = df['y'].to_numpy()
        x_temp -= x_temp.min()
        x_temp = x_temp / x_temp.max() * 2 * np.pi

        df['radians'] = x_temp
        df['radius'] = y_temp

        return df

    def generate_plot (self, df, file_name_path, polar, filetype, s, alpha , lw, image_size, dpi, color, cmap, cmap_color, cmap_direction ,background_color):
        """generate the plot based on the inputs and save it to the file name that is provided

        Args:
            df (DataFrame): the data that is ready to be plotted
            file_name (str): the file name you want to save the plot to 
            polar (bool, optional): Whether you want to plot in the Cartesian or Polor coordincates where True = Polar and False = Cartesian. Defaults to False.
            filetype (str, optional): define the file type of the image you want to save to. Defaults to "png".
            s (int, optional): the size of the dots in the image. Defauls to 1
            alpha (int, optional): the transperancy of the plot. Defaults to 0.1
            lw (int, optional): is the line width of the plot. Defaults to 0.1
            image_size (tuple, optional): the size of the image. Defaults to (5,5)
            dpi (int, optional): the resolution of the plot. Defaults to 1000
            color (str, optional): the color of the dots on the plot. Defaults to 'black.
            cmap (bool, optional): if you want the color to be continuous. Defaults to False
            cmap_color (str/list, optional): this can be a string for a builtin cmap or you can pass a multiple colors and it will create the cmap for you. Defaults to 'plasma_r'  
            cmap_direction (str, optional): the direction in which you want the color to propogate can be either H for horizontal or V for vertical. Defaults to Vertical
            background_color (str, optional): the color of the background of the plot. Defaults to 'white'.
        """
        
        print("generate plot")

        plt.figure(facecolor=background_color, figsize = image_size)      

        if polar == True:

            ax = plt.axes(polar=True)
            
            ax.set_aspect('equal')
            ax.axis('off')
            
            if cmap == True:

                if cmap_direction == 'H':

                    direction = 'radians'

                elif cmap_direction == 'V':

                    direction = 'radius'

                if type(cmap_color) is list:
                    
                    cmap_color = LinearSegmentedColormap.from_list('cmap', cmap_color, N = 100)

                ax.scatter(x=df['radians'], y=df['radius'], s= s , alpha=alpha, lw=lw, c=df[direction],cmap = cmap_color)

            elif cmap == False:

                ax.scatter(x=df['radians'], y=df['radius'], s= s , alpha=alpha, color=color,lw=lw)

            ax.set_rlim(df['radius'].min(), df['radius'].max())
            ax.set_theta_zero_location("N")  # set zero at the north (top)
            ax.set_theta_direction(-1) # go clockwise

        elif polar == False:

            ax = plt.axes()

            ax.set_aspect('equal')
            ax.axis("off")

            if cmap == True:

                if cmap_direction == 'H':

                    direction = 'x'

                elif cmap_direction == 'V':

                    direction = 'y'

                if type(cmap_color) is list:
                    
                    cmap_color = LinearSegmentedColormap.from_list('cmap', cmap_color, N = 100)

                ax.scatter(x=df['x'], y=df['y'], s= s , alpha=alpha, lw=lw, c=df[direction],cmap = cmap_color)

            elif cmap == False: 
                
                ax.scatter(x=df['x'], y=df['y'], s=s, alpha=alpha, color=color,lw=lw)

        plt.savefig(file_name_path, dpi = dpi)

        plt.clf()

    
    def generate_animation(self, df, file_name_path, polar, filetype, s, alpha , lw, image_size, dpi, color, cmap, cmap_color, cmap_direction ,background_color, interval, num_partitions ):
        """generate the animation based on the inputs and save it to the file name that is provided

        Args:
            df (DataFrame): the data that is ready to be plotted
            file_name (str): the file name you want to save the plot to 
            polar (bool, optional): Whether you want to plot in the Cartesian or Polor coordincates where True = Polar and False = Cartesian. Defaults to False.
            filetype (str, optional): define the file type of the image you want to save to. Defaults to "png".
            s (int, optional): the size of the dots in the image. Defauls to 1
            alpha (int, optional): the transperancy of the plot. Defaults to 0.1
            lw (int, optional): is the line width of the plot. Defaults to 0.1
            image_size (tuple, optional): the size of the image. Defaults to (5,5)
            dpi (int, optional): the resolution of the plot. Defaults to 1000
            color (str, optional): the color of the dots on the plot. Defaults to 'black.
            cmap (bool, optional): if you want the color to be continuous. Defaults to False
            cmap_color (str/list, optional): this can be a string for a builtin cmap or you can pass a multiple colors and it will create the cmap for you. Defaults to 'plasma_r'  
            cmap_direction (str, optional): the direction in which you want the color to propogate can be either H for horizontal or V for vertical. Defaults to Vertical
            background_color (str, optional): the color of the background of the plot. Defaults to 'white'.
            animate (bool, optional): whether you want to animate the plot or not. Defaults to False
            interval (int, optional): the interval time in milliseconds in which you want to plot. Defaults to 1
            num_partitions (int, optional): the amount of transitions you want to have in your animation. Defaults to 20
        """

        print("generate animation")

        norm = None 

        direction = None 

        if polar == False:

            figure = plt.figure(facecolor=background_color, figsize = image_size )      

            ax = plt.axes()

            left = df['x'].min()
            right = df['x'].max()
            down = df['y'].min()
            up = df['y'].max()

            ax.set_xlim(left, right)
            ax.set_ylim(down, up)
            ax.set_aspect('equal')
            ax.axis("off")

            if cmap == True:

                if cmap_direction == 'H':

                    direction = 'x'

                elif cmap_direction == 'V':

                    direction = 'y'

                norm = matplotlib.colors.Normalize( vmin= df[direction].min(), vmax= df[direction].max() )

                if type(cmap_color) is str:

                    cmap_color = matplotlib.cm.get_cmap(cmap_color)

                elif type(cmap_color) is list:
                    
                    cmap_color = LinearSegmentedColormap.from_list('cmap', cmap_color, N = 100)

                scatter = ax.scatter(x=[0], y=[0], s=s, alpha=alpha, lw= lw, c= [0],cmap = cmap_color)
            
            elif cmap == False:

                scatter = ax.scatter(x=[0], y=[0], s=s, alpha=alpha, color=color,lw= lw)

            partitions = np.ceil ( np.linspace(0, len(df)+1, num=num_partitions) ).astype(int).tolist()

            anim = FuncAnimation(fig = figure, func = self.animate_img, frames= partitions, fargs = (scatter, df, polar, cmap,  cmap_color, norm, direction),
                interval=interval, blit=True)

            anim.save(file_name_path)
        
        elif polar == True:

            figure = plt.figure(facecolor=background_color, figsize = image_size) 

            ax = plt.axes(polar=True)
            
            left = df['x'].min()
            right = df['x'].max()
            down = df['y'].min()
            up = df['y'].max()

            ax.set_rlim(df['radius'].min(), df['radius'].max())
            ax.set_theta_zero_location("N")  # set zero at the north (top)
            ax.set_theta_direction(-1) # go clockwise

            ax.set_aspect('equal')
            ax.axis("off")

            if cmap == True:

                if cmap_direction == 'H':

                    direction = 'radians'

                elif cmap_direction == 'V':

                    direction = 'radius'

                norm = matplotlib.colors.Normalize( vmin= df[direction].min(), vmax= df[direction].max() )

                if type(cmap_color) is str:

                    cmap_color = matplotlib.cm.get_cmap(cmap_color)

                elif type(cmap_color) is list:
                    
                    cmap_color = LinearSegmentedColormap.from_list('cmap', cmap_color, N = 100)
            
                scatter = ax.scatter(x=[0], y=[0], s=s, alpha=alpha, lw= lw, c= [0],cmap = cmap_color)
            
            elif cmap == False:

                scatter = ax.scatter(x=[0], y=[0], s=s, alpha=alpha, color=color,lw= lw)

            partitions = np.ceil ( np.linspace(0, len(df)+1, num=num_partitions) ).astype(int).tolist()

            anim = FuncAnimation(fig = figure, func = self.animate_img, frames= partitions, fargs = (scatter, df, polar, cmap, cmap_color, norm, direction),
                interval=interval, blit=True)

            anim.save(file_name_path)

        plt.clf()
    
    def animate_img (self, i, scatter, df, polar, cmap, cmap_color, norm, direction ):
        """the function that generates the animation

        Args:
            i (int): is the partition in which the animation will be plotted on
            scatter (matplotlib.scatter): is the scatter plot that you want to animte 
            df (DataFrame): the data that is ready to be plotted
            polar (bool, optional): Whether you want to plot in the Cartesian or Polor coordincates where True = Polar and False = Cartesian. Defaults to False.
            cmap (bool, optional): if you want the color to be continuous. Defaults to False
            cmap_color (str/list, optional): this can be a string for a builtin cmap or you can pass a multiple colors and it will create the cmap for you. Defaults to 'plasma_r' 
            norm (matplotlib.colors.Normalize): it is the normalizer for the cmap that you created
            direction (str): it is the direction in which you want the colors to be propogated

        Returns:
            scatter (matplotlib.scatter): the updated animation after each partition
        """

        if polar == False:

            if cmap == True:

                scatter.set_offsets( np.c_[ df['x'].iloc[:i], df['y'].iloc[:i] ] )
                scatter.set_color(cmap_color(norm( df[direction].iloc[:i])))

            elif cmap == False:

                scatter.set_offsets( np.c_[ df['x'].iloc[:i], df['y'].iloc[:i] ] )
    
            return scatter,
        
        elif polar == True :

            if cmap == True:

                scatter.set_offsets( np.c_[ df['radians'].iloc[:i], df['radius'].iloc[:i] ] )
                scatter.set_color(cmap_color(norm( df[direction].iloc[:i])))

            elif cmap == False:

                scatter.set_offsets( np.c_[ df['radians'].iloc[:i], df['radius'].iloc[:i] ] )
    
            return scatter,
        
    def regenerate_img (self, filename,  polar = True, filetype = 'png', s = 1, alpha = 0.1, lw = 0.1, image_size = (5,5), dpi = 1000, color = 'black', cmap = False, cmap_color = 'plasma_r', cmap_direction = 'V', background_color = 'white', animate = False, interval = 1, num_partitions = 20 ):
        """regenerating an image/animation that is existant in the logfile and saving the image

        Args:
            filename (str): The name of the file that you want to regenrate
            polar (bool, optional): Whether you want to plot in the Cartesian or Polor coordincates where True = Polar and False = Cartesian. Defaults to False.
            filetype (str, optional): define the file type of the image you want to save to. Defaults to "png".
            s (int, optional): the size of the dots in the image. Defauls to 1
            alpha (int, optional): the transperancy of the plot. Defaults to 0.1
            lw (int, optional): is the line width of the plot. Defaults to 0.1
            image_size (tuple, optional): the size of the image. Defaults to (5,5)
            dpi (int, optional): the resolution of the plot. Defaults to 1000
            color (str, optional): the color of the dots on the plot. Defaults to 'black.
            cmap (bool, optional): if you want the color to be continuous. Defaults to False
            cmap_color (str/list, optional): this can be a string for a builtin cmap or you can pass a multiple colors and it will create the cmap for you. Defaults to 'plasma_r'  
            cmap_direction (str, optional): the direction in which you want the color to propogate can be either H for horizontal or V for vertical. Defaults to V
            background_color (str, optional): the color of the background of the plot. Defaults to 'white'.
            animate (bool, optional): whether you want to animate the plot or not. Defaults to False
            interval (int, optional): the interval time in milliseconds in which you want to plot. Defaults to 1
            num_partitions (int, optional): the amount of transitions you want to have in your animation. Defaults to 20

        """

        print("\nRegenerating Image :")

        try:

            seed = int ( filename.split('.')[0].split('_')[2] )

        except:
            print()
            raise Exception("This file name does not exist in the logfile")

        logfile = self.check_logfile_existence()

        df = self.get_data_from_logfile(filename, logfile, seed)
        
        file_name, file_name_path = self.generate_filename(seed, filetype)
        
        if animate == False:
                        
            plot = self.generate_plot(df, file_name_path, polar, filetype, s, alpha , lw, image_size, dpi, color, cmap, cmap_color, cmap_direction ,background_color )
        
        elif animate == True:

            animation = self.generate_animation(df, file_name_path, polar, filetype, s, alpha , lw, image_size, dpi, color, cmap, cmap_color, cmap_direction ,background_color, interval, num_partitions)
                


    def get_data_from_logfile (self, filename, logfile, seed):
        """return the dataframe from the logfile 

        Args:
            filename (str): The name of the file that you want to regenrate
            logfile (DataFrame): the dataframe that contains the logfile entities
            seed (int): the seed number

        Raises:
            Exception: If the file name that you want to regenerate does not exist

        Returns:
            DataFrame: return the data for the regenerated image that is ready to be plotted
        """

        df = GenerativeArt.fixed_df.copy()

        logfile = logfile[logfile['file_name'] == filename]

        if len(logfile) == 0:
            raise Exception("This file name does not exist in the logfile")

        my_formula = [ logfile['formula_x'].values[0], logfile['formula_y'].values[0] ]

        transform_x = my_formula[0].split('\n')
        transform_x.append( "df['x'] = transform_x(df['x_i'],df['y_i'], "+str(seed)+")" )

        transform_y = my_formula[1].split('\n')
        transform_y.append( "df['y'] = transform_y(df['x_i'],df['y_i'], "+str(seed)+")" )

        transform_x = '\n'.join(transform_x)
        transform_y = '\n'.join(transform_y)

        exec(transform_x)
        exec(transform_y)

        return df



if __name__ == '__main__':
    
    pass
    

