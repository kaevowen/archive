#include <stdio.h>

int main()
{
	int n = 5;
	int i, j;
	int pivot = (int)((n+(n-1)) / 2);
	int k = n-1;
	
	for(i = 0 ; i < n * 2 ; i++)
	{
		for(j = 0 ; j < n+(n-1) ; j++)
		{
			if(j >= pivot - k && j <= pivot + k)
			{
				printf("*");
			}			
			
			else
			{	
				printf(" ");
			}
		}

		if(i >= (n*2) / 2)
		{
			if(k <= -1)
			{
				k+=2;
				continue;
			}	
			
			k++;
			puts("");
		}

		else
		{
			k--;
			puts("");
		}
	}
	
	return 0;
}
