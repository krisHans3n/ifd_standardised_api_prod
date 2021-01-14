import uuid


class ImageSolid:
    def __innit__(self):

        self.url = ""
        self.file_path = ""
        self.filetype = None
        self.guid = uuid.uuid4().hex

        self.height = None
        self.width = None
        self.size = None

        self.pixel_ratio = None
        self.resolution = None
        self.pixel_format = None

        self.authenticity_level = None
        self.pixel_vector = None

        self.metadata = None
        #self.metadata_type = self.metadata.get_type_md()
        #self.origin_date = self.metadata.get_origin_date()
        #self.author = self.metadata.get_author()
        #self.compression_type = self.metadata.get_compression_alg()
        #self.location = self.metadata.get_location_taken()

    def get_height(self):
        return self.height

    def get_file_path(self):
        return self.file_path

    def get_width(self):
        return self.width

    def get_guid(self):
        return self.guid

    def get_pixel_ratio(self):
        return self.pixel_ratio

    def get_resolution(self):
        return self.resolution

    def get_url(self):
        return self.url

    def get_metadata(self):
        return self.metadata

    def get_metadata_type(self):
        return self.metadata.get_type_md()

    def get_pixel_vector(self):
        return self.pixel_vector

    def get_origin_date(self):
        return self.metadata.get_origin_date()

    def get_authenticity_level(self):
        return self.authenticity_level

    def get_author(self):
        return self.metadata.get_author()

    def get_compression_type(self):
        return self.metadata.get_compression_alg()

    def get_color_bitmap_type(self):
        return self.color_bitmap_type

    def get_network_trace(self):
        return self.network_trace

    def get_network_stops(self):
        return self.network_stops

    def get_checksum(self):
        return self.checksum

    def get_location(self):
        return self.metadata.get_location_taken()

    def get_hash_type(self):
        return self.hash_type

    def get_brightness_pixel_vector(self):
        return self.brightness_pixel_vector


class ImageEmpty:
    def __init__(self):
        var = None
