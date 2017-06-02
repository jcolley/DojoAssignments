function collectThemAll(){
    for(var i=1;i<=151;i++){
        var curimg = "http://pokeapi.co/media/img/"+i+".png";
        $(".poke").clone().appendTo("#container");
        $("#container .poke").addClass("poke"+i);
        $("#container .poke").removeClass("poke");
        $(".poke"+i).attr("src", curimg);
        if(i%9 === 0){
            $(".poke"+i).last().after("<br>");
        }
    }
}

collectThemAll();