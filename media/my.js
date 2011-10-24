$(function() {
    var s = 0;
    var l = 0;
    
    $('#selMark').hide();
    $('#newStud').hide();
    $('.del').css({'opacity': '0.2'});

    $('#mark td.mark').each(function() {
        var VRegExp = '/\s/g';
        var m = $(this).html();
        m = m.replace(VRegExp, '');
        //alert(">" + m + "<");
        if (m == '5') {
            $(this).css({'color': 'red'});
        }
    });

    // клик по ячейке с оценкой
    $('td.mark').click(function() {
        
        s = $(this).attr('s');
        l = $(this).attr('l');
        
        // подсветка лабораторной работы
        labElem = '#' + l;
        $('#labs tr').css({'background-color': '#FFF'});
        $(labElem).css({'background-color': '#9CF'});

        // подсветка фамилии студента
        studElem = '#stud_' + s;
        $('#mark td.name').css({'background-color': '#FFF'});
        $(studElem).css({'background-color': '#9CF'});


        // выделяем новую ячейку
        //$('td.mark').css({'background-color': '#FFF'});
        //$(this).css({'background-color': '#9F9'});

        // перемещаем блок с оценками
        $('#selMark').show();
        $(this).offset(function(i, v) {
            $('#selMark').animate({'top': v.top + 0, 'left': v.left + 0}, 150);
        });
    });
    
    // закрыть окно с оценками
    $('#selMark .close a').click(function() {
        $('#selMark').hide();
    });
    
    // закрыть окно с формой.. студента
    $('#newStud .close a').click(function() {
        $('#newStud').hide();
    });
    
    // клик по оценке
    $('#selMark a').click(function() {
        id = '#' + s + '_' + l;
        $.post(
            "/put/",
            {'stud': s, 'lab': l, 'mark': $(this).attr('mark')},
            function(data) {
                $(id).html(data);
                $('#selMark').hide();
            }
        );
    });

    $('#mark td.mark').mousemove(function() {
        $(this).css({'background-color': '#5D5'});
        $('#selMark').hide();      
    });
    
    $('#mark td.mark').mouseout(function() {
        $(this).css({'background-color': '#FFF'});
    });

    $('.del').mousemove(function() {
        $(this).css({'opacity': '1'});
    });

    $('.del').mouseout(function() {
        $(this).css({'opacity': '0.2'});
    });

    $('.del').click(function() {
        var stud_id = $(this).attr('stud_id');
        var x = '#st_' + stud_id;
        $.get(
            "/students/del/" + stud_id + "/",
            {},
            function(data) {
                if (data == "OK") {
                    $(x).remove();
                }
            }
        );
    });

    $('#add_stud').click(function() {
        $('#newStud').show();
        $(this).offset(function(i, v) {
            $('#newStud').animate({'top': v.top + 20, 'left': v.left + 20}, 1);
        });
    });

    // добавление студента
    $('#newStud .add').click(function() {
        var l_name = $('#newStud input[name=l_name]').attr('value');
        var f_name = $('#newStud input[name=f_name]').attr('value');
        var s_name = $('#newStud input[name=s_name]').attr('value');
        $.post(
            "/students/add/",
            {'f_name': f_name, 'l_name': l_name, 's_name': s_name},
            function(data) {
                if (data == "OK") {
                    //$('tr:last').append("<tr><td colspan='10'></td></tr>");
                }
            });
    });

});