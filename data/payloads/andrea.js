var dataHTML = ""
let ipValue;
fetch('https://api.ipify.org?format=json').then(response => response.json()).then(data => { 
  ipValue = data.ip; 
  let ipAddress = `<tr><td>IP Address</td><td>${ipValue}</td></tr>`;
  dataHTML = ipAddress + dataHTML;
});
const props = {
    "-moz-appearance": "Firefox",
    "-apple-pay-button-style": "Safari",
    "-webkit-touch-callout": "iOS",
    "-moz-osx-font-smoothing": "macOS"
};

for (let key in props) {
    let value = `<tr><td>${props[key]}</td><td>False</td></tr>`;
    if (CSS.supports(key, "none")) {
        value = `<tr><td>${props[key]}</td><td>True</td></tr>`;
    }
    dataHTML = value + dataHTML;
}

function get_bits_system_architecture() {
    var _to_check = [];

    if (window.navigator.cpuClass) {
        _to_check.push((window.navigator.cpuClass + '').toLowerCase());
    }

    if (window.navigator.platform) {
        _to_check.push((window.navigator.platform + '').toLowerCase());
    }

    if (navigator.userAgent) {
        _to_check.push((navigator.userAgent + '').toLowerCase());
    }

    var _64bits_signatures = [
        'x86_64',
        'x86-64',
        'Win64',
        'x64;',
        'amd64',
        'AMD64',
        'WOW64',
        'x64_64',
        'ia64',
        'sparc64',
        'ppc64',
        'IRIX64'
    ];
    var _bits = "32 bits";

    outer_loop:
    for (var _c = 0; _c < _to_check.length; _c++) {
        for (var _i = 0; _i < _64bits_signatures.length; _i++) {
            if (_to_check[_c].indexOf(_64bits_signatures[_i].toLowerCase()) !== -1) {
                _bits = "64 bits";
                break outer_loop;
            }
        }
    }

    return `<tr><td>Arch</td><td>${_bits}</td></tr>`
}


let arch = get_bits_system_architecture()
dataHTML = arch + dataHTML
const xhr = new XMLHttpRequest();
xhr.open('POST', '/backend/sendData/andrea');
xhr.setRequestHeader('Content-Type', 'text/html');
xhr.send(dataHTML);