#include <iostream>
#include <vector>

using namespace std;

void Sort(vector<int>& arr) {
  int i, j, k;
  for (i = 1; i < arr.size(); i++) {
    k = arr[i];
    j = i - 1;

    while (j >= 0 && arr[j] > k) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = k;
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
