#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#ifdef _POSIX_VERSION
    #include <pthread.h>
    #include <unistd.h>
#endif

#include <Python.h>

double integrate(double (*f)(double), double a, double b);
double integrate2(double (*f)(double), double a, double b, int n);

// double f(double x){ return 1.0/(1.0 + x*x); }
// double f2(double t){ return pow(t, 0 - 1) * pow(e, -t); }
// double f3(double x){ return 0.0; }

#include "definitions.h"

double f22(){ return integrate(f2, 0.0, 1000.0); }

d_type getD_Type(d_type n){ return rand() % (n*n); }

void makeArray(d_type * dbar, d_type n, d_type seed){
    int i;
    // srand(2);
    srand(seed);
    for(i = 0; i < n; i++) { dbar[i] = getD_Type(n); }
}

int isSorted(d_type *arr, int n){
    int i;
    for(i = 1; i < n; i++){ if(arr[i-1] > arr[i]){ return 0; } }
    return 1;
}

double integrate(double (*f)(double), double a, double b){
    int n = 5000000;

    double h = (b-a)/(double)n;
    double s = (*f)(a) + (*f)(b);

    int i;
    for(i = 1; i < n; i+=2){ s = s + 4 * (*f)(a + i * h); }
    for(i = 2; i < n-1; i+=2){ s = s + 2 * (*f)(a + i*h); }

    return (s*h)/3.0;
}

double integrate2(double (*f)(double), double a, double b, int n){
    double h = (b-a)/(double)n;
    double s = (*f)(a) + (*f)(b);

    int i;
    for(i = 1; i < n; i+=2){ s = s + 4 * (*f)(a + i * h); }
    for(i = 2; i < n-1; i+=2){ s = s + 2 * (*f)(a + i*h); }

    return (s*h)/3.0;
}

uint Ackermann(uint m, uint n){
    if(m == 0ll){ return n + 1; }
    if(n == 0ll){ return Ackermann(m - 1ll, 1ll); }
    return Ackermann(m - 1ll, Ackermann(m, n - 1ll));
}

uint AckermannLookup(uint m, uint n){
    if(ackermannLookupTable[m][n]){
        return ackermannLookupTable[m][n];
    }
    
    if(ackermannLookupTable[m][n] == 0){
        if(m == 0ll){
            ackermannLookupTable[m][n] = n + 1ll;
        }else if(n == 0ll){
            ackermannLookupTable[m][n] = AckermannLookup(m - 1ll, 1ll);
        }else{
            ackermannLookupTable[m][n] =  AckermannLookup(m - 1ll, Ackermann(m, n - 1ll));
        }
    }
    return ackermannLookupTable[m][n];
}

int isPrime(d_type n){
    if((n <= 1) || (n % 2 == 0 && n != 2) || (n % 3 == 0 && n != 3) || (n % 5 == 0 && n != 5) || (n % 7 == 0 && n != 7)){ return 0; }

    d_type j;
    for(j = 11; j < (d_type)sqrt(n)+2; j+=2){ if(n % j == 0){ return 0; } }

    return 1;
}

void merge(d_type *a, int n, int m) {
    int i, j, k;
    d_type *x = malloc(n * sizeof(d_type));
    for (i = 0, j = m, k = 0; k < n; k++) {
        x[k] = j == n      ? a[i++]
             : i == m      ? a[j++]
             : a[j] < a[i] ? a[j++]
             :               a[i++];
    }
    for (i = 0; i < n; i++) {
        a[i] = x[i];
    }
    free(x);
}

void merge_sortC(d_type *arr, int n){
    if (n < 2)
        return;
    int m = (int)(n / 2);
    merge_sortC(arr, m);
    merge_sortC(arr + m, n - m);
    merge(arr, n, m);
}

void bubble_sort(d_type *arr, int n){
    int i, j;
    for(i = 0; i < n; i++){
        for(j = 1; j < n; j++){
            if(arr[j-1] > arr[j]){
                arr_swap(arr, j-1, j);
            }
        }
    }
}

void bubble_sort2(d_type *arr, int n){
    int i;
    int itemCount = n;
    int hasChanged = 1;
    while(hasChanged != 0){
        hasChanged = 0;
        for(i = 1; i<itemCount; i++){
            if(arr[i] < arr[i-1]){
                arr_swap(arr, i-1, i);
                hasChanged = 1;
            }
        }
        itemCount--;
    }
}

