var lastTarget = null;
function isFile(evt) {
    var dt = evt.dataTransfer;

    for (var i = 0; i < dt.types.length; i++) {
        if (dt.types[i] === "Files") {
            return true;
        }
    }
    return false;
}

window.addEventListener("dragenter", function (e) {
    if (isFile(e)) {
        lastTarget = e.target;
        document.querySelector("#dropzone").style.visibility = "";
        document.querySelector("#dropzone").style.opacity = 1;
        document.querySelector("#textnode").style.fontSize = "48px";
    }
});

window.addEventListener("dragleave", function (e) {
    e.preventDefault();
    if (e.target === document || e.target === lastTarget) {
        document.querySelector("#dropzone").style.visibility = "hidden";
        document.querySelector("#dropzone").style.opacity = 0;
        document.querySelector("#textnode").style.fontSize = "42px";
    }
});

window.addEventListener("dragover", function (e) {
    e.preventDefault();
});

window.addEventListener("drop", function (e) {
    e.preventDefault();
    document.querySelector("#dropzone").style.visibility = "hidden";
    document.querySelector("#dropzone").style.opacity = 0;
    document.querySelector("#textnode").style.fontSize = "42px";
    if(e.dataTransfer.files && e.dataTransfer.files[0])
    {
        loadImage(e.dataTransfer.files[0]);
        
    }
});
window.addEventListener('load', function() {
    document.querySelector('input[type="file"]').addEventListener('change', function() {
        if (this.files && this.files[0]) {
            loadImage(this.files[0]);
        }
    });
  });