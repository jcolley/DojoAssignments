$(document).ready(function(){
    generateNinja();
    revealNinja();
});

$(document).on("click",".ninja", function(){
    $(this).slideUp("fast");
    if($(".ninja:visible").length === 1){
        resetNinja();
    }
});

function generateNinja(){
    destroyNinja();
    for(var i=1;i<=8;i++){
        $(".template").clone().appendTo("#container");
        $("#container .template").addClass("ninja");
        $("#container .ninja").removeClass("template");
        if(i%4 === 0){
            $(".ninja").last().after("<br>");
        }
    }
}

function destroyNinja(){
    $(".ninja").remove();
    $("br").remove();
}

function revealNinja(){
    $(".ninja").fadeTo(2000, 1.0,function(){
        if ($(this).is(':visible')){
            $(this).css('display','inline-block');
        }
    });
    $(".ninja").removeClass("hidden");
}

function resetNinja(){
    generateNinja();
    revealNinja();
}

$("footer button").click(function(){
    resetNinja();
});