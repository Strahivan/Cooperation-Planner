$(document).ready(function(){

    $('.loading').removeClass( "d-none" )
    $(".data_table").load("/data", function(response, status, xhr) {
         $('.loading').addClass( "d-none" );
         if ( status == "error" ) {
            alert('Fehler beim laden der CSV Datei!');
         }
     });

    $('#saveFilter').click(function(){
    $('.loading').removeClass( "d-none" )
        var $filterPanel = $('#filterFieldSet'),
            $reach = $filterPanel.find('#reach'),
            $url = $filterPanel.find('#url'),
            $statuscode = $filterPanel.find('#statuscode'),
            $tld = $filterPanel.find('#tld'),
            $globalrank = $filterPanel.find('#globalrank');
            $(".data_table").load("/filter?reach="+ $reach.val() + '&url=' + $url.val() +
                    '&statuscode=' + $statuscode.val() + '&tld=' + $tld.val() + '&globalrank=' + $globalrank.val(),
                function(response, status, xhr) {
                    $('.loading').addClass( "d-none" );
                    if ( status == "error" ) {
                        alert('Fehler beim laden der CSV Datei!');
                    }
            });
    });

    $('#resetFilter').click(function(){
        $('.loading').removeClass( "d-none" )
        var $filterPanel = $('#filterFieldSet');
            $filterPanel.find('input').val('');
            $(".data_table").load("/filter?globalrank=&url=&statuscode=&tld=&reach=", function(response, status, xhr) {
                $('.loading').addClass( "d-none" );
                if ( status == "error" ) {
                    alert('Fehler beim laden der CSV Datei!');
                }
            });
    });

    $('.btn-csv').click(function(){
        var $filterPanel = $('#filterFieldSet'),
            $reach = $filterPanel.find('#reach'),
            $url = $filterPanel.find('#url'),
            $statuscode = $filterPanel.find('#statuscode'),
            $tld = $filterPanel.find('#tld'),
            $globalrank = $filterPanel.find('#globalrank');

        $.get( "/generate_csv?reach="+ $reach.val() + '&url=' + $url.val() +
             '&statuscode=' + $statuscode.val() + '&tld=' + $tld.val() + '&globalrank=' + $globalrank.val(), function( csv ) {
         var $a = $('<a />', {
              'href': 'data:text/csv;charset=utf-8,' + encodeURI(csv),
              'download': 'plot.csv',
              'text': "click"
            }).hide().appendTo("body")[0].click();
        }).fail(function() {
            alert('Fehler beim laden der CSV Datei!');
        });
    });

    $('.btn-delete').click(function(){
         $('.loading').removeClass( "d-none" )
         $.get( "/delete_db", function(){
                $(".data_table").load("/data", function(response, status, xhr) {
                    $('.loading').addClass( "d-none" );
                    if ( status == "error" ) {
                        alert('Fehler beim laden der CSV Datei!');
                    }
            });
         });
    });


    const form = document.querySelector('form');
    form.addEventListener('submit', e => {
        e.preventDefault();
        var formData = new FormData($('#upload-file')[0]);
        $('.loading').removeClass( "d-none" )
        $.ajax({
            method: 'POST',
            url: '/upload_file',
            data: formData,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                $(".data_table").load("/data", function() {
                    $('.loading').addClass( "d-none" );
                });
            },
            error: function(msg){
                $('.loading').addClass( "d-none" );
                    alert('Fehler beim laden der CSV Datei!');
            }
       });
    });
});
