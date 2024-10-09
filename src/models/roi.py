from src.models.roi_result import RoiResult


class Roi:
    """
    Region of Interest class to store data points and results for a region of interest.

    Attributes:
    data_points: List of data points for the region of interest.
    results: List of results for the region of interest.
    """
    def __init__(self, data_points):
        """
        Initialize the Region of Interest class with data points and an empty list of results.

        :param data_points: List of data points for the region of interest.
        """
        self.data_points = data_points
        self.results = []

    def get_by_row_number(self, row_number):
        """
        Get data point by row number

        :param row_number: Number of the row to get the data point from.
        :return: Roi data point
        """
        return self.data_points[row_number+3]

    def get_max_inbetween(self, row_start, row_end):
        """
        Get the maximum value in between two rows

        :param row_start: Starting row for comparison.
        :param row_end: Ending row for comparison.
        :return: Maximum value in between the two rows.
        """
        max_value = 0
        for i in range(row_start + 3, row_end + 3):
            if self.data_points[i].value > max_value:
                max_value = self.data_points[i].value
        return max_value


    def calculate_baseline(self, row_number) -> float:
        """
        Calculate the baseline for a specific row number

        :param row_number: Number of the row to calculate the baseline for.
        :return: Baseline value for the row.
        """
        baseline = 0
        for i in range(row_number - 40, row_number):
            baseline += self.data_points[i].value
        return baseline / 40

    def add_result(self, start, end):
        """
        Add a result to the region of interest

        :param start: Start row number for the region of interest.
        :param end: End row number for the region of interest.
        """
        peak = self.get_max_inbetween(start, end)
        baseline = self.calculate_baseline(start)
        self.results.append(RoiResult(peak, baseline))
