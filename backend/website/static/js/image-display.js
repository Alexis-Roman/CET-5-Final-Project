document.getElementById('imageForm1').addEventListener('click', function() {
    document.getElementById('imageUpload1').click();
});

document.getElementById('imageUpload1').addEventListener('change', function() {
    var uploadedImage = document.getElementById('uploadedImage1');
    var uploadLabel = document.getElementById('uploadLabel1');
    var imageIcon = document.getElementById('imageIcon');
    var fileInput = document.getElementById('imageUpload1');
    var file = fileInput.files[0];
    var reader = new FileReader();

    reader.onload = function(e) {
        uploadedImage.src = e.target.result;
        uploadedImage.style.display = 'block';
        uploadLabel.style.display = 'none';
        imageIcon.style.display = 'none';
    };

    reader.readAsDataURL(file);
});

document.getElementById('uploadedImage1').addEventListener('click', function() {
    document.getElementById('imageUpload1').click();
});