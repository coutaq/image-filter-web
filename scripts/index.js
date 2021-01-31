
function sendPost(content){
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'index.html', true);
    console.log(content);
    xhr.setRequestHeader('Content-type', content);
    xhr.onload = function () {
        console.log("succesfully sent post to server");
    };
    xhr.send('POST');
}

  function loadImage(image){
    if(!image.type.startsWith('image')){
        alert("Please upload an image!");
        return;
    }
    var img = document.querySelector('#image-center');  // $('img')[0]
    img.src = URL.createObjectURL(image); // set src to blob url
    img.onload = imageIsLoaded;
    var reader = new FileReader();
    reader.addEventListener("loadend", function() {
        let data = reader.result;
        console.log(data);
        sendPost(data);
     });
     reader.readAsDataURL(image);
  }
  function imageIsLoaded() { 
    document.querySelector('label').innerHTML = "upload again";
    document.querySelector('#filters').style.display = "block";
    
  }
  function getBase64Image(file) {
    var fr = new FileReader();
    fr.onload = function () {
        console.log(fr.result.toString());
    }
    fr.readAsBinaryString(file);
}
function _arrayBufferToBase64( buffer ) {
    var binary = '';
    var bytes = new Uint8Array( buffer );
    var len = bytes.byteLength;
    for (var i = 0; i < len; i++) {
        binary += String.fromCharCode( bytes[ i ] );
    }
    return window.btoa( binary );
}

function ArrayBufferToBinary(buffer) {
    var uint8 = new Uint8Array(buffer);
    return uint8.reduce((binary, uint8) => binary + uint8.toString(2), "");
}