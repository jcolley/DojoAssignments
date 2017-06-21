var start = -2;
var end = 10;
var skip = 2;

function printRange(start,end,skip){
    if(start<0){
        if(end<0){
            for(var i=start;i<end;i+=skip){
                console.log(i);
            }
        }else{
            return "Error: End cannot be reached with those values!"
        }
    }else{
        if(end>0){
            for(var i=start;i<end;i+=skip){
                console.log(i);
            }
        }else{
            return "Error: End cannot be reached with those values!"
        }
    }
}

printRange(start,end,skip);