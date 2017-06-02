#include <iostream>
#include <vector>

#define RANGE 255

using namespace std;

void Sort(vector<int>& arr) {
  int count[RANGE + 1] = {};
  for (auto i = arr.begin(); i != arr.end(); i++) {
    count[*i]++;
  }

  for (int i = 1; i <= RANGE; i++) {
    count[i] = count[i] + count[i - 1];
  }

  vector<int> ret(arr.size());
  for (auto i = arr.begin(); i != arr.end(); i++) {
    ret[count[*i] - 1] = *i;
    count[*i]--;
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
  Sort(in);
  cout << "After: " << endl;
  print(in);
}
