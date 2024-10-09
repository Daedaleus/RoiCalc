import pandas


class DataSet:
    """
    A class to represent a data set.

    Attributes
    ----------
    rois : list t of ROIs
    applications : list of applications
    """
    def __init__(self):
        """
        Constructs all the necessary attributes for the data set object.

        :param rois: a list of ROIs
        :param applications: a list of applications


        """
        self.rois = []
        self.applications = []

    def add_application(self, application):
        """
        Add an application to the data set

        :param application: an application object
        """
        self.applications.append(application)

    def do_applications(self):
        """
        Perform all applications in the data set
        """
        for application in self.applications:
            for roi in self.rois:
                roi.add_result(application.start, application.end)
            mean_amplitude = 0
            for roi in self.rois:
                mean_amplitude += roi.results[-1].amplitude
            mean_amplitude = mean_amplitude / len(self.rois)
            application.mean_amplitude = mean_amplitude

    def export_to_excel(self):
        """
        Export the data set to an excel file
        """
        output_name = input("Enter the output file name: ")
        data = [["ROI", "Base", "Peak", "Normalized Base", "Normalized Peak", "Amplitude"]]
        for roi, i in zip(self.rois, range(1, len(self.rois)+1)):
            for result in roi.results:
                data.append([i, result.baseline, result.peak, result.normalized_baseline, result.normalized_peak, result.amplitude])

        for roi, i in zip(self.rois, range(1, len(self.rois)+1)):
            data.append([i,roi.results[-1].baseline,
                         roi.results[-1].peak, roi.results[-1].normalized_baseline, roi.results[-1].normalized_peak, roi.results[-1].amplitude])
        with pandas.ExcelWriter(f"../output/${output_name}.xlsx") as writer:
            df = pandas.DataFrame(data)
            df.to_excel(writer, sheet_name="Sheet1")