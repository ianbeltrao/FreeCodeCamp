class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
        
    def get_area(self, width, height):
        area = self.width * self.height
        return area
    
    def get_perimeter(self, width, height):
        perimeter = (2 * self.width) +  (2 * self.height)
        return perimeter

    def get_diagonal(self, width, height):
        diagonal = ((2 ** self.width + 2 ** self.height) ** .5)
        return diagonal

    def get_picture(self, width, height):
        