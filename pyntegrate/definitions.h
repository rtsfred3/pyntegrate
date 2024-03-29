#ifndef definitions_h
#define definitions_h

#define d_type long
#define uint unsigned long long

uint ackermannLookupTable[100][1000];

struct arg_struct {
    d_type *arr;
    int arg1;
    int arg2;
    int depth;
};

double e = 2.718281828459045235360;

double f(double x){ return 1.0/(1.0 + x*x); }
double f2(double t){ return pow(t, 0 - 1) * pow(e, -t); }
double f3(double x){ return 0.0; }

uint fact(uint n) { if(n <= 0){ return 1; }else{ return n * fact(n - 1); } }

#define n_pi 4.0*integrate2(f, 0, 1, 100000000)
#define o_pi 4.0*integrate(f, 0, 1)

#define arr_swap(arr, a, b) { d_type temp = arr[a]; arr[a] = arr[b]; arr[b] = temp; }

// #define arr_swap2(*a, *b) { *a = *a + *b; *b = *a - *b; *a = *a - *b; }

#define printArr(arr, n) { int ii; int ww = 10; printf("\n"); for(ii = 0; ii<n; ii++){ if((ii+1) % ww == 0 || ii == n-1){ printf("%7.2ld\n", arr[ii]); }else{ printf("%7.2ld ", arr[ii]); } } printf("\n"); }

#define chudnovsky_M(q) { fact(6*q) / (fact(6*q) * pow(fact(q), 3)) }

#define chudnovsky_L(q) { 545140134.0*q + 13591409.0 }

#define chudnovsky_X(q) { pow(-262537412640768000, q) }

#define willans_inner_funct(j) { ((long double)(fact(j - 1) + 1)/(long double)(j)) }

uint isPrimeWilson(uint n){
    // return fact(n - 1) % n != 0 && n != 4;
    
    return fact(n - 1) / (n * n);
}

uint wilson(uint n){
    return ((uint)((fact(n) % (n+1)) / n) * (n - 1)) + 2;
}

uint willans_inner_summation(uint i){
    uint j;
    uint val = 0;
    for(j = 1; j <= i; j++){
        val += (uint)floor(pow(cos(o_pi * (long double)willans_inner_funct(j)), 2));
    }
    return val;
}

uint willans(uint n){
    uint i;
    float val = 0;
    for(i = 1; i <= pow(2, n); i++){
        val += (uint)floor(pow((long double)n/(long double)willans_inner_summation(i), 1.0L/(long double)n));
    }
    return 1 + val;
}

#endif