void insertion_sort(d_type *arr, int n){
    int i, j;
    // d_type key;
    for(j = 1; j < n; j++){
        // d_type key = arr[j];
        i = j;
        while(i > 0 && arr[i-1] > arr[i]){
            arr_swap(arr, i-1, i);
            i = i - 1;
        }
    }
}

int partition(d_type *arr, int low, int high){
    d_type pivot = arr[low];
    int lastSmall = low;
    int i;
    for(i = low+1; i<high; i++){
        if(arr[i] < pivot){
            lastSmall++;
            arr_swap(arr, lastSmall, i);
        }
    }
    arr_swap(arr, low, lastSmall);
    return lastSmall;
}

void quicksort(d_type *arr, int low, int high){
    if(low < high){
        int part = partition(arr, low, high);
        quicksort(arr, low, part);
        quicksort(arr, part+1, high);
    }
}

void bucketsort(d_type *arr, int n){
    clock_t start;
    int i, j, w;
    int bins = 10.0;
    int n2 = (int)((1.0/(double)bins)*n);
    d_type **B = (d_type **)malloc(n2*sizeof(d_type *));

    int v[4] = {0, 0, 0, 0};

    if(v[0]){ start = clock(); }

    for(i = 0; i<n2; i++){
        B[i] = (d_type *)malloc((n+1)*sizeof(d_type));
        B[i][n] = 0.0;
    }

    if(v[0]){ printf("Marker 1 (Allocating Arrays):\t%f seconds\n", (double)(clock() - start) / CLOCKS_PER_SEC); }

    for(i = 0; i<n; i++){
        if(v[2]){ printf("arr[%d] = %0.2ld \tn = %d\t", i, arr[i], n); }

        w = (int)((double)(arr[i])/((double)(bins*n)));

        if(v[2]){ printf("w=%d\n", w); }
        B[w][(int)(B[w][n])] = arr[i];
        B[w][n]++;
    }

    if(v[0]){ printf("Marker 2 (Placing Elements):\t%f seconds\n", (double)(clock() - start) / CLOCKS_PER_SEC); }

    for(i = 0; i<n2; i++){
        if(B[i][n] > 1){
            quicksort(B[i], 0, B[i][n]);
        }
        if(v[3]){ if(B[i][n] > 0){ printArr(B[i], (int)B[i][n]); } }
        if(v[1]){ if(B[i][n] > 0){ printf("Size of bin[%d]\t = %d\n", i, (int)B[i][n]); } }
    }

    if(v[0]){ printf("Marker 3 (Sorting Bins):\t%f seconds\n", (double)(clock() - start) / CLOCKS_PER_SEC); }

    i = 0;
    for(j = 0; j<n2; j++){
        if(i >= n){ break; }
        if(B[j][n] > 0){
            for(w = 0; w<B[j][n]; w++){
                if(i >= n){ break; }
                arr[i++] = B[j][w];
            }
        }
    }

    if(v[0]){ printf("Marker 4 (Extracting Elements):\t%f seconds\n", (double)(clock() - start) / CLOCKS_PER_SEC); }

    free(B);

    if(v[0]){ printf("Marker 5 (Freeing Bins):\t%f seconds\n", (double)(clock() - start) / CLOCKS_PER_SEC); }

    // if(v[0] && 0 == 1){ printf("Total Memory Footprint: %lu\n", ((n+1)*n2*sizeof(d_type))); }
}

float chudnovsky(uint n){
    float q;
    float summation = 0.0;
    
    for(q = 0.0; q < n; q++){
        float a = chudnovsky_M(q);
        float b = chudnovsky_L(q);
        float c = chudnovsky_X(q);
        summation += (double)(a * b)/(c);
    }
    
    // printf("%f\n", (double)(426880.0*sqrt(10005)));
    // printf("%f\n", summation);
    
    return (426880.0*sqrt(10005))/summation;
}

#ifdef _POSIX_VERSION

void* checkPrimes(void *vals){
    uint *arr = (uint *)((uint *)vals);

    uint i;
    for(i = arr[0]; i < arr[1]; i++){ if(isPrime(i)){ arr[3]++; } }

    if(arr[2] != 0){ pthread_exit(NULL); }
    return NULL;
}

