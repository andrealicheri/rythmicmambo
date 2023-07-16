function getTimezone() {
    const DateTimeFormat = window.Intl?.DateTimeFormat;
    if (DateTimeFormat) {
        const timezone = new DateTimeFormat().resolvedOptions().timeZone;
        if (timezone) {
            return timezone;
        }
    }

    return `UTC${offset >= 0 ? '+' : ''}${Math.abs(offset)}`;
}

let timezone = `<tr><td>Timezone</td><td>${getTimezone()}</td></tr>`
dataHTML = timezone + dataHTML