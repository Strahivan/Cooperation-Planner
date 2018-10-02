$(document).ready(function(){
    $('.filterable .btn-open-filter').click(function(){
        var $panel = $(this).parents('.filterable'),
        $filters = $panel.find('.data_table .filters input'),
        $t_body = $panel.find('.data_table .table tbody'),
        $create_filter = $panel.find('.btn-create-filter');
        if ($filters.prop('disabled') == true) {
            $filters.prop('disabled', false);
            $create_filter.prop('disabled', false)
            $filters.first().focus();
        } else {
            $filters.val('').prop('disabled', true);
            $create_filter.prop('disabled', true)
            $t_body.find('.no-result').remove();
            $t_body.find('tr').show();
        }
    });

    $('.filterable .btn-create-filter').click(function(){
        var $panel = $(this).parents('.filterable'),
            $create_filter = $panel.find('.btn-create-filter');
            $status = $panel.find('#status'),
            $url = $panel.find('#url'),
            $statuscode = $panel.find('#statuscode'),
            $tld = $panel.find('#tld'),
            $inLink = $panel.find('#inLink');
            $create_filter.prop('disabled', true)
            $(".data_table").load("/filter?status="+ $status.val() + '&url=' + $url.val() +
                    '&statuscode=' + $statuscode.val() + '&tld=' + $tld.val() + '&inLink=' + $inLink.val());
    });
});
