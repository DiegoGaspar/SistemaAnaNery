$(function slide(){
    $('#slide img:eq(0)').show(2000,function(){
        window.setTimeout(function(){
            $('#slide img:eq(0)').fadeOut(3000,function(){
                $('#slide img:eq(1)').show(2000,function(){
                    window.setTimeout(function(){
                        $('#slide img:eq(1)').fadeOut(3000, function(){
                            $('#slide img:eq(2)').show(2000, function(){
                                window.setTimeout(function(){
                                    $('#slide img:eq(2)').fadeOut(3000, function(){
                                        $('#slide img:eq(3)').show(2000, function(){
                                            window.setTimeout(function(){
                                                $('#slide img:eq(3)').fadeOut(3000, function(){
                                                    $('#slide img:eq(4)').show(2000, function(){
                                                        window.setTimeout(function(){
                                                            $('#slide img:eq(4)').fadeOut(3000);
                                                        });
                                                    });
                                                });
                                            });
                                        });
                                    });
                                });
                            });
                        });
                    });
                });
            });
        });
    });
    setInterval(slide,25000);
});
