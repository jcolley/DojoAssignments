$(document).ready(function(){
    collectThemAll();
});

$(document).on("click", "img", function(){

    var dex = $(this).attr("dex");

    $.get("http://pokeapi.co/api/v1/pokemon/"+dex+"/",function(pokemon){
        var name = pokemon.name;
        var weight = pokemon.weight;
        var height = pokemon.height;
        var types = [];
        for(var i=0;i<pokemon.types.length;i++){
            types.push(pokemon.types[i].name);
        }

        $("#name").empty();
        $("#pokedex img").empty();
        $("#types").empty();
        $("#height").empty();
        $("#weight").empty();

        $("#name").text(name);
        $("#pokedex img").attr("src","http://pokeapi.co/media/img/"+dex+".png")
        $("#height").text(height);
        $("#weight").text(weight);
        $("#pokedex img").attr("alt",name);
        for(var i=0;i<types.length;i++){
            $("#pokedex ul").append("<li>"+types[i]+"</li>");
        }
    }, "JSON");
});

$(document).on({
    ajaxStart: function() {
         $("#pokedex img").attr("src","img/loading.gif");
    }
});

function collectThemAll(){
    for(var i=1;i<=151;i++){
        var curimg = "http://pokeapi.co/media/img/"+i+".png";
        $(".template").clone().appendTo("#pokejail");
        $("#pokejail .template img").attr("dex", i);
        $("#pokejail .template img").attr("src", curimg);
        $("#pokejail .poke").removeClass("template");

        if(i%6 === 0){
            $("#pokejail .poke").last().after("<br>");
        }
    }
}