#include <iostream>
#include <vector>

using namespace std;

void countingSort(vector<int>& arr, int exp) {
  int count[10] = {};
  for (auto i = arr.begin(); i != arr.end(); i++) {
    count[(*i / exp) % 10]++;
  }

  for (int i = 1; i < 10; i++) {
    count[i] += count[i - 1];
  }

  vector<int> ret(arr.size());
  for (auto i = arr.begin(); i != arr.end(); i++) {
    ret[count[(*i / exp) % 10] - 1] = *i;
    count[(*i / exp) % 10]--;
  }
  arr = ret;
}

void print(vector<int>& v) {
  for (auto i = v.begin(); i != v.end(); i++) {
    cout << *i << " ";
  }
  cout << endl;
}

int main(void) {
  vector<int> in = {2,  4,   8,  15, 0, 37, 19, 8, 13,
                    33, 100, 97, 54, 1, 10, 8,  2};
  cout << "Before: " << endl;
  print(in);
  countingSort(in, 1);
  cout << "After: " << endl;
  print(in);
}
