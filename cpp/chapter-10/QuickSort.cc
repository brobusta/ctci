#include <iostream>
#include <vector>

using namespace std;

int partition(vector<int>&, int, int);
void quickSort(vector<int>&, int, int);

void Sort(vector<int>& arr) {
  quickSort(arr, 0, arr.size() - 1);
}

void quickSort(vector<int>& arr, int low, int high) {
  int index = partition(arr, low, high);
  if (low < index - 1)
    quickSort(arr, low, index - 1);
  if (index < high)
    quickSort(arr, index, high);
}

int partition(vector<int>& arr, int low, int high)
{
  int pivot = arr[(low + high) / 2];
  while(low <= high) {
    while(arr[low] < pivot) low++;

    while(arr[high] > pivot) high--;

    if (low < high) {
      swap(arr[low], arr[high]);
      low++;
      high--;
    }
  }
  return low;
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
