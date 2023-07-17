if (navigator.pdfViewerEnabled) { pdfValue = "True" } else { pdfValue = "False" }
let pdf = `<tr><td>PDF</td><td>${pdfValue}</td></tr>` // PDF Viewer
dataHTML = pdf + dataHTML