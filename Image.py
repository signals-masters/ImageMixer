import cv2
import numpy as np
import matplotlib.pyplot as plt
import warnings
import logging

# Logging
logger = logging.getLogger(__name__)



class Image():

    id = 0
    def __init__(self):

        """
        Initialize an Image object.

        Attributes:
        - name (str): The name of the image extracted from the file path.
        - img (numpy.ndarray): The image data loaded from the specified path.
        - shape (tuple): The shape of the loaded image.
        - fft (numpy.ndarray): The 2D Fourier Transform of the image.
        - fft_shifted (numpy.ndarray): The shifted version of the Fourier Transform.
        - mag (numpy.ndarray): The magnitude spectrum of the shifted Fourier Transform.
        - phase (numpy.ndarray): The phase spectrum of the shifted Fourier Transform.
        - real (numpy.ndarray): The real part of the shifted Fourier Transform.
        - imaginary (numpy.ndarray): The imaginary part of the shifted Fourier Transform.
        - components_shifted (None): Placeholder for components of the shifted Fourier Transform.
        """
        self.id = Image.id
        Image.id += 1
        self.img_back_up = None
        self.img = None
        self.shape = None

        self.fft = None
        self.fft_shifted = None
        self.mag = None
        self.phase = None
        self.real = None
        self.imaginary = None
        self.components_shifted = None
        self.type_to_component = None # contatiner for the types mapped to components of the shifted Fourier Transform

    ######################################Encapsulation Layer####################################################
    def get_id(self):
        return self.id
    
    def get_img(self):
        return self.img.T
    
    def set_img(self, img):
        self.img = img
    
    def get_shape(self):
        return self.shape
    
    def set_shape(self, shape):
        self.shape = shape
    
    def get_fft(self):
        return self.fft
    
    def get_fft_shifted(self):
        return self.fft_shifted
    
    def get_mag(self):
        return self.components_shifted[0]
    
    def get_phase(self):
        return self.components_shifted[1]
    
    def get_real(self):
        return self.components_shifted[2]
    
    def get_imaginary(self):
        return self.components_shifted[3]
    
    def get_components_shifted(self):
        return self.components_shifted
    
    ##################################__main__functions__#######################################################
        
    def load_img(self, pth, show=False):

        """
        Load and process the image from the specified file path.

        Parameters:
        - show (bool, optional): If True, display the loaded image using cv2.imshow.
                                Default is True.

        Raises:
        - Exception: Raises an exception if there's an error loading or processing the image.

        Returns:
        - None
        """

        # try:
        self.img = cv2.imread(pth).astype(np.float32)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.shape = self.img.shape
        self.img_back_up = self.img.copy()

        if show:
            # cv2.imshow('Image', self.img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            # return plt.imshow(self.img, cmap='gray').
            plt.imsave("./imgs/1.png" , self.img)
        # except:
            # print(f"Error: Couldn't load the image at {pth}")

    def reshape(self, new_height, new_width):
        """
        Resize the image to the specified dimensions.

        Parameters:
        - new_height (int): The new height of the image.
        - new_width (int): The new width of the image.

        Returns:
        - None
        """
        # Resize the image
        self.img = cv2.resize(self.img, (new_width, new_height))
        # Update the shape attribute
        self.shape = self.img.shape

    @classmethod
    def reshape_all(cls, image_instances):
        """
        Resize all images in a list of Image instances to the smallest dimensions among them.

        Parameters:
        - cls (class): The class reference.
        - image_instances (list): List of Image instances to be resized.

        Returns:
        - None
        """
        # Find the smallest image dimensions among all instances
        min_height = min(inst.img.shape[0] for inst in image_instances)
        min_width = min(inst.img.shape[1] for inst in image_instances)

        # Resize all images to the smallest dimensions
        for inst in image_instances:
            inst.reshape(min_height, min_width)
            inst.compute_fourier_transform()

    def compute_fourier_transform(self, show=True):
        """
        Compute the 2D Fourier Transform and related components of the image.

        Parameters:
        - show (bool, optional): If True, display visualizations of the Fourier Transform components.
                                Default is True.

        Returns:
        - None
        """
        # Compute the 2D Fourier Transform
        self.fft = np.fft.fft2(self.img)

        # Shift the zero-frequency component to the center
        self.fft_shifted = np.fft.fftshift(self.fft)

        # Compute the magnitude of the spectrum
        self.mag = np.abs(self.fft)

        # Compute the phase of the spectrum
        self.phase = np.angle(self.fft)

        # real ft components
        self.real = self.fft.real

        #imaginary ft components
        self.imaginary = self.fft.imag

        # Compute the components of the shifted Fourier Transform
        self.components_shifted=[np.log(np.abs(self.fft_shifted)+1) , np.angle(self.fft_shifted) , np.log(self.fft_shifted.real+1) , np.log(self.fft_shifted.imag+1)]

        #contruct a dictionary to map each component to its type
        self.type_to_component = dict(zip(["magnitude", "phase", "real", "imaginary"], self.components_shifted))

    def change_brightness(self, img, brightness_factor):
        """
        Change the brightness of the image.

        Parameters:
        - brightness_factor (float): The factor by which to change the brightness.

        Returns:
        - None
        """
        # Change the brightness of the image
        return np.clip(img + brightness_factor , 0, 255.0)
    
    def change_contrast(self, img, contrast_factor):
        """
        Change the contrast of the image.

        Parameters:
        - contrast_factor (float): The factor by which to change the contrast.

        Returns:
        - None
        """
        # Change the contrast of the image
        return np.clip(img * contrast_factor , 0, 255.0)
    
    def plot(self, gamma=1, contrast_factor=1, brightness_factor=0, plot_components=True, plot_img=True):

        # Plot the image components
        if plot_components:
            for comp in self.components_shifted:
                #gamma correction
                #comp = np.power(comp, gamma)S

                # Apply Contrast
                if contrast_factor:
                    comp = self.change_contrast(comp, contrast_factor)

                # Apply Brightness    
                if brightness_factor:
                    comp = self.change_brightness(comp, brightness_factor)
                
                # Show
                plt.imshow(comp, cmap='gray')
                plt.gca().invert_yaxis()
                plt.show()

        # plot the image itself
        if plot_img:
            img = self.img.copy()
            #gamma correction
            #self.img = np.power(self.img, gamma)
            if contrast_factor:
                img = self.change_contrast(img, contrast_factor)
            if brightness_factor:
                img = self.change_brightness(img, brightness_factor)

            plt.imshow(img, cmap='gray')
            plt.show()


    


# # Example usage:
joker = Image()
me = Image()
moza = Image()

# # # Load images
joker.load_img("joker_PNG35.png")
me.load_img("Screenshot 2023-08-22 182109.png")
moza.load_img("moza1.png")

# # # # # Print initial shapes
# # # # print(joker.shape)
# # # # print(me.shape)

# # # Reshape all images to the smallest dimensions
Image.reshape_all([joker, me, moza])

# # # # # Print shapes after reshaping
# # # # print(joker.shape)
# # # # print(me.shape)


# me.compute_fourier_transform()
# moza.compute_fourier_transform()
# joker.compute_fourier_transform()
# moza.plot()

# # # # im = pil_image.fromarray(me)
# # # # contrast_enhancer = ImageEnhance.Contrast(im)
# # # # plt.imshow(contrast_enhancer.enhance(5), cmap='gray')
# # # # plt.show()

# x = np.fft.ifft2(joker.real + 1j * me.imaginary)
# plt.imshow(np.abs(x), cmap='gray')
# plt.show()