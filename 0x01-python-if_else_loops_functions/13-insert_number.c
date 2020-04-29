#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node -  inserts a number into a sorted singly linked list.
 *
 * @head: sorted linked list.
 * @number: number for the new node
 *
 * Return: the address of the new node, or NULL if it failed
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;

	if (head)
	{
		current = *head;

		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);

		new->n = number;
		new->next = NULL;

		if (*head == NULL)
			*head = new;
		else
		{
			while (current->next != NULL)
			{
				if (current->n < number && current->next->n >= number)
				{
					new->next = current->next;
					current->next = new;
					break;
				}
				current = current->next;
						}
			current->next = new;
		}
		return (new);
	}
	return (NULL);
}
