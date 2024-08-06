document.addEventListener('DOMContentLoaded', function () {
    var dragDropArea = document.getElementById('drag-drop-area');
    var uploadButton = document.getElementById('upload-button');
    var selectedFile;

    // Drag and drop event listeners
    dragDropArea.addEventListener('dragover', function (e) {
        e.preventDefault();
        e.stopPropagation();
        dragDropArea.classList.add('dragging');
    });

    dragDropArea.addEventListener('dragleave', function (e) {
        e.preventDefault();
        e.stopPropagation();
        dragDropArea.classList.remove('dragging');
    });

    dragDropArea.addEventListener('drop', function (e) {
        e.preventDefault();
        e.stopPropagation();
        dragDropArea.classList.remove('dragging');
        selectedFile = e.dataTransfer.files[0];
        dragDropArea.innerHTML = selectedFile.name;
    });

    dragDropArea.addEventListener('click', function () {
        var fileInput = document.createElement('input');
        fileInput.type = 'file';
        fileInput.accept = 'image/*';
        fileInput.onchange = function (e) {
            selectedFile = e.target.files[0];
            dragDropArea.innerHTML = selectedFile.name;
        };
        fileInput.click();
    });

    // Upload button click event
    uploadButton.addEventListener('click', function () {
        if (!selectedFile) {
            alert('Por favor, selecciona una imagen primero.');
            return;
        }

        var formData = new FormData();
        formData.append('file', selectedFile);  // Asegúrate de que el nombre del campo sea 'file'

        fetch('https://backend-1-gaka.onrender.com:10000/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.processed_image_url) {
                alert('Imagen subida con éxito');
                console.log(data);
                // Mostrar la imagen procesada al usuario
                var imgElement = document.createElement('img');
                imgElement.src = data.processed_image_url;
                imgElement.alt = 'Imagen procesada';
                document.body.appendChild(imgElement);  // Añadir la imagen al final del body
            } else {
                alert('Error procesando la imagen');
            }
        })
        .catch(error => {
            console.log(error);
        });
    });
});
