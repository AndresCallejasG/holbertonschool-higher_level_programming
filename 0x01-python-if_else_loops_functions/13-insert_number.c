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
	listint_t *current, *prev;
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
			prev = NULL; 
			while (current != NULL && current->n < number)
			{
				prev = current;				
				current = current->next;
			}
			new->next = current;
			if (prev != NULL)
				prev->next = new;
			else
				*head = new;			
		}
		return (new);
	}
	return (NULL);
}
