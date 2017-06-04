#include <iostream>
#include <vector>

using namespace std;

void Sort(vector<int>& arr) {
  for (int i = 0; i < arr.size(); i++) {
    int min = i;
    for (int j = i + 1; j < arr.size(); j++) {
      if (arr[j] < arr[min])
        min = j;
    }
    swap(arr[i], arr[min]);
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
