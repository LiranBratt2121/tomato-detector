class ObjDistanceFinder:
    def __init__(self, focal_length, real_width, width_in_frame):
        self._focal_length = focal_length
        self.real_width = real_width
        self.width_in_frame = width_in_frame

    @property
    def focal_length(self):
        return self._focal_length

    @focal_length.setter
    def focal_length(self, calculated_focal_length):
        self._focal_length = calculated_focal_length

    def calculate_focal_length(self, width_in_rf_image: float, measured_distance: float):
        self.focal_length = (width_in_rf_image * measured_distance) / self.real_width

    def find_distance(self):
        return (self.real_width * self.focal_length) / self.width_in_frame
