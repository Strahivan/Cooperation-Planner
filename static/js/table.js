$(document).ready(function(){
   $('#table_with_pagination').DataTable({
        "searching": false,
        "initComplete": function(settings, json) {
            $('.loading').addClass( "d-none" );
        }
   });
   $('.dataTables_length').addClass('bs-select');
});