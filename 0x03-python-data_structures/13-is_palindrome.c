#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * list_len -  number of elements in a linked list_t list.
 *
 * @h: List
 *
 * Return: number of elements
 */
size_t list_len(const listint_t *h)
{
	int i = 0;
	const listint_t *current;

	if (h)
	{
		current = h;

		while (current)
		{
			current = current->next;
			i++;
		}
	}

	return (i);
}

/**
 * is_palindrome - 1 if a linked list is a palindrome and 0 if not.
 *
 * @head: list
 *
 * Return: 1 if a listint is a palindrome and
 * 0 if not.
 */

int is_palindrome(listint_t **head)
{
	const listint_t *current;
	int *array;
	int i, len;

	current = *head;

	len = list_len(*head);
	array = malloc(sizeof(int) * (len + 1));

	for (i = 0; current && i < len; i++, current = current->next)
	{
		array[i] = current->n;
	}
	for (i = 0; i <= ((len / 2) - 1); i++)
	{
		if (array[i] != array[len - 1 - i])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}