int compute_primes(uint n, uint NUM_THREADS){
    pthread_t threads[NUM_THREADS];

    uint arr[NUM_THREADS][4];

    uint i;
    for(i = 0; i<NUM_THREADS; i++){
        arr[i][0] = (uint)((i)*(n/NUM_THREADS));
        arr[i][1] = (uint)((i+1)*(n/NUM_THREADS));
        arr[i][2] = NUM_THREADS-i-1;
        arr[i][3] = 0;
    }

    if(arr[NUM_THREADS-1][1] != n){ arr[NUM_THREADS-1][1] = n; }

    for(i = 0; i<NUM_THREADS-1; i++){
        pthread_create(&threads[i], NULL, checkPrimes, (void *)&arr[i]);
    }

    checkPrimes((void *)&arr[NUM_THREADS-1]);

    for(i = 0; i<NUM_THREADS-1; i++){
        pthread_join(threads[i], NULL);
    }

    int total = 0;
    for(i = 0; i<NUM_THREADS; i++){
        total += arr[i][3];
    }
    return total;
}

void* parallel_merge_sortC(void *args){
    pthread_t thread_id, thread_id2;
    d_type *arr = ((struct arg_struct *)args)->arr;
    int n = ((struct arg_struct *)args)->arg1;
    int depth = ((struct arg_struct *)args)->depth;

    if (n < 2){ return NULL; }

    int m = (int)(n / 2);

    struct arg_struct args_t;
    args_t.arr = arr;
    args_t.arg1 = m;
    args_t.depth = depth+1;

    struct arg_struct args_m;
    args_m.arr = arr + m;
    args_m.arg1 = n - m;
    args_m.depth = depth+1;

    if(depth > 2){
        parallel_merge_sortC((void *)&args_t);
        parallel_merge_sortC((void *)&args_m);
    }else{
        pthread_create(&thread_id, NULL, parallel_merge_sortC, (void *)&args_t);
        pthread_create(&thread_id2, NULL, parallel_merge_sortC, (void *)&args_m);
        pthread_join(thread_id2, NULL);
        pthread_join(thread_id, NULL);
    }

    merge(arr, n, m);

    return NULL;
}

void* p_quicksort(void *args){
    pthread_t thread_id, thread_id2;
    d_type *arr = ((struct arg_struct *)args)->arr;
    int low = ((struct arg_struct *)args)->arg1;
    int high = ((struct arg_struct *)args)->arg2;
    int depth = ((struct arg_struct *)args)->depth;
    if(low >= high){ return NULL; }

    if(low < high){
        int part = partition(arr, low, high);

        struct arg_struct argv_t;
        argv_t.arr = arr;
        argv_t.arg1 = low;
        argv_t.arg2 = part;
        argv_t.depth = depth+1;

        struct arg_struct argv_m;
        argv_m.arr = arr;
        argv_m.arg1 = part+1;
        argv_m.arg2 = high;
        argv_m.depth = depth+1;

        if(depth > 2){
            p_quicksort((void *)&argv_t);
            p_quicksort((void *)&argv_m);
        }else{
            pthread_create(&thread_id, NULL, p_quicksort, (void *)&argv_t);
            pthread_create(&thread_id2, NULL, p_quicksort, (void *)&argv_m);

            pthread_join(thread_id2, NULL);
            pthread_join(thread_id, NULL);
        }
    }

    return NULL;
}

static PyObject* p_primes(PyObject *self, PyObject *args){
    d_type x;
    int total = 0;

    if(!PyArg_ParseTuple(args, "l", &x)){
        return NULL;
    }

    long number_of_processors = sysconf(_SC_NPROCESSORS_ONLN);

    total = compute_primes((uint)x, (uint)number_of_processors);

    return Py_BuildValue("i", total);
}

