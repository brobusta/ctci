#include <iostream>
#include <vector>

using namespace std;

void insertionSort(vector<float>&);

void bucketSort(vector<float>& arr) {
  int n = arr.size();
  vector<float> bucket[n];

  for (int i = 0; i < n; i++) {
    int bi = n * arr[i];
    bucket[bi].push_back(arr[i]);
  }

  for (int i = 0; i < n; i++) {
    insertionSort(bucket[i]);
  }

  int index = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < bucket[i].size(); j++) {
      arr[index++] = bucket[i][j];
    }
  }
}

void insertionSort(vector<float>& arr) {
  int i, j;
  float k;
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

void print(vector<float>& v) {
  for (auto i = v.begin(); i != v.end(); i++) {
    cout << *i << " ";
  }
  cout << endl;
}

int main(void) {
  vector<float> in = {0.2, 0.4, 0.8, 0.15, 0.0, 0.37, 0.19, 0.21, 0.13, 0.33, 0.100, 0.97, 0.54, 0.1, 0.10};
  cout << "Before: " << endl;
  print(in);
  bucketSort(in);
  cout << "After: " << endl;
  print(in);
}
