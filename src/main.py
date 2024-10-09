from src.helper.helper import get_info_from_user, calculate_and_export

if __name__ == "__main__":
    '''Main function to run the program'''
    roi_count, applications_entries, data = get_info_from_user()
    calculate_and_export(applications_entries, roi_count, data)