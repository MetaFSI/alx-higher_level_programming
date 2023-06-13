#include "lists.h"
/**
 * palindrome - Reverses a singly linked list.
 * @l:  Pointer to a pointer to the head node of the list.
 * @r: pointer of the node
 *
 * Return: Pointer to the head node of the reversed list.
 */
int palindrome(listint_t **l, listint_t *r)
{
	int response;

	if (r != NULL)
	{
		response = palindrome(l, r->next);
		if (response != 0)
		{
			response = (r->n == (*l)->n);
			*l = (*l)->next;
			return (response);
		}
		return (0);

	}
	return (1);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to a pointer to the head node of the linked list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL)
	{
		return (0);
	}
	return (palindrome(head, *head));
}
