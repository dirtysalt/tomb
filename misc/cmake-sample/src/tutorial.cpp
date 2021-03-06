/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <memory>
#include <vector>
#include <functional>
#include <thread>
#include <condition_variable>
#include <mutex>

#include "tutorial.h"
#include "config.h"

#ifdef USE_MATHLIB
#include "mathlib.h"
#else
int add(int x, int y) {
    printf("use native add\n");
    return x + y;
}
#endif

using namespace std;

int main(int argc, const char**argv) {
    auto tutorial = Tutorial();
    // report version
    std::cout << argv[0] << " Version " << Tutorial_VERSION_MAJOR << "."
              << Tutorial_VERSION_MINOR << std::endl;
    int z = add(10, 20);
    std::cout << "add(10, 20) = " << z <<std::endl;

#ifdef USE_MATHLIB
    std::cout << "exp(10.0) = " << myexp(10.0) << std::endl;
    std::cout << "log(10.0) = " << myexp(10.0) << std::endl;
    std:: cout << "isPrime(87793) = " << isPrime(87793) << std::endl;
#endif
    return 0;
}
