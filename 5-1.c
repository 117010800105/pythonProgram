#include"iostream.h"
void print_star( )                    	   	/* print_star���� */
{  
	cout<<"* * * * * * * * * *"<<endl;
}

void print_message( )                		/* print_message���� */ 
{	
	cout<<"Welcome you to use C language ! "<<endl;
	print_star( );							/* ����print_star���� */
}

void main( )	
{ 
	print_message( );            		  	/* ����print_message���� */
	print_star( );              	     	/* ����print_star���� */ 
}