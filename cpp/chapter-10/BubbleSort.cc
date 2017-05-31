#include <iostream>
#include <vector>

using namespace std;

void Sort(vector<int>& arr) {
  bool changed = true;
  int size = arr.size();

  if (size <= 1) return;

  while (changed) {
    changed = false;
    for (int i = 1; i < size; i++) {
      if (arr[i] < arr[i - 1]) {
        int temp = arr[i];
        arr[i] = arr[i - 1];
        arr[i - 1] = temp;
        changed = true;
      }
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
