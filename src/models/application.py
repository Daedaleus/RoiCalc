class Application:
    """
    A class to represent an application.

    Attributes:
    name: The name of the application.
    data_sets: A list of data sets.
    mean_amplitude: The mean amplitude of the application.
    """
    def __init__(self, start, end):
        """
        Constructs all the necessary attributes for the application object.

        :param start: Start frame of the application.
        :param end: End frame of the application.
        """
        self.start = start
        self.end = end
        self.mean_amplitude = 0
