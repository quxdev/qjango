function getHeightAndWidth(element) {
  let w = element.clientWidth;
  let h = screen.height;

  // Resize height to be a square if and only if the aspect ratio indicates
  // that the device is not a mobile phone
  if (w < 768) {
    if (h > w * 3) {
      h = w;
    }
  } else {
    h = w < 1200 ? w * 0.50 : 640;
  }
  return { width: w, height: h };
}

function resizeCover() {
  let div = document.getElementById("above-the-fold");
  let xyz = document.getElementById("xyz");
  if (xyz == null) {
    return;
  }
  let abc = xyz
    .getElementsByClassName("container-xl")[0]
    .getElementsByClassName("d-flex")[0];

  let size = getHeightAndWidth(div);
  let h = size.height;
  div.style.minHeight = h + "px";
  xyz.style.minHeight = h + "px";
  abc.style.minHeight = (h - 80) + "px";
}

function resizeSplash() {
  let div = document.getElementById("splash");
  let size = getHeightAndWidth(div);
  div.style.minHeight = size.height + "px";
}

document.addEventListener("DOMContentLoaded", function () {
  resizeCover();
  resizeSplash();
  window.onresize = function () {
    resizeCover();
    resizeSplash();
  }
});
