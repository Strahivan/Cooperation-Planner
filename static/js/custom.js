$(document).ready(function(){
    $(".data_table").load("/data");

    $('#saveFilter').click(function(){
        var $filterPanel = $('#filterModal'),
            $status = $filterPanel.find('#status'),
            $url = $filterPanel.find('#url'),
            $statuscode = $filterPanel.find('#statuscode'),
            $tld = $filterPanel.find('#tld'),
            $inLink = $filterPanel.find('#inLink');
            $(".data_table").load("/filter?status="+ $status.val() + '&url=' + $url.val() +
                    '&statuscode=' + $statuscode.val() + '&tld=' + $tld.val() + '&inLink=' + $inLink.val());
    });
    $('.btn-csv').click(function(){
        $.get( "/generate_csv", function( csv ) {
         var $a = $('<a />', {
              'href': 'data:text/csv;charset=utf-8,' + encodeURI(csv),
              'download': 'csv.csv',
              'text': "click"
            }).hide().appendTo("body")[0].click();
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
