#include <Python.h>
#include <object.h>
i#include <listobject.h>
#include <stdlib.h>
#include <stdio.h>

/**
* print_python_list_info - A fn to print python basics in C
* @p: Apoint
* Return: Nil
*/
void print_python_list_info(PyObject * p)
{
	long int size = PyList_Size(p);
	int a;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (a = 0; a < size; a++)
		printf("Element %i: %s\n", a, Py_TYPE(obj->ob_item[a])->tp_name);
}
