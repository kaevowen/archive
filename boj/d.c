#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <ctype.h>
#define EXCEED 2670
#define len(a) ( sizeof(a) / sizeof(*a) )

void RNG( int low, int high );
void Sort( void );
int intcmp(const void *v1, const void *v2);

void main(void){
	//RNG(16, 98);
	Sort();
	
}

void RNG(int low, int high){
	int i;
	FILE *fp;
	
	srand( ( time(NULL) ) );
	
	fp = fopen("rand.txt", "w+");
	
	if(fp == NULL)
	{
		puts("file creation fail");
	}
	else
	{
		for( i = 1 ; i < EXCEED ; i++)
		{
			srand((time(NULL)));
			if ( i % 9 == 0)
			{
				fputs("\n", fp);
			}
			else
			{
				fprintf(fp, "%3d ", ( rand() & (high - low) ) + low);
			}
		}
	}
	puts("create rand.txt");
	fclose(fp);
}

void Sort( void )
{	
	FILE *fp;
	//int *arr = malloc(sizeof(int) * EXCEED);
	//memset(arr, 0, sizeof(int) * EXCEED);
	
	int arr[EXCEED] = {0, };
	int i = 0, j = 0;
	char buff[35];
	char tmp[4];
	
	fp = fopen("rand.txt", "r");
	
	if (fp == NULL)
	{
		puts("read fail");
	}
	
	else
	{
		while(fgets(buff, 35, fp) != 0)
		{	
			for(i=0;i<32;i++)
			{	
				memset(tmp, 0, len(tmp));
				if(i==0)
				{
					tmp[0] = buff[i+1];
					tmp[1] = buff[i+2];
					arr[j++] = atoi(tmp);
				}
				
				if( isspace(buff[i]) && isspace(buff[i-1]) )
				{
					tmp[0] = buff[i+1];
					tmp[1] = buff[i+2];
					arr[j++] = atoi(tmp);
				}
				
			}
			/*
				0 space 0+1 0+2
				1 char
				2 char
				3 space
				
				4 space 4+1 4+2
				5 char
				6 char
				7 space
				
				8 space 8+1 8+2
				9 char
			   10 char
			   11 space
			   
			   12 space 12+1 12+2
			   13 char
			   14 char
			   15 space
				...				   
			*/
		}

			for(i=0 ; i < EXCEED - 3 ; i++)
			{	
				if ( i == 0 ) 
				{
				
					printf("%d ", arr[i++]);
				}
				else if( i % 8 == 0 ) puts("");
					
				printf("%d ", arr[i]);
			}
		}
	}


int intcmp(const void *v1, const void *v2)
{
	int cmpv1, cmpv2;
	
	cmpv1 = *(int *)v1;
	cmpv2 = *(int *)v2;
	
	return cmpv1 - cmpv2;
}
