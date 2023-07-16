let ipValue;
fetch('https://api.ipify.org?format=json').then(response => response.json()).then(data => { 
  ipValue = data.ip; 
  let ipAddress = `<tr><td>IP Address</td><td>${ipValue}</td></tr>`;
  dataHTML = ipAddress + dataHTML;
});