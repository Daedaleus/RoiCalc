class RoiResult:
    """
    Region of Interest Result class to store results for a region of interest.

    Attributes:
    peak: Peak value for the region of interest.
    baseline: Baseline value for the region of interest.
    normalized_baseline: Normalized baseline value for the region of interest.
    normalized_peak: Normalized peak value for the region of interest.
    amplitude: Amplitude value for the region of interest.
    """
    def __init__(self, peak, baseline):
        """
        Initialize the Region of Interest Result class with peak and baseline values.
        :param peak: Peak value for the region of interest.
        :param baseline: Baseline value for the region of interest.
        """
        self.peak = peak
        self.baseline = baseline
        self.normalized_baseline = baseline / baseline * 100
        self.normalized_peak = peak / baseline * 100
        self.amplitude = self.normalized_peak - self.normalized_baseline
