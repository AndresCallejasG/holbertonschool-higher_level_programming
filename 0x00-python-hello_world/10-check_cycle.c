#include "lists.h"
/**
 * check_cycle - checks if there is a loop.
 *
 * @list: linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cyclearray
 */
int check_cycle(listint_t *list)
{

	listint_t *aux_slow = list, *aux_fast = list;

	while (aux_slow && aux_fast && aux_fast->next)
	{
		aux_slow = aux_slow->next;
		aux_fast = aux_fast->next->next;
		if (aux_slow == aux_fast)
			return (1);
	}
	return (0);
}
