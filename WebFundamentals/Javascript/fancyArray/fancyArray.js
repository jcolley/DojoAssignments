function fancyArray(arr,symbol,reversed){
    var sym = symbol || "->";
    var msg = "";
    var reversed = reversed || 0;
    if(!reversed){
        for(var i=0;i<arr.length;i++){
            msg = i+" "+sym+" "+arr[i];
            console.log(msg);
        }
    }else{
        for(var i=arr.length-1;i>=0;i--){
            msg = i+" "+sym+" "+arr[i];
            console.log(msg);
        }
    }
}

fancyArray(["James","Jill","Jane","Jack"],"==>",false);