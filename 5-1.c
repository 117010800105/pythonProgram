#include"iostream.h"
void print_star( )                    	   	/* print_star函数 */
{  
	cout<<"* * * * * * * * * *"<<endl;
}

void print_message( )                		/* print_message函数 */ 
{	
	cout<<"Welcome you to use C language ! "<<endl;
	print_star( );							/* 调用print_star函数 */
}

void main( )	
{ 
	print_message( );            		  	/* 调用print_message函数 */
	print_star( );              	     	/* 调用print_star函数 */ 
}