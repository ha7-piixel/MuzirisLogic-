//This is a new C program for to understand the differences between the negative and the positive numbers 
#include <stdio.h>
void posneg(int a){
	if(a > 0)
		printf("The given number %d is a positive number", a);
	else if(a == 0)
		printf("The given number is a 0");
	else 
		printf("The given number %d is a negative number", a);
}
int main(){
	int n;
	printf("Enter the number you want to simulate: ");
	scanf("%d", &n);
	posneg(n);
	return 0;
}
