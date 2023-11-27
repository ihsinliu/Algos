#include <stdio.h>

int binarySearch(int* array, int length, int target) {
    if (array == NULL) {
        return -1;
    }

    int l = 0, r = length - 1;
    int mid;
    int val;
    while (l+1 <= r) {
        mid = (l + r) / 2;
        val = array[mid];
        if (val == target) {
            r=mid;
        } else if (val < target) {
            l = mid;
        } else {
            r = mid;
        }
    }

    if (array[l] == target) {
        return l;
    }
    if (array[r] == target) {
        return r;
    }

    return -1;
}