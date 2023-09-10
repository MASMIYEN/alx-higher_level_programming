#include "lists.h"
/**
 * is_palindron - checks if palindrom or not
 *
 * @head: header
 *
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return(1);
	return(aux_palind(head, *head));
}
/**
 * aux_palind- function to check for palindrom
 *
 * @head: header
 * @end: end of list
 *
 * Return: palindrome or not
 */
int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
