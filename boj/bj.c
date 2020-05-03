#include <stdio.h>

int main(void){
	int n = 0;
	int i = 0, j = 0, k = 0;
	
	scanf("%d", &n);
	
	int pivot = (int)( (n+(n-1)) / 2 );
	
	for(i = 0 ; i < n ; i++){
		for(j = 0 ; j < n+(n-1) ; j++){
			if(j >= pivot - k && j <= pivot + k)
				printf("*");
			
			else
			{
				printf(" ");
			}
			
			if(j==pivot+k) break;
		}
		if(i==n-1)
			break;
		
		else
		{
			puts("");
			k++;
		}
	}
	
	return 0;
}
