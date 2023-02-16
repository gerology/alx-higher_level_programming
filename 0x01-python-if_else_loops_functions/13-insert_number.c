#include "lists.h"
#include <stdlib.h>

/**
 * listint_t *insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to address of node
 * @number: number to be inserted
 * Return - address of node, NULL if failed
 */

stint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t new_node;

	current = *head;
	new_node = malloc(sizeof(listint));

	current->next = NULL;
	current->n = number

	if (*head == NULL)
		return (NULL);
	else
	{
		while (current->next != NULL)
			current = current->next;
		current->next = new_node;
	}
	
}
