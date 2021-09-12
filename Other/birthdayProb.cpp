#include "math.h"
#include <iostream>

int find(double p) {
  return ceil(sqrt(2*365*log(1/(1-(atan(1)*4)))));
}

int main() {
  std::cout << find(0.91);
}
