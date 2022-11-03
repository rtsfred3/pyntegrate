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

uint wilson(uint n){
    return (floor(
        (factorial(n) % (n+1)) / n
    ) * (n - 1)) + 2;
}

long double willans_inner_funct(uint j) {
    return ((long double)(factorial(j - 1) + 1)/(long double)(j));
}

uint willans_inner_summation(uint i){
    uint j;
    uint val = 0;
    for(j = 1; j <= i; j++){
        val += (uint)floor(pow(cos(M_PI * (long double)willans_inner_funct(j)), 2));
    }
    return val;
}

uint willans(uint n){
    uint i;
    float val = 0;
    for(i = 1; i <= pow(2, n); i++){
        val += floor(pow((long double)n/(long double)willans_inner_summation(i), 1.0L/(long double)n));
    }
    // printf("%f\n", val/pow(2, n));
    return 1 + val;
}

#endif
