#include<stdio.h>

void  main()

{

	int a,b,temp;

	print(“Enter any two numbers:”);

	scanf(“%d%d”,&a,&b);

	temp=a;

	a=b;

	b=temp;

	printf(“After swapping “);

	printf(“a=%d”,a);

	printf(“b=%d”,b);

	return 0;

}
