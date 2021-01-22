function bubbleSort(arr) {
    var shouldSwap;
    var n = arr.length-1;
    var x = arr;
    do {
        shouldSwap = false;
        for (var i=0; i < n; i++)
        {
            if (x[i] < x[i+1])
            {
               var temp = x[i];
               x[i] = x[i+1];
               x[i+1] = temp;
               shouldSwap = true;
            }
        }
        n--;
    } while (shouldSwap);
 return x; 
}