$(function() {
    $.ajax({
        url: '/right',
        success: function(data) {
            console.log('get info');
            $('#right').css("color", "black" );
        }
    });
});
