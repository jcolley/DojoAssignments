var counter = 0;
var filters = ["hue-rotate(45deg)"
              , "hue-rotate(90deg)"
              , "hue-rotate(180deg)"
              , "hue-rotate(225deg)"
              ,"hue-rotate(270deg)"
              , "hue-rotate(315deg)"
              , "hue-rotate(0deg)"];

var div = $('#coloredDiv');
var interval;



$("#click button").click(function () {
    $("#logo").toggleClass("colorcycle");
    interval = window.setInterval(changeFilter, 286);
});

function changeFilter() {
    var filter = filters.shift();
    filters.push(filter);
    $(".colorcycle").css({
        '-webkit-filter': filter,
        'filter': filter
    });
}

$("#hide button").click(function(){
    $("#logo").hide();
});

$("#show button").click(function(){
    $("#logo").show();
});

$("#toggle button").click(function(){
    $("#logo").toggle();
});

$("#slideDown button").click(function(){
    $("#logo").slideDown("slow");
});

$("#slideUp button").click(function(){
    $("#logo").slideUp("slow");
});

$("#slideToggle button").click(function(){
    $("#logo").slideToggle("slow");
});

$("#fadeOut button").click(function(){
    $("#logo").fadeOut("slow");
});

$("#fadeIn button").click(function(){
    $("#logo").fadeIn("slow");
});

$("#addClass button").click(function(){
    $("#logo").addClass("class");
});

$("#before button").click(function(){
    $("#before button").before($('<img class="before" src="images/before.png" alt="hand pointing left">'));
});

$("#after button").click(function(){
    $("#after button").after($('<img class="after" src="images/after.png" alt="hand pointing right">'));
});

$("#append button").click(function(){
    $("#append button").append($('<br><img class="append" src="images/deadlink.png" alt="a dead Link">'));
});

$("#html button").click(function(){
    $("#html button").html($('<br><h3>HTML ADDED!</h3>'));
});

$("#attr button").click(function(){
    alert($("#attr input").attr("checked"));
});

$("#val button").click(function(){
    alert("Value of the YEP! checkbox: "+$("#attr input").val());
});

$("#text button").click(function(){
    alert("The text of the next button is: "+$("#data button").text());
});

$("#data button").click(function(){
    
});