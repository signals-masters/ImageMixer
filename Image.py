import cv2
import numpy as np
import matplotlib.pyplot as plt

class Image():
    
    def __init__(self, img_pth):
        self.path = img_pth
        self.name = img_pth.split('/')[-1]
        self.img = None
        self.shape = None

        self.fft = None
        self.fft_shifted = None
        self.mag = None
        self.phase = None
        self.real = None
        self.imaginary = None

    def load_img(self, show=True):
        try:
            self.img = cv2.imread(self.path)
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            self.shape = self.img.shape
            print(self.img.shape)

            if show:
                # Display the image (you can also perform further processing here)
                cv2.imshow('Image', self.img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        except:
            print(f"Error: Couldn't load the image at {self.path}")

    def reshape(self, new_height, new_width):
        # Resize the image
        self.img = cv2.resize(self.img, (new_width, new_height))
        # Update the shape attribute
        self.shape = self.img.shape

    @classmethod
    def reshape_all(cls, image_instances):
        # Find the smallest image dimensions among all instances
        min_height = min(inst.img.shape[0] for inst in image_instances)
        min_width = min(inst.img.shape[1] for inst in image_instances)

        # Resize all images to the smallest dimensions
        for inst in image_instances:
            inst.reshape(min_height, min_width)



    def compute_fourier_transform(self, show=True):
        # Compute the 2D Fourier Transform
        self.fft = cv2.dft(np.float32(self.img), flags=cv2.DFT_COMPLEX_OUTPUT)

        # Shift the zero-frequency component to the center
        self.fft_shifted = np.fft.fftshift(self.fft)

        # Compute the magnitude of the spectrum
        self.mag = 20*np.log(cv2.magnitude(self.fft_shifted[:,:,0],self.fft_shifted[:,:,1]))

        # Normalize the magnitude spectrum
        self.mag = cv2.normalize(self.mag, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)

        # Compute the phase of the spectrum
        self.phase = cv2.phase(self.fft_shifted[:,:,0], self.fft_shifted[:,:,1], angleInDegrees=True)

        #real ft components
        self.real = self.fft_shifted[:,:,0]

        #imaginary ft components
        self.imaginary = self.fft_shifted[:,:,1]


    def plot(self, arr, type):
        plt.figure(figsize=(8, 8))
        if type == 'magnitude': 
            plt.imshow(np.log1p(arr), cmap='gray')
        elif type == "phase":
            plt.imshow(arr, cmap='hsv')
            plt.colorbar()
        else:
            plt.imshow(arr, cmap='gray')

        plt.title(f'{self.name} {type}')
        plt.colorbar()
        plt.show()



        





# Example usage:
joker = Image("joker_PNG35.png")
me = Image("Screenshot 2023-08-22 182109.png")

# Load images
joker.load_img()
me.load_img()

# Print initial shapes
print(joker.shape)
print(me.shape)

# Reshape all images to the smallest dimensions
Image.reshape_all([joker, me])

# Print shapes after reshaping
print(joker.shape)
print(me.shape)

cv2.imshow('Image', joker.img)
cv2.waitKey(0)
cv2.imshow('Image', me.img)
cv2.waitKey(0)

me.compute_fourier_transform()
joker.compute_fourier_transform()
joker.plot(me.mag, 'magnitude')
joker.plot(me.phase, 'phase')
joker.plot(me.real, 'real')
joker.plot(me.imaginary, 'imaginary')
plt.plot(joker.imaginary, 'o')
plt.show()
