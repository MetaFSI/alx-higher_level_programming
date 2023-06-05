#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - link single list
 * @n: integer
 * @next: points to the next node
 *
 * Description: link a single list node structure
 * for Python - Hello, World 10-13 tasks.
 */
typedef struct intList_s
{
	int n;
	struct IntList_s *next;
} intList_t;

size_t print_listint(const intList_t *h);
listint_t *add_nodeint(intList_t **head, const int n);
void free_listint(intList_t *head);
int checking(intList_t *lsTT);

#endif /* LISTS_H */

