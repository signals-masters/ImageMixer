class Gallery():
    def __init__(self):
        self.ids_to_objs = {}
    
    def add_image(self, img_obj, img_id):
        self.ids_to_objs[img_id] = img_obj
    
    def get_gallery(self):
        return self.ids_to_objs