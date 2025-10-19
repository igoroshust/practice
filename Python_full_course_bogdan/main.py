import traceback

try:
    x = 1 / 0
except Exception as e:
    print('---')
    exception_traceback = traceback.format_exc()
    print(exception_traceback)