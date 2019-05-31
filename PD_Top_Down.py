

# public static int cutRod(int arr[],int n,Integer memo[]){
#     if(n<=0)
#     return 0;
#     int max=Integer.MIN_VALUE;
#     if(memo[n]!=null)
#     return memo[n];
#     else{
#         for(int i=0;i<n;i++)
#         {
#             max=Math.max(max,arr[i]+cutRod(arr,n-i-1,memo));
#         }
#         memo[n]=max;
#         return memo[n];
#     }
# }

def cut(arr[], n , memo[]):
    if n <= 0:
        return 0
        max= MIN_VALUE
        if memo[n] != null:
            return memo[n]
        else:
            i = 0
            for i < n :
                i++
                max = Math.max(max, arr[i]+ cut(arr, n-i-1, memo))
            memo[n] = max    
            return memo[n]