static PyObject* parallel_merge_sort(PyObject *self, PyObject *args){
    PyObject* seq;
    int i, seqlen;
    d_type * dbar;

    if(!PyArg_ParseTuple(args, "O", &seq)){
        return NULL;
    }

    seq = PySequence_Fast(seq, "argument must be iterable");
    if(!seq){ return NULL; }

    seqlen = PySequence_Fast_GET_SIZE(seq);
    dbar = malloc(seqlen*sizeof(d_type));
    if(!dbar) {
        Py_DECREF(seq);
        return PyErr_NoMemory(  );
    }

    for(i = 0; i < seqlen; i++) {
        PyObject *fitem;
        PyObject *item = PySequence_Fast_GET_ITEM(seq, i);
        if(!item) {
            Py_DECREF(seq);
            free(dbar);
            return 0;
        }
        fitem = PyNumber_Long(item);
        if(!fitem) {
            Py_DECREF(seq);
            free(dbar);
            PyErr_SetString(PyExc_TypeError, "all items must be numbers");
            return 0;
        }
        dbar[i] = PyLong_AsLong(fitem);
        Py_DECREF(fitem);
    }

    struct arg_struct argv;
    argv.arr = dbar;
    argv.arg1 = seqlen;
    argv.depth = 0;

    // parallel_merge_sortC(dbar, seqlen);
    parallel_merge_sortC((void *)&argv);

    for(i = 0; i < seqlen; i++){
        PySequence_SetItem(seq, i, PyLong_FromLong(dbar[i]));
    }

    free(dbar);

    return Py_BuildValue("O", seq);
}

static PyObject* p_quick_sort(PyObject *self, PyObject *args){
    PyObject* seq;
    int i, seqlen;
    d_type * dbar;

    if(!PyArg_ParseTuple(args, "O", &seq)){
        return NULL;
    }

    seq = PySequence_Fast(seq, "argument must be iterable");
    if(!seq){ return NULL; }

    seqlen = PySequence_Fast_GET_SIZE(seq);
    dbar = malloc(seqlen*sizeof(d_type));
    if(!dbar) {
        Py_DECREF(seq);
        return PyErr_NoMemory(  );
    }

    for(i = 0; i < seqlen; i++) {
        PyObject *fitem;
        PyObject *item = PySequence_Fast_GET_ITEM(seq, i);
        if(!item) {
            Py_DECREF(seq);
            free(dbar);
            return 0;
        }
        fitem = PyNumber_Long(item);
        if(!fitem) {
            Py_DECREF(seq);
            free(dbar);
            PyErr_SetString(PyExc_TypeError, "all items must be numbers");
            return 0;
        }
        dbar[i] = PyLong_AsLong(fitem);
        Py_DECREF(fitem);
    }

    struct arg_struct argv;
    argv.arr = dbar;
    argv.arg1 = 0;
    argv.arg2 = seqlen;
    argv.depth = 0;

    // parallel_merge_sortC(dbar, seqlen);
    p_quicksort((void *)&argv);

    for(i = 0; i < seqlen; i++){
        PySequence_SetItem(seq, i, PyLong_FromLong(dbar[i]));
    }

    free(dbar);

    return Py_BuildValue("O", seq);
}

#endif

static PyObject* arctan(PyObject *self, PyObject *args){
    double x;

    if(!PyArg_ParseTuple(args, "d", &x)){
        return NULL;
    }

    return Py_BuildValue("f", integrate(f, 0, x));
}

static PyObject* arctan2(PyObject *self, PyObject *args){
    double x;
    int n;

    if(!PyArg_ParseTuple(args, "di", &x, &n)){
        return NULL;
    }

    return Py_BuildValue("f", integrate2(f, 0, x, n));
}

static PyObject* gamma_fun(PyObject *self, PyObject *args){
    int a;
    if(!PyArg_ParseTuple(args, "d", &a)){ return NULL; }

    return Py_BuildValue("f", f22());
}

static PyObject* is_prime(PyObject *self, PyObject *args){
    PyObject* seq;
    d_type x;

    if(!PyArg_ParseTuple(args, "l", &x)){
        return NULL;
    }

    if(isPrime(x)){
        seq = Py_True;
    }else{
        seq = Py_False;
    }

    return Py_BuildValue("O", seq);
}

static PyObject* primes(PyObject *self, PyObject *args){
    d_type x;
    int total = 0;

    if(!PyArg_ParseTuple(args, "l", &x)){
        return NULL;
    }

    d_type i;
    for(i = 0; i<x; i++){
        if(isPrime(i)){ total++; }
    }

    return Py_BuildValue("i", total);
}

static PyObject* pi(PyObject *self, PyObject *args){
    return Py_BuildValue("f", 4*integrate2(f, 0, 1, 100000000));
}

static PyObject* bubblesort(PyObject *self, PyObject *args){
    PyObject* seq;
    uint i, seqlen;
    d_type * dbar;

    if(!PyArg_ParseTuple(args, "O", &seq)){
        return NULL;
    }

    seq = PySequence_Fast(seq, "argument must be iterable");
    if(!seq){ return NULL; }

    seqlen = PySequence_Fast_GET_SIZE(seq);
    dbar = malloc(seqlen*sizeof(d_type));
    if(!dbar) {
        Py_DECREF(seq);
        return PyErr_NoMemory(  );
    }

    for(i = 0; i < seqlen; i++) {
        PyObject *fitem;
        PyObject *item = PySequence_Fast_GET_ITEM(seq, i);
        if(!item) {
            Py_DECREF(seq);
            free(dbar);
            return 0;
        }
        fitem = PyNumber_Long(item);
        if(!fitem) {
            Py_DECREF(seq);
            free(dbar);
            PyErr_SetString(PyExc_TypeError, "all items must be numbers");
            return 0;
        }
        dbar[i] = PyLong_AsLong(fitem);
        Py_DECREF(fitem);
    }

    bubble_sort(dbar, seqlen);

    for(i = 0; i < seqlen; i++){
        PySequence_SetItem(seq, i, PyLong_FromLong(dbar[i]));
    }

    free(dbar);

    return Py_BuildValue("O", seq);
}

static PyObject* bubblesort2(PyObject *self, PyObject *args){
    PyObject* seq;
    int i, seqlen;
    d_type * dbar;

    if(!PyArg_ParseTuple(args, "O", &seq)){
        return NULL;
    }

    seq = PySequence_Fast(seq, "argument must be iterable");
    if(!seq){ return NULL; }

    seqlen = PySequence_Fast_GET_SIZE(seq);
    dbar = malloc(seqlen*sizeof(d_type));
    if(!dbar) {
        Py_DECREF(seq);
        return PyErr_NoMemory(  );
    }

    for(i = 0; i < seqlen; i++) {
        PyObject *fitem;
        PyObject *item = PySequence_Fast_GET_ITEM(seq, i);
        if(!item) {
            Py_DECREF(seq);
            free(dbar);
            return 0;
        }
        fitem = PyNumber_Long(item);
        if(!fitem) {
            Py_DECREF(seq);
            free(dbar);
            PyErr_SetString(PyExc_TypeError, "all items must be numbers");
            return 0;
        }
        dbar[i] = PyLong_AsLong(fitem);
        Py_DECREF(fitem);
    }

    bubble_sort2(dbar, seqlen);

    for(i = 0; i < seqlen; i++){
        PySequence_SetItem(seq, i, PyLong_FromLong(dbar[i]));
    }

    free(dbar);

    return Py_BuildValue("O", seq);
}

static PyObject* bucket_sort(PyObject *self, PyObject *args){
    PyObject* seq;
    int i, seqlen;
    d_type * dbar;

    if(!PyArg_ParseTuple(args, "O", &seq)){
        return NULL;
    }

    seq = PySequence_Fast(seq, "argument must be iterable");
    if(!seq){ return NULL; }

    seqlen = PySequence_Fast_GET_SIZE(seq);
    dbar = malloc(seqlen*sizeof(d_type));
    if(!dbar) {
        Py_DECREF(seq);
        return PyErr_NoMemory(  );
    }

    for(i = 0; i < seqlen; i++) {
        PyObject *fitem;
        PyObject *item = PySequence_Fast_GET_ITEM(seq, i);
        if(!item) {
            Py_DECREF(seq);
            free(dbar);
            return 0;
        }
        fitem = PyNumber_Long(item);
        if(!fitem) {
            Py_DECREF(seq);
            free(dbar);
            PyErr_SetString(PyExc_TypeError, "all items must be numbers");
            return 0;
        }
        dbar[i] = PyLong_AsLong(fitem);
        Py_DECREF(fitem);
    }

    bucketsort(dbar, seqlen);

    for(i = 0; i < seqlen; i++){
        PySequence_SetItem(seq, i, PyLong_FromLong(dbar[i]));
    }

    free(dbar);

    return Py_BuildValue("O", seq);
}

static PyObject* merge_sort(PyObject *self, PyObject *args){
    PyObject* seq;
    int i, seqlen;
    d_type * dbar;

    if(!PyArg_ParseTuple(args, "O", &seq)){
        return NULL;
    }

    seq = PySequence_Fast(seq, "argument must be iterable");
    if(!seq){ return NULL; }

    seqlen = PySequence_Fast_GET_SIZE(seq);
    dbar = malloc(seqlen*sizeof(d_type));
    if(!dbar) {
        Py_DECREF(seq);
        return PyErr_NoMemory(  );
    }

    for(i = 0; i < seqlen; i++) {
        PyObject *fitem;
        PyObject *item = PySequence_Fast_GET_ITEM(seq, i);
        if(!item) {
            Py_DECREF(seq);
            free(dbar);
            return 0;
        }
        fitem = PyNumber_Long(item);
        if(!fitem) {
            Py_DECREF(seq);
            free(dbar);
            PyErr_SetString(PyExc_TypeError, "all items must be numbers");
            return 0;
        }
        dbar[i] = PyLong_AsLong(fitem);
        Py_DECREF(fitem);
    }

    merge_sortC(dbar, seqlen);

    for(i = 0; i < seqlen; i++){
        PySequence_SetItem(seq, i, PyLong_FromLong(dbar[i]));
    }

    free(dbar);

    return Py_BuildValue("O", seq);
}

static PyObject* quick_sort(PyObject *self, PyObject *args){
    PyObject* seq;
    int i, seqlen;
    d_type * dbar;

    if(!PyArg_ParseTuple(args, "O", &seq)){
        return NULL;
    }

    seq = PySequence_Fast(seq, "argument must be iterable");
    if(!seq){ return NULL; }

    seqlen = PySequence_Fast_GET_SIZE(seq);
    dbar = malloc(seqlen*sizeof(d_type));
    if(!dbar) {
        Py_DECREF(seq);
        return PyErr_NoMemory(  );
    }

    for(i = 0; i < seqlen; i++) {
        PyObject *fitem;
        PyObject *item = PySequence_Fast_GET_ITEM(seq, i);
        if(!item) {
            Py_DECREF(seq);
            free(dbar);
            return 0;
        }
        fitem = PyNumber_Long(item);
        if(!fitem) {
            Py_DECREF(seq);
            free(dbar);
            PyErr_SetString(PyExc_TypeError, "all items must be numbers");
            return 0;
        }
        dbar[i] = PyLong_AsLong(fitem);
        Py_DECREF(fitem);
    }

    quicksort(dbar, 0, seqlen);

    for(i = 0; i < seqlen; i++){
        PySequence_SetItem(seq, i, PyLong_FromLong(dbar[i]));
    }

    free(dbar);

    return Py_BuildValue("O", seq);
}

static PyObject* insert_sort(PyObject *self, PyObject *args){
    PyObject* seq;
    int i, seqlen;
    d_type * dbar;

    if(!PyArg_ParseTuple(args, "O", &seq)){
        return NULL;
    }

    seq = PySequence_Fast(seq, "argument must be iterable");
    if(!seq){ return NULL; }

    seqlen = PySequence_Fast_GET_SIZE(seq);
    dbar = malloc(seqlen*sizeof(d_type));
    if(!dbar) {
        Py_DECREF(seq);
        return PyErr_NoMemory(  );
    }

    for(i = 0; i < seqlen; i++) {
        PyObject *fitem;
        PyObject *item = PySequence_Fast_GET_ITEM(seq, i);
        if(!item) {
            Py_DECREF(seq);
            free(dbar);
            return 0;
        }
        fitem = PyNumber_Long(item);
        if(!fitem) {
            Py_DECREF(seq);
            free(dbar);
            PyErr_SetString(PyExc_TypeError, "all items must be numbers");
            return 0;
        }
        dbar[i] = PyLong_AsLong(fitem);
        Py_DECREF(fitem);
    }

    insertion_sort(dbar, seqlen);

    for(i = 0; i < seqlen; i++){
        PySequence_SetItem(seq, i, PyLong_FromLong(dbar[i]));
    }

    free(dbar);

    return Py_BuildValue("O", seq);
}

static PyObject* pass_arr(PyObject *self, PyObject *args){
    PyObject* seq;
    d_type i, seqlen;
    d_type * dbar;

    if(!PyArg_ParseTuple(args, "O", &seq)){ return NULL; }

    seq = PySequence_Fast(seq, "argument must be iterable");
    if(!seq){ return NULL; }

    seqlen = PySequence_Fast_GET_SIZE(seq);
    dbar = malloc(seqlen*sizeof(d_type));
    if(!dbar) {
        Py_DECREF(seq);
        return PyErr_NoMemory(  );
    }

    for(i = 0; i < seqlen; i++) {
        PyObject *fitem;
        PyObject *item = PySequence_Fast_GET_ITEM(seq, i);
        if(!item) {
            Py_DECREF(seq);
            free(dbar);
            return 0;
        }
        fitem = PyNumber_Long(item);
        if(!fitem) {
            Py_DECREF(seq);
            free(dbar);
            PyErr_SetString(PyExc_TypeError, "all items must be numbers");
            return 0;
        }
        dbar[i] = PyLong_AsLong(fitem);
        Py_DECREF(fitem);
    }

    for(i = 0; i < seqlen; i++){
        PySequence_SetItem(seq, i, PyLong_FromLong(dbar[i]));
    }

    free(dbar);

    return Py_BuildValue("O", seq);
}

static PyObject* makeArr(PyObject *self, PyObject *args){
    d_type i, seqlen;
    d_type seed = 2;
    
    if(!PyArg_ParseTuple(args, "l|l", &seqlen, &seed)){ return NULL; }
    
    // if(!PyArg_ParseTuple(args, "ll", &seqlen, &seed)){ return NULL; }
    // if(!PyArg_ParseTuple(args, "l", &seqlen)){ return NULL; }
    
    if(seqlen < 0){ return Py_BuildValue("O", PyList_New(0)); }

    PyObject * seq = PyList_New(seqlen);

    d_type * dbar = malloc(seqlen*sizeof(d_type));
    makeArray(dbar, seqlen, 2);

    for(i = 0; i < seqlen; i++){ PyList_SetItem(seq, i, PyLong_FromLong(dbar[i])); }

    free(dbar);

    return Py_BuildValue("O", seq);
}

static PyObject* makeArrSequential(PyObject *self, PyObject *args){
    d_type i, seqlen;

    if(!PyArg_ParseTuple(args, "l", &seqlen)){ return NULL; }
    if(seqlen < 0){ return Py_BuildValue("O", PyList_New(0)); }

    PyObject * seq = PyList_New(seqlen);

    for(i = 0; i < seqlen; i++){ PyList_SetItem(seq, i, PyLong_FromLong(i)); }
    
    return Py_BuildValue("O", seq);
}

static PyObject* makeArrZeros(PyObject *self, PyObject *args){
    d_type i, seqlen;

    if(!PyArg_ParseTuple(args, "l", &seqlen)){ return NULL; }
    if(seqlen <= 0){ return Py_BuildValue("O", PyList_New(0)); }

    PyObject * seq = PyList_New(seqlen);
    
    // for(i = 0; i < seqlen; i++){
    //     PyList_SetItem(seq, i, PyLong_FromLong(0));
    // }
    
    for(i = 0; i < (int)(seqlen/2.0) + 1; i++){
        PyList_SetItem(seq, i, PyLong_FromLong(0));
        PyList_SetItem(seq, (seqlen - 1) - i, PyLong_FromLong(0));
    }
    
    return Py_BuildValue("O", seq);
}

static PyObject* runChudnovsky(PyObject *self, PyObject *args){
    double n;

    if(!PyArg_ParseTuple(args, "d", &n)){ return NULL; }
    
    return Py_BuildValue("d", chudnovsky(n));
}

static PyObject* runWilson(PyObject *self, PyObject *args){
    uint n;
    
    if(!PyArg_ParseTuple(args, "l", &n)){ return NULL; }
    
    uint a = wilson(n);
    
    return Py_BuildValue("l", a);
}

static PyObject* runIsPrimeWilson(PyObject *self, PyObject *args){
    uint n;
    
    if(!PyArg_ParseTuple(args, "l", &n)){ return NULL; }
    
    return Py_BuildValue("l", isPrimeWilson(n));
}

static PyObject* runWillans(PyObject *self, PyObject *args){
    d_type n;

    if(!PyArg_ParseTuple(args, "l", &n)){ return NULL; }
    
    return Py_BuildValue("l", willans(n));
}

static PyObject* runAckermann(PyObject *self, PyObject *args){
    uint m, n;

    if(!PyArg_ParseTuple(args, "KK", &m, &n)){ return NULL; }
    
    return Py_BuildValue("K", Ackermann(m, n));
}

static PyObject* runAckermannLookup(PyObject *self, PyObject *args){
    uint m, n;

    if(!PyArg_ParseTuple(args, "KK", &m, &n)){ return NULL; }
    
    return Py_BuildValue("K", AckermannLookup(m, n));
}

static PyObject* checkIsSorted(PyObject *self, PyObject *args){
    PyObject* seq;
    d_type prev, i, seqlen = 0;

    if(!PyArg_ParseTuple(args, "O", &seq)){ return NULL; }

    seq = PySequence_Fast(seq, "argument must be iterable");
    if(!seq){ return NULL; }

    seqlen = PySequence_Fast_GET_SIZE(seq);

    prev = PyLong_AsLong(PyNumber_Long(PySequence_Fast_GET_ITEM(seq, 0)));

    for(i = 1; i < seqlen; i++) {
        d_type val = PyLong_AsLong(PyNumber_Long(PySequence_Fast_GET_ITEM(seq, i)));
        if(prev > val){ Py_RETURN_FALSE; }
        prev = val;
    }

    Py_RETURN_TRUE;
}

static PyMethodDef arctan_methods[] = {
    { "arctan", arctan, METH_VARARGS, "Give arctan" },
    { "arctan2", arctan2, METH_VARARGS, "Give arctan" },
    { "gamma", gamma_fun, METH_VARARGS, "returns gamma" },
    { "pi", pi, METH_NOARGS, "Returns PI" },
    { "bubblesort", bubblesort, METH_VARARGS, "Sorts array" },
    { "bubblesort2", bubblesort2, METH_VARARGS, "Sorts array" },
    { "mergesort", merge_sort, METH_VARARGS, "Sorts array" },
    
    #ifdef _POSIX_VERSION
    { "p_mergesort", parallel_merge_sort, METH_VARARGS, "Sorts array" },
    { "p_quicksort", p_quick_sort, METH_VARARGS, "Sorts array" },
    { "p_primes", p_primes, METH_VARARGS, "Checks if prime" },
    #endif
    
    { "insertionsort", insert_sort, METH_VARARGS, "Sorts array" },
    { "quicksort", quick_sort, METH_VARARGS, "Sorts array" },
    { "bucketsort", bucket_sort, METH_VARARGS, "Sorts array" },
    { "pass_arr", pass_arr, METH_VARARGS, "Passes array" },
    { "isPrime", is_prime, METH_VARARGS, "Checks if prime" },
    { "primes", primes, METH_VARARGS, "Checks if prime" },
    { "makeArrMin", makeArr, METH_VARARGS, "Makes an array of random values" },
    { "makeArrMinRandom", makeArr, METH_VARARGS, "Makes an array of random values" },
    { "makeArrSequential", makeArrSequential, METH_VARARGS, "Makes an array of sequential values" },
    { "makeArrZeros", makeArrZeros, METH_VARARGS, "Makes an array of zeros" },
    { "isSorted", checkIsSorted, METH_VARARGS, "Checks if array is sorted" },
    { "Ackermann", runAckermann, METH_VARARGS, "Ackermann Function" },
    { "AckermannLookup", runAckermannLookup, METH_VARARGS, "Ackermann Function w/ Look Up Table" },
    { "Chudnovsky", runChudnovsky, METH_VARARGS, "Chudnovsky Algorithm" },
    { "wilson", runWilson, METH_VARARGS, "Wilson Algorithm" },
    { "isPrimeWilson", runIsPrimeWilson, METH_VARARGS, "Wilson Theorem" },
    { "willans", runWillans, METH_VARARGS, "Willans Formula" },
    { NULL, NULL, 0, NULL }
};

static struct PyModuleDef arctanmodule = {
    PyModuleDef_HEAD_INIT,
    "arctan_module",
    "A Python module that computes arctan(x)",
    -1,
    arctan_methods
};

PyMODINIT_FUNC PyInit_arctan(void){
    // PyObject *m;
    // Py_Initialize();
    return PyModule_Create(&arctanmodule);
}
