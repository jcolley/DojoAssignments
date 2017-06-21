$(document).ready(function(){

    var curURL = window.location.href

    if(curURL.includes('success')){
        set("title", "Success!");
        set("#container", "<h1>Successful Body</h1>");
    }else{
        set("title", "Hello World");
        set("#container", "<h1>Hello World</h1>");
    }
});

function set(element, value){
    $(element).html(value);
    console.log("Set "+toString(element)+" to "+ toString(value));
}