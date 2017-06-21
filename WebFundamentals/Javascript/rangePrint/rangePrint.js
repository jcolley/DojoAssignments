function printRange(start,stop,skip){
    for(var val=start;val<stop-1;val+=skip){
        console.log(val);
    }
}

printRange(2,10,2);