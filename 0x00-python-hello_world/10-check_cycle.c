#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if list is cycle
 * @list: pointer to list
 * Return: 0 if the list doesn't has cycle, 1 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
