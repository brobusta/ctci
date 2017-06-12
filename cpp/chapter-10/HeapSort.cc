#include <iostream>
#include <vector>

using namespace std;

void build_max_heap(vector<int>&);
void heapify(vector<int>&, int, int);

void Sort(vector<int>& arr) {
  build_max_heap(arr);
  int heap_size = arr.size();

  while (heap_size > 1) {
    swap(arr[0], arr[heap_size - 1]);
    heap_size--;
    heapify(arr, 0, heap_size);
  }
}

void build_max_heap(vector<int>& arr)
{
  int last_inner = (int) (arr.size() / 2) - 1;
  for (int i = last_inner; i >= 0; i--) {
    heapify(arr, i, arr.size());
  }
}

void heapify(vector<int>& arr, int pos, int heap_size) {
  int max_size = heap_size;
  
  int left = 2 * pos + 1;
  int right = 2 * pos + 2;

  if (pos < max_size) {
    int largest = pos;
    
    if (left < max_size && arr[left] > arr[largest]) {
      largest = left;
    }
    if (right < max_size && arr[right] > arr[largest]) {
      largest = right;
    }

    if (largest != pos) {
      swap(arr[pos], arr[largest]);
      heapify(arr, largest, heap_size);
    }
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
