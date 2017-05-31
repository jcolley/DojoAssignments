function bdayCountdown(daysLeft){
    var sadMsg = "days until my birthday. Such a long time... :(";
    var excMsg = "DAYS UNTIL MY BIRTHDAY!!!";
    var scream1 = "♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪ღ♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•*";
    var scream2 = "♪ღ♪░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░░♪ღ♪";
    var scream3 = "*•♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•«";

    while(daysLeft){
        if(daysLeft>=30){
            console.log(daysLeft,sadMsg);
        } else if(daysLeft<30){
            console.log(daysLeft,excMsg);
        }
        daysLeft--;
    }
    console.log(scream1);
    console.log(scream2);
    console.log(scream3);
}

bdayCountdown(60);