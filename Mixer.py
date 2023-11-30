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


        if w1 + w2 + w3 + w4 != 1:
            pass
            raise ValueError("Invalid weights")

        else:
            self.w1 = w1
            self.w2 = w2
            self.w3 = w3
            self.w4 = w4
            self.weights = [w1, w2, w3, w4]
        
        
    
    def extract_img_from_gallery(self, gallery):
        img1 = gallery[self.img_id1].type_to_component[self.type_1]
        img2 = gallery[self.img_id2].type_to_component[self.type_2]
        img3 = gallery[self.img_id3].type_to_component[self.type_3]
        img4 = gallery[self.img_id4].type_to_component[self.type_4]

        return img1, img2, img3, img4

    def mix(self, gallery):
        # there is a bug here 
        counter = 0
        phase_mag_flag = False
        real_imag_flag = False
        img1, img2, img3, img4 = self.extract_img_from_gallery(gallery)
        magnitudes = np.zeros_like(img1)
        phases = np.zeros_like(img1)
        real = np.zeros_like(img1)
        imaginary = np.zeros_like(img1)

        # cases: given phase and magnitudes // given real and imaginary
        # will fail if another compination is found
        for type , img in zip([self.type_1, self.type_2, self.type_3, self.type_4], [img1, img2, img3, img4]):
            if type == "magnitude":
                phase_mag_flag = True
                magnitudes += img * self.weights[counter]
            elif type == "phase":
                phase_mag_flag = True
                phases += img #* self.weights[counter]
            elif type == "real":
                real_imag_flag = True
                real += img
            elif type == "imaginary":
                real_imag_flag = True
                imaginary += img * self.weights[counter]
            else:
                raise ValueError("Unknown type")
            counter += 1
            if phase_mag_flag and real_imag_flag:
                raise ValueError("Can't mix phase and magnitude with real and imaginary")
        
        if phase_mag_flag:
            return 0,magnitudes , phases
        
        return 1,real, imaginary

    def inverse_fft(self, gallery):
        components = self.mix(gallery)
        fft = None
        if components[0] == 0:
            magnitude = components[1]
            phase = components[2]
            fft = magnitude * np.exp(1j * phase)
            print(fft.shape)
        else:
            real = components[1]
            imaginary = components[2]
            fft = real + 1j * imaginary

        return np.abs(np.fft.ifft2(fft))
    

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

# me.plot()
# joker.plot()
# moza1.plot()
# moza2.plot()

# gallery.add_image(me, me.id)
# gallery.add_image(joker, joker.id)
# gallery.add_image(moza1, moza1.id)
# gallery.add_image(moza2, moza2.id)

# g = gallery.get_gallery()
# print(g)
# mixer = Mixer(1,0, 0, 0, me.id, joker.id, moza1.id, moza2.id, "magnitude", "magnitude", "phase", "phase")

# output = mixer.inverse_fft(g)
# print(output)
# plt.imshow(output, cmap='gray')
# plt.title("mixer output")
# plt.show()

