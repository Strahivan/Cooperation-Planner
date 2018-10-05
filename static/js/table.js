$(document).ready(function(){
   $('#table_with_pagination').DataTable({
        "pagingType": "full",
        "searching": false
   });
   $('.dataTables_length').addClass('bs-select');
});