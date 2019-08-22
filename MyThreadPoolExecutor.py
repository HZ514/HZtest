"""
线程池
"""
from queue import Queue
from concurrent.futures import ThreadPoolExecutor, ALL_COMPLETED, wait


Emp_q = Queue()
T_list = []
employee_number_and_project_dict = {}


def select_data(name):
    pass


def request_t(emp_number_tuple):
    val = select_data(emp_number_tuple[0])
    print(emp_number_tuple)
    employee_number_and_project_dict[emp_number_tuple] = val
    T_list.append(val)


def concurrent_scan():
    all_task = []
    from os import cpu_count
    pool = ThreadPoolExecutor(cpu_count() + 1)

    for i in range(Emp_q.qsize()):
        task = pool.submit(request_t, Emp_q.get(), )
        all_task.append(task)
    wait(all_task, return_when=ALL_COMPLETED)


is_coding_tuple = (1, 2, 3, 4, 5)
for index, is_coding_col in enumerate(is_coding_tuple):
        Emp_q.put((index, is_coding_col))


concurrent_scan()


print(T_list)
print(employee_number_and_project_dict)
