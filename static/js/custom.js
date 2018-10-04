$(document).ready(function(){
    $(".data_table").load("/data", function() {
        $('#table_with_pagination').DataTable({
            "pagingType": "simple"
        });
        $('.dataTables_length').addClass('bs-select');
    });

    $("#search_table").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#table_body tr").filter(function() {
          $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
      });

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
        var $filterPanel = $('#filterModal'),
            $status = $filterPanel.find('#status'),
            $url = $filterPanel.find('#url'),
            $statuscode = $filterPanel.find('#statuscode'),
            $tld = $filterPanel.find('#tld'),
            $inLink = $filterPanel.find('#inLink');

        $.get( "/generate_csv?status="+ $status.val() + '&url=' + $url.val() +
             '&statuscode=' + $statuscode.val() + '&tld=' + $tld.val() + '&inLink=' + $inLink.val(), function( csv ) {
         var $a = $('<a />', {
              'href': 'data:text/csv;charset=utf-8,' + encodeURI(csv),
              'download': 'plot.csv',
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
