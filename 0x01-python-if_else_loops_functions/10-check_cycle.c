#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to heqd of the list
 * @number: number to add to list
 *
 * Return: pointer to new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *start = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (start == NULL || start->n >= number)
	{
		new->next = start;
		*head = new;
		return (new);
	}

	while (start && start->next && start->next->n < number)
		start = start->next;
	new->next = start->next;
	start->next = new;

	return (new);
}
