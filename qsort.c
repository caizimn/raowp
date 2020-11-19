#include <stdlib.h>

int compare(const void *value1, const void *value2) 
{
    return *(int*)value1 - *(int*)value2;/*升序*/
}

qsort(nums, numsSize, sizeof(int), compare);