#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int checking(intList_t *lsTT)
{
	intList_t *slowing = lsTT;
	intList_t *fasting = lsTT;

	if (!lsTT)
		return (0);

	while (slowing && fasting && fasting->next)
	{
		slowing = slowing->next;
		fasting = fasting->next->next;
		if (slowing == fasting)
			return (1);
	}

	return (0);
}
