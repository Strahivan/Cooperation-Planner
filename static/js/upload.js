const url = 'process.php';
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
            $("#data_table").load("/data");
    },
   });
});