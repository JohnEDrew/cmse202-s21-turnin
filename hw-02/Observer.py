from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

# Finish the new Observer class!
class Observer():
    '''
    This class creates an artificial night sky observer.
    '''
    
    # This function will get called automatically
    # when a new "observer" is created
    def __init__(self,im1_filename,im2_filename):
        '''
        When initializing the observer, the "red" image should be given
        as the first input argument and the "ir" image should be the second input
        '''
        self.im1_filename = im1_filename
        self.im2_filename = im2_filename
        self.load_images(im1_filename,im2_filename)
        
    def load_images(self,im1_filename,im2_filename):
        '''
        This function reads in the header and data of two file and assigns them to to respective attributes.
        '''
        self.im1_header = fits.open(im1_filename)
        self.im1_data = fits.getdata(im1_filename)
        self.im2_header = fits.open(im2_filename)
        self.im2_data = fits.getdata(im2_filename)
        
    def calc_stats(self):
        ''' This function calculates and prints the mean and standard deviation for both image files.
        '''
        print('Mean of im1: ', np.mean(self.im1_data))  
        print('Std of im1: ', np.std(self.im1_data))
        print('Mean of im2: ', np.mean(self.im2_data))
        print('Std of im2: ', np.std(self.im2_data))
       
    
    def make_composite(self):
        '''
        This function is incomplete! Make sure to finish it and
        then update this docstring to explain what the function does!
        '''
        
        # Define the array for storing RGB values
        rgb = np.zeros((self.im1_data.shape[0],self.im1_data.shape[1],3))
        
        # Define a normalization factor for our denominator using the R filter image
        norm_factor = self.im1_data.astype("float").max()
        
        # Compute the red channel values and then clip them to ensure nothing is > 1.0
        rgb[:,:,0] = 1.5 * (self.im2_data.astype("float")/norm_factor)
        rgb[:,:,0][rgb[:,:,0] > 1.0] = 1.0