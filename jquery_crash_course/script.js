$(document).ready(function() {
    // hide
    $('#hide').click(function() {
        // $(this).hide();
        $('p').hide()
        $('h2').hide();
        $("#heading2").hide();
        $("#heading2").css("color", "green");
        $(".para").hide();
    });

    $("p").dblclick(function() {
        $(this).hide();
    });

    // show
    $("#show").click(function() {
        $('p').show()
        $('h2').show();
    });

    // fade
    $("#fadeid").click(function() {
        console.log('fadein');
        $('#heading2').fadeIn(3000);
    });

    $("#fadeout").click(function() {
        console.log('fadeout');
        $('#heading2').fadeOut(3000); 
    });


    $("#flip").click(function() {
        $("#panel").slideDown("slow");
      
    });

    $("#flipUp").click(function() {
        $("#panel").slideUp("slow");
    });

    $("#flipToggle").click(function() {
        $("#panel").slideToggle("slow");
    });

    $("#addItem").click(function() {
        $("ol").append("<li>New Append Item</li>")
    });

});