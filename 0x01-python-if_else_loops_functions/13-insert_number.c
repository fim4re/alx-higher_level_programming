#include "lists.h"

/**
 * insert_node - inserts number in sorted list
 * @head: head pointer
 * @number: number to insert
 * Return: inserted node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = next;

	return (new);
}
