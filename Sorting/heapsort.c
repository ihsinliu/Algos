#include<stdio.h>
#include<stdlib.h>

void swap(int *arr, int i, int j)
{
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
}

void heapify(int *f, int n)
{
	int node, parent, left_child, right_child, max;

	/* We begin with the parent node with the highest index */
	node = ((n+1)/2) - 1;

	while(node >= 0)
	{
		parent = node;
		left_child = parent * 2 + 1;
		while(left_child < n)
		{
			right_child = left_child + 1;

			/* First, we want to find which is actually max: parent, left child, or right child */
			max = parent;

			/* Test left child */
			if(f[max] < f[left_child])
				max = left_child;

			/* Test if right child is less than max index found so far */
			/* (only test if that node is within array boundaries) */
			if(right_child < n)
				if(f[max] < f[right_child])
					max = right_child;

			/* If the parent is already the maximum, we can move down to the next lower node */
			if( max == parent )
				break;

			/* If the parent is not the maximum, we swap with the correct max index. */
			/* Then, we will have to fix any down line issues caused by swaping the
			 * parent and child nodes, so we continue the while loop */
			if(max != parent)
			{
				swap(f, parent, max);
				parent = max;
				left_child = parent*2+1;
			}
		}
		node--;
	}
}

int * allocate_array(int len, char * values[])
{
	int *arr, i;
	arr = (int *)malloc(len*sizeof(int));

	for(i=1; i<len; i++){
		arr[i-1] = atoi(values[i]);
	}
	return arr;
}

int test_heap( int * f, int n)
{
	int i;
	int child_A, child_B;

	for( i = 0; i < n; i++ )
	{
		child_A = ( 2 * i ) + 1;
		child_B = ( 2 * i ) + 2;

		if( child_A < n )
			if( f[i] < f[child_A] )
				return -1;
		
		if( child_B < n )
			if( f[i] < f[child_B] )
				return -1;
	}

	return 1;
}

int main()
{
	int result;
	int i;
    int len = 20;
    char * values[] = {"111", "21", "32", "1", "5", "61", "71", "8", "9", "10",
                       "121", "112", "143", "143", "125", "16", "17", "181", "19", "220"};
	int n = len - 1;
	int * arr = allocate_array( len, values );

	heapify( arr, n );
	result = test_heap( arr, n );

	for( i = 0; i < n; i++ )
		printf("%d ", arr[i]);
	printf("\n");

	if( result == 1 )
		printf("Heap test success!\n");
	else
		printf("Heap test failed.\n");

	free(arr);

	return 0;
}