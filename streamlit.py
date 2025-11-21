<html>
  <head>
    <script src="https://aframe.io/releases/1.4.2/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <a-box position="0 1 -3" rotation="0 45 0" color="#4CC3D9" 
             animation="property: rotation; to: 0 405 0; loop: true; dur: 5000"></a-box>
      <a-sphere position="2 1.25 -5" radius="1.25" color="#EF2D5E"></a-sphere>
      <a-cylinder position="-1 0.75 -3" radius="0.5" height="1.5" color="#FFC65D"></a-cylinder>
      <a-plane rotation="-90 0 0" width="10" height="10" color="#7BC8A4"></a-plane>
      <a-sky color="#ECECEC"></a-sky>
    </a-scene>
  </body>
</html>
