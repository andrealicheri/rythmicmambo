const xhr = new XMLHttpRequest();
xhr.open('POST', '/backend/sendData/NAMEVARIABLE');
xhr.setRequestHeader('Content-Type', 'text/html');
xhr.send(dataHTML);