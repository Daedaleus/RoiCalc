import pandas

from src.models import DataPoint, Application, DataSet, Roi


def import_from_excel(column_number: int, data: pandas.DataFrame) -> [DataPoint]:
    """Import data from excel

    Args:
        :param column_number: Column number
        :param data: Dataframe

    Returns:
        list: List of data points
    """
    data_points = []
    for i in range(3, len(data)):
        data_points.append(DataPoint(data.iloc[i, 0], data.iloc[i, column_number]))
    return data_points


def get_info_from_user():
    """Get the information from the user and return the roi count and applications entries

    Returns:
        tuple: roi count and applications entries
    """
    print("Copy excel file path and paste here")
    file_name = input()
    data = pandas.read_excel(file_name)
    count = data.columns.size - 2

    print("How many applications do you have?")
    applications = int(input())
    applications_entries = []
    for i in range(applications):
        application = Application(0, 0)

        print("Please enter the start of the {0}. application".format(i+1))
        application.start = int(input())

        print("Please enter the end of the {0}. application".format(i+1))
        application.end = int(input())
        applications_entries.append(application)
    return count, applications_entries, data


def calculate_and_export(applications: [Application], count: int, data: pandas.DataFrame):
    """Calculate and export the applications

    Args:
        :param applications: list of applications
        :param count: Amount of rois
        :param data: Dataframe
    """
    data_set = DataSet()
    for i in range(count):
        data_set.rois.append(Roi(import_from_excel(i + 2, data)))

    for application in applications:
        data_set.add_application(application)

    data_set.do_applications()
    data_set.export_to_excel()
