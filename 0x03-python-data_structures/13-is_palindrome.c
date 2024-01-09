#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a singly list is a palidrome
 * @head: pointer to pointer
 * Return: 0 if a palidrome is not, 1 if yes
*/
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (a_palind(head, *head));
}
/**
 * a_palind - know if is palindrome
 * @head: head list
 * @end: end list
 * Return: 1 if aux palind
*/
int a_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (a_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
