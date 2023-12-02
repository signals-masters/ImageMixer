class Gallery():
    def __init__(self):
        self.ids_to_objs = {}
    
    def add_image(self, img_obj, img_id):
        self.ids_to_objs[img_id] = img_obj
    
    def get_gallery(self):
        return self.ids_to_objs 
    
    def crop_imgs(self, x, y , width, height):
        for _, img in self.ids_to_objs.items():
            current_img = img.get_img()
            img.set_img(current_img[y:y+height, x:x+width])
            img.set_shape((width, height))
            img.compute_fourier_transform()

            
            