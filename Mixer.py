import numpy as np
from OutputImage import OutputImage
from Gallery import Gallery
from Image import Image
import matplotlib.pyplot as plt

class Mixer():

    def __init__(self, w1, w2, w3, w4, img_id1, img_id2, img_id3, img_id4, type_1, type_2, type_3, type_4):
        self.img_id1 = img_id1
        self.img_id2 = img_id2
        self.img_id3 = img_id3
        self.img_id4 = img_id4
        # types must be some real + some img or some mag. and some phase
        self.type_1 = type_1
        self.type_2 = type_2
        self.type_3 = type_3
        self.type_4 = type_4
        self.types = [type_1, type_2, type_3, type_4]
        # weights
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.w4 = w4
        self.weights = [w1, w2, w3, w4]
        
    def extract_img_from_gallery(self, gallery):
        img1 = gallery[self.img_id1]
        img2 = gallery[self.img_id2]
        img3 = gallery[self.img_id3]
        img4 = gallery[self.img_id4]
        return img1, img2, img3, img4
    
    def choose_mode(self):
        phase_mag = 0
        real_imag = 0
        for type in self.types:
            if type == "phase" or type == "magnitude":
                phase_mag += 1
            elif type == "real" or type == "imaginary":
                real_imag += 1
            else:
                raise ValueError("Invalid type")
        
        if phase_mag == 0:
            return 1
        elif real_imag == 0:
            return 2
        else:
            raise ValueError("Invalid types")  

    def inverse_fft(self, gallery):
        img_objs = self.extract_img_from_gallery(gallery)
        mode = self.choose_mode()
        if mode == 2:
            magnitudes = np.zeros(img_objs[0].shape)
            phases = np.zeros(img_objs[0].shape)

            for i, img_obj in enumerate(img_objs):
                if self.types[i] == "magnitude":
                    magnitudes += self.weights[i] * img_obj.mag
                elif self.types[i] == "phase":
                    phases += self.weights[i] * img_obj.phase

            print("using mag phase")
            return np.clip(np.abs(np.fft.ifft2(magnitudes * np.exp(1j * phases))), 0,225) 

        elif mode == 1:
            real = np.zeros(img_objs[0].shape)
            imaginary = np.zeros(img_objs[0].shape)

            for i, img_obj in enumerate(img_objs):
                if self.types[i] == "real":
                    real += self.weights[i] * img_obj.real
                elif self.types[i] == "imaginary":
                    imaginary += self.weights[i] * img_obj.imaginary

            print("using real imag")
            return np.clip(np.abs(np.fft.ifft2(real + imaginary * 1j)), 0, 225)


    

# gallery = Gallery()
# me = Image()
# joker = Image()
# moza1 = Image()
# moza2 = Image()
# print(me.id, joker.id, moza1.id, moza2.id)
# joker.load_img("joker_PNG35.png")
# me.load_img("Screenshot 2023-08-22 182109.png")
# moza1.load_img("moza1.png")
# moza2.load_img("moza2.png")
# Image.reshape_all([joker, me, moza1, moza2])
# me.compute_fourier_transform()
# joker.compute_fourier_transform()
# moza1.compute_fourier_transform()
# moza2.compute_fourier_transform()
# # me.plot()
# # joker.plot()
# # moza1.plot()
# # moza2.plot()
# gallery.add_image(me, me.id)
# gallery.add_image(joker, joker.id)
# gallery.add_image(moza1, moza1.id)
# gallery.add_image(moza2, moza2.id)
# g = gallery.get_gallery()
# mixer = Mixer(1,2/3, 1/3, 0, me.id, moza2.id, moza1.id, joker.id, "real", "imaginary", "imaginary", "imaginary")
# output = mixer.inverse_fft(g)
# output = OutputImage()
# output.img = output
# print(output)
# plt.imshow(output, cmap='gray')
# plt.title("mixer output")
# plt.show()

