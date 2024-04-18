#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - Main function that create zombies
 * Return: Always 0 on sucess
 */
int main(void)
{
	int pid, i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(2);
		}
		else
			exit(0);
	}

	infinite_while();

	return (0);
}

/**
 * infinite_while - sleeeeep
 * Return: Always 0 (sucess)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
