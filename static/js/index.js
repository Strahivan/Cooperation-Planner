$(document).ready(function(){

    $('.loading').removeClass( "d-none" )
    $(".data_table").load("/data", function(response, status, xhr) {
         $('.loading').addClass( "d-none" );
         if ( status == "error" ) {
            alert('Fehler beim Aufbau der Datenbankverbindung');
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
                        alert('Fehler beim Laden der Datenbank');
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
                    alert('Fehler beim Laden der Datenbank');
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
            alert('Fehler beim Exportieren der CSV-Datei!');
        });
    });

    $('.btn-delete').click(function(){
         $('.loading').removeClass( "d-none" )
         $.get( "/delete_db", function(){
                $(".data_table").load("/data", function(response, status, xhr) {
                    $('.loading').addClass( "d-none" );
                    if ( status == "error" ) {
                        alert('Fehler beim L�schen der Datenbank');
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
                    alert('�berpr�fen Sie die Struktur ihrer CSV-Datei');
            }
       });
    });
});
