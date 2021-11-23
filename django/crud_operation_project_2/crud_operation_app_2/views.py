from django.shortcuts import render
from .models import TestDataTable2,TestCaseStatus
# Create your views here.

def get_loader(request):
    return render(request, 'crud_operation_app_2/temp_loader.html')


def get_data(request):
    """THIS FUNCTION IS THE ENDPOINT FOR API CALL
    ALL DATA WILL BE FIRST GATHERED HERE AND THEN PASSED TO HTML USING AN OBJECT (here context)"""
    context = None

    test_data_table2_data = TestDataTable2_list()
    total_status_table_counts = TestDataTable2Counts()

    context = {
        'test_data': test_data_table2_data,
        'status_counts': total_status_table_counts
    }
    return render(request,'crud_operation_app_2/one_file.html', context)

def update_data(request):
    get_data(request)


def TestDataTable2_list():
    data = TestDataTable2.objects.all()
    return data

def TestDataTable2Counts():
    total_test_run = TestDataTable2.objects.exclude(status='ERROR').count()
    total_test_pass = TestDataTable2.objects.all().filter(status='PASS').count()
    total_tests_failed = TestDataTable2.objects.all().filter(status='FAIL').count()
    total_tests_running = TestDataTable2.objects.all().filter(status='RUNNING').count()

    status_counts = {
        'total_test_run' : total_test_run,
        'total_test_pass': total_test_pass,
        'total_test_failed': total_tests_failed,
        'total_test_running': total_tests_running

    }

    print(status_counts)
    return status_counts

#
# def TestDataTable2_list(request):
#     context = {'test_data' : TestDataTable2.objects.all(),
#                }
#     #return render(request,'crud_operation_app_2/crud_operation_list.html',context)
#     return render(request, 'crud_operation_app_2/one_file.html', context)

def TestDataTable2_form(request):
    return


def TestDataTable2_delete(request):
    return