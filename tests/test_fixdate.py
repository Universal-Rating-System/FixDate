class TestCsvWrpr:
    def test_replace_with_actual_tests(self):
        x = 1
        y = 1
        assert x == y


# def do_tests(p_app_path='', p_cls=True):
#     '''Test the class methods.  Also called by the PackageIt PIP app to
#     test the module during PIP installation.
#
#     Parameters
#     - baseFolder    : Base folder for source code
#     - cls = True    : Clear the screen at start-up
#     '''
#
#     def basic_test(p_app_path=p_app_path):
#         '''Basic and mandatory scenario tests for certification of the class'''
#         success = True
#         # Below must be implemented.  Abandoned due to time pressure
#         # date = FixDate( _name, '21MAY17', p_in_format = 'DMY' )
#         # if date.date != datetime.date( 2021, 5, 17 ):
#         #     success = success and False
#         date = FixDate(_name, '  .  .  ', p_in_format='DMY')
#         if date.date is not None:
#             success = success and False
#         date = FixDate(_name, '.  .', p_in_format='DMY')
#         if date.date is not None:
#             success = success and False
#         date = FixDate(_name, '11.10.03', p_in_format='DMY')
#         if date.date != datetime.date(2003, 10, 11):
#             success = success and False
#         date = FixDate(_name, '11.10.68', p_in_format='DMY')
#         if date.date != datetime.date(1968, 10, 11):
#             success = success and False
#         date = FixDate(_name, '68.10.11', p_in_format='YMD')
#         if date.date != datetime.date(1968, 10, 11):
#             success = success and False
#         date = FixDate(_name, '10.11.68', p_in_format='MDY')
#         if date.date != datetime.date(1968, 10, 11):
#             success = success and False
#         date = FixDate(_name, '073 339 5214')
#         if date.date_str is not None and date.date is not None:
#             success = success and False
#         date = FixDate(_name, '19681011')
#         if date.date != datetime.date(1968, 10, 11):
#             success = success and False
#         date = FixDate(_name, '1968/10/11')
#         if date.date != datetime.date(1968, 10, 11):
#             success = success and False
#         date = FixDate(_name, '4/9/1996')
#         if date.date != datetime.date(1996, 9, 4):
#             success = success and False
#         date = FixDate(_name, '2001/9/8')
#         if date.date != datetime.date(2001, 9, 8):
#             success = success and False
#         date = FixDate(_name, '5/10/1976')
#         if date.date != datetime.date(1976, 10, 5):
#             success = success and False
#         date = FixDate(_name, '2000/4/21')
#         if date.date != datetime.date(2000, 4, 21):
#             success = success and False
#         date = FixDate(_name, '1968/10/1')
#         if date.date != datetime.date(1968, 10, 1):
#             success = success and False
#         date = FixDate(_name, '20-Oct-1968')
#         if date.date != datetime.date(1968, 10, 20):
#             success = success and False
#         date = FixDate(_name, '20-Oct-68')
#         if date.date != datetime.date(1968, 10, 20):
#             success = success and False
#         date = FixDate(_name, '20/10/1968')
#         if date.date != datetime.date(1968, 10, 20):
#             success = success and False
#         date = FixDate(_name, '00/00/00')
#         if date.date is not None:
#             success = success and False
#         date = FixDate(_name, '00-00-00')
#         if date.date is not None:
#             success = success and False
#         date = FixDate(_name, '2017-01-0I')
#         if date.date is not None:
#             success = success and False
#         date = FixDate(_name, '2017-02-30')
#         if date.date != datetime.date(2017, 2, 28):
#             success = success and False
#         date = FixDate(_name, '')
#         if date.date is not None:
#             success = success and False
#         date = FixDate(_name, '2017-20-10')
#         if date.date != datetime.date(2017, 10, 20):
#             success = success and False
#         date = FixDate(_name, '2017.20.10')
#         if date.date != datetime.date(2017, 10, 20):
#             success = success and False
#         date = FixDate(_name, '20.10.2017')
#         if date.date != datetime.date(2017, 10, 20):
#             success = success and False
#         date = FixDate(_name, '10.20.2017')
#         if date.date != datetime.date(2017, 10, 20):
#             success = success and False
#         date = FixDate(_name, '1900/00/00')
#         if date.date is not None:
#             success = success and False
#         beetools.result_rep(success, 'Done')
#         return success
#
#     # end basic_test
#
#     success = True
#     b_tls = beetools.Archiver(
#         _name, _VERSION, __doc__[0], p_app_path=p_app_path, p_cls=p_cls
#     )
#     logger = logging.getLogger(_name)
#     logger.setLevel(beetools.DEF_LOG_LEV)
#     file_handle = logging.FileHandler(beetools.LOG_FILE_NAME, mode='w')
#     file_handle.setLevel(beetools.DEF_LOG_LEV_FILE)
#     console_handle = logging.StreamHandler()
#     console_handle.setLevel(beetools.DEF_LOG_LEV_CON)
#     file_format = logging.Formatter(
#         beetools.LOG_FILE_FORMAT, datefmt=beetools.LOG_DATE_FORMAT
#     )
#     console_format = logging.Formatter(beetools.LOG_CONSOLE_FORMAT)
#     file_handle.setFormatter(file_format)
#     console_handle.setFormatter(console_format)
#     logger.addHandler(file_handle)
#     logger.addHandler(console_handle)
#
#     b_tls.print_header(p_cls=p_cls)
#     success = basic_test()
#     beetools.result_rep(success, 'Done')
#     b_tls.print_footer()
#     if success:
#         return b_tls.archive_path
#     return False
#
#
# # end do_tests
#
# if __name__ == '__main__':
#     do_tests(p_app_path=_path)
# # end __main__
