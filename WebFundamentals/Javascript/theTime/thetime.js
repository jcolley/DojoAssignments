var HOUR = 7;
var MINUTE = 15;
var PERIOD = "PM";

function getTimeOfDayMsg(){
    var timeOfDay = "";
    if(PERIOD === "AM"){
        timeOfDay = "in the morning.";
    }else if (PERIOD === "PM"){
        timeOfDay = "in the evening.";
    }else {
        timeOfDay = "ERR: PERIOD can only be AM or PM";
    }
    return timeOfDay;
}

function getTimeAfterHourMsg(){
    var timeAfterHour = "";
    if(MINUTE < 30){
        timeAfterHour = "just after";
    }else if(MINUTE > 30){
        timeAfterHour = "almost"
        if(HOUR < 12){
            HOUR++;
        }else if(HOUR === 12){
            HOUR = 1;
        }
    }
    return timeAfterHour;
}

console.log("It's",getTimeAfterHourMsg(),HOUR,getTimeOfDayMsg());