// static/js/scripts.js
function pingIP() {
    var ip = document.getElementById('ipInput').value;
    // Aquí puedes agregar la lógica para realizar el ping
    // Por ahora, simplemente mostramos la IP
    document.getElementById('pingResult').innerText = "Pinging IP: " + ip;
}
function traceIP() {
    var ip = document.getElementById('ipInput').value;
    // Aquí puedes agregar la lógica para realizar el ping
    // Por ahora, simplemente mostramos la IP
    document.getElementById('pingResult').innerText = "trace IP: " + ip;
}