#include <iostream>

using namespace std;

int bin_search_left(int *arr, int target, int n) {
    int left = -1;
    int right = n-1;
    int med = (left+right)/2;
    while(left < right-1) {
        if(arr[med] >= target) {
            right = med;
        } else {
            left = med;
        }
        med = (left + right)/2;
    }

    if(arr[right] == target) {
        return right;
    } else {
        return -1;
    }
}

int bin_search_right(int *arr, int target, int n) {
    int left = 0;
    int right = n;
    int med = (left+right)/2;
    while(left < right-1) {
        if(arr[med] <= target) {
            left = med;
        } else {
            right = med;
        }
        med = (left + right)/2;
    }

    if(arr[left] == target) {
        return left;
    } else {
        return -1;
    }
}

void check_ans(int *mas) {
    if(mas[0] == -1) {
        cout << -1;
    } else {
        cout << mas[0] << " " << mas[1] << endl;
    }
}

void Solution(int *arr, int target, int n) {
    int left = bin_search_left(arr, target, n);
    int right = bin_search_right(arr, target, n);
    int mas[2] = {left, right};
    check_ans(mas);
} 

int* init_arr(int n) {
    int *arr;
    arr = new int[n];
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    } 
    return arr;
}

void clear(int *arr) {
    delete[] arr;
}

int main() {
    int n, target;
    cin >> n >> target;
    int *arr = init_arr(n);
    Solution(arr, target, n);
    clear(arr);
    return 0;
}