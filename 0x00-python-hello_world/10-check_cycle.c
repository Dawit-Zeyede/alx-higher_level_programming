#include "lists.h"
int check_cycle(listint_t *list)
{
	listint_t *current;

	current = list;
	while (current->next != NULL)
	{
		if (current->next == list)
			return (1);
		current = current->next;
	}
	return (0);
}
