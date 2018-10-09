$(document).ready(function(){
    $(".data_table").load("/data");

    $('#saveFilter').click(function(){
        var $filterPanel = $('#filterFieldSet'),
            $reach = $filterPanel.find('#reach'),
            $url = $filterPanel.find('#url'),
            $statuscode = $filterPanel.find('#statuscode'),
            $tld = $filterPanel.find('#tld'),
            $globalrank = $filterPanel.find('#globalrank');
            $(".data_table").load("/filter?reach="+ $reach.val() + '&url=' + $url.val() +
                    '&statuscode=' + $statuscode.val() + '&tld=' + $tld.val() + '&globalrank=' + $globalrank.val());
    });

    $('#resetFilter').click(function(){
        var $filterPanel = $('#filterFieldSet');
            $filterPanel.find('input').val('');
            $(".data_table").load("/filter?globalrank=&url=&statuscode=&tld=&reach=");
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
        });
    });

    $('.btn-delete').click(function(){
         $.get( "/delete_db", function(){
                $(".data_table").load("/data");
         });
    });


    const form = document.querySelector('form');
    form.addEventListener('submit', e => {

        e.preventDefault();
        var formData = new FormData($('#upload-file')[0]);

        $.ajax({
            method: 'POST',
            url: '/upload_file',
            data: formData,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                $(".data_table").load("/data");
        }
       });
    });
});
