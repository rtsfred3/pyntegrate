#ifndef definitions_h
#define definitions_h

#define d_type long
#define uint unsigned long long

uint factorial(uint n) { if(n <= 0){ return 1; }else{ return n*factorial(n - 1); } }

#define arr_swap(arr, a, b) { d_type temp = arr[a]; arr[a] = arr[b]; arr[b] = temp; }

#define printArr(arr, n) { int ii; int ww = 10; printf("\n"); for(ii = 0; ii<n; ii++){ if((ii+1) % ww == 0 || ii == n-1){ printf("%7.2ld\n", arr[ii]); }else{ printf("%7.2ld ", arr[ii]); } } printf("\n"); }

#define chudnovsky_M(q) { factorial(6*q) / (factorial(6*q) * pow(factorial(q), 3)) }

#define chudnovsky_L(q) { 545140134.0*q + 13591409.0 }

#define chudnovsky_X(q) { pow(-262537412640768000, q) }

#endif
