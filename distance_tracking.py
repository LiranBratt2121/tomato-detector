class ObjDistanceFinder:
    def __init__(self, real_width_cm: float, width_in_frame_px: float, focal_length: float | None = None):
        self._focal_length = focal_length
        self.real_width_cm = real_width_cm
        self.width_in_frame_px = width_in_frame_px

    @property
    def focal_length(self):
        return self._focal_length

    @focal_length.setter
    def focal_length(self, calculated_focal_length):
        self._focal_length = calculated_focal_length

    def calculate_focal_length(self, measured_distance_cm: float):
        self.focal_length = (((self.width_in_frame_px * measured_distance_cm) / self.real_width_cm))

    def find_distance(self):
        return ((((self.real_width_cm * self.focal_length) / self.width_in_frame_px)) / 2)
