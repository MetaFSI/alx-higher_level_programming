#include "lists.h"

/**
 * checking - checks if a cycle containing linked list
 * @listing: check linked list
 *
 * Return: in case 1 , list has a cycle, in case 0 it doesn't
 */
int checking(intList_t *listing)
{
	intList_t *slowing = listing;
	intList_t *fsting = listing;

	if (!listing)
		return (0);

	while (slowing && fsting && fsting->suevent)
	{
		slowing = slowing->suevent;
		fsting = fsting->suevent->suevent;
		if (slowing == fsting)
			return (1);
	}

	return (0);
}
