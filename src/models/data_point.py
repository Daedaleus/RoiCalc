class DataPoint:
    """
    A class to represent a data point.

    Attributes:
    time: The time of the data point.
    value: The value of the data point.
    """
    def __init__(self, time, value):
        """
        Constructs a new DataPoint object.
        :param time:
        :param value:
        """
        self.time = time
        self.value = value
