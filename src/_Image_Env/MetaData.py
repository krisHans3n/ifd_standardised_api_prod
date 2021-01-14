class MetaData:

    '''
    convert to dynamically adding attributes by passing in **kwargs and
    setting each key value pair
    attention will need to be given for when this class is used in other processes
    to make sure they know the attributes that exists with each class
    however, not necessary just now
    '''

    def __init__(self):
        self.data_raw = None
        self.file_type = None
        self.metadata_type = None
        self.origin_date = None
        self.author = None
        self.location = None
        self.compression_alg = None
        self.metadata_dict = None
        self.metadata_dict_indexlst = None

    def get_metadata_dict(self):
        return self.metadata_dict

    def get_file_type(self):
        return self.file_type

    def get_type_md(self):
        return self.metadata_type

    def get_origin_date(self):
        return self.origin_date

    def get_author(self):
        return self.author

    def get_compression_alg(self):
        return self.compression_alg

    def get_location_taken(self):
        return self.location

