#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct intList_s - linked list as single
 * @n: int variale
 * @suevent: suevent node to be pointed
 *
 * Description: linked list as single node structure
 * alx phyton hello
 */
typedef struct intList_s
{
	int n;
	struct intList_s *suevent;
} intList_t;

int checking(intList_t *listing);

#endif /* LISTS_H */
