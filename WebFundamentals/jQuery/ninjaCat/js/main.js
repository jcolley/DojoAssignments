$("img").click(function(){
    var newimg = $(this).attr("cat");
    var oldimg = $(this).attr("src");
    $(this).attr("cat",oldimg);
    $(this).attr("src",newimg);
    if($(this).attr("src").indexOf("ninja")){
        $(this).attr("alt", "ninja"+i)
    }else{
        $(this).attr("alt", "cat"+i)
    }
});