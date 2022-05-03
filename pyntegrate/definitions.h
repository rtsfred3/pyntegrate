#ifndef definitions_h
#define definitions_h

#define d_type long
#define uint unsigned long long

#define arr_swap(arr, a, b) { d_type temp = arr[a]; arr[a] = arr[b]; arr[b] = temp; }

#define printArr(arr, n) { int ii; int ww = 10; printf("\n"); for(ii = 0; ii<n; ii++){ if((ii+1) % ww == 0 || ii == n-1){ printf("%7.2ld\n", arr[ii]); }else{ printf("%7.2ld ", arr[ii]); } } printf("\n"); }

#endif
