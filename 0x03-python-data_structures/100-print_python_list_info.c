#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - print info about python
 * @p: python object list
*/

void print_python_list_info(PyObject *p)
{
	long int size = Py_Size(p);
	int i, alloc;

	alloc = ((PyListObject *)p)->allocated;

	printf("[*] size of the Python List = %li\n", size);
	printf("[*] Allocated = %d\n", alloc);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
