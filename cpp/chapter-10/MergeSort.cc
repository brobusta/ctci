#include <iostream>
#include <vector>

using namespace std;

void mergeSort(vector<int>&, vector<int>&, int, int);
void merge(vector<int>&, vector<int>&, int, int, int);

void Sort(vector<int>& arr) {
  vector<int> helper(arr.size());
  mergeSort(arr, helper, 0, arr.size() - 1);
}

void mergeSort(vector<int>& arr, vector<int>& helper, int low, int high) {
  if (low < high) {
    int middle = (low + high) / 2;
    mergeSort(arr, helper, low, middle);
    mergeSort(arr, helper, middle + 1, high);
    merge(arr, helper, low, middle, high);
  }
}

void merge(vector<int>& arr, vector<int>& helper, int low, int middle,
           int high) {
  helper = arr;

  int left = low;
  int right = middle + 1;
  int index = low;
  while (left <= middle && right <= high) {
    if (helper[left] <= helper[right]) {
      arr[index] = helper[left];
      left++;
    } else {
      arr[index] = helper[right];
      right++;
    }
    index++;
  }

  while (left <= middle) {
    arr[index] = helper[left];
    left++;
    index++;
  }
}

void print(vector<int>& v) {
  for (auto i = v.begin(); i != v.end(); i++) {
    cout << *i << " ";
  }
  cout << endl;
}

int main(void) {
  vector<int> in = {2, 4, 8, 15, 0, 37, 19, 21, 13, 33, 100, 97, 54, 1, 10};
  cout << "Before: " << endl;
  print(in);
  Sort(in);
  cout << "After: " << endl;
  print(in);
}
