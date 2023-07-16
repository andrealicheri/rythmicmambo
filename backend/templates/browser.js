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
