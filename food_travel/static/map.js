
const map = L.map('map').setView([-24.782906266416592, -65.41105428100433], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(map);

async function fetchDestinations() {
    const response = await fetch('/coordenadas');
    const destinos = await response.json();
    console.log(destinos);
    destinos.forEach(destino => {
        L.marker([destino.ubicacion__latitud, destino.ubicacion__longitud]).addTo(map)
            .bindPopup(destino.nombre)
            .openPopup();
    });
}

let rutaControl = L.Routing.control({
    waypoints: [
        L.latLng(-24.79024564287792, -65.40210575687009),
        L.latLng(-24.78655448677337, -65.40486040064857),
        //...otros puntos
    ],
    routeWhileDragging: true
}).addTo(map);


document.getElementById('guardar-ruta').addEventListener('click', async () => {
    const waypoints = rutaControl.getWaypoints();
    const ruta = waypoints.map(wp => ({
        lat: wp.latLng.lat,
        lon: wp.latLng.lng
    }));

    const response = await fetch('/ruta/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(ruta)
    });

    if (response.ok) {
        console.log("Ruta guardada con éxito");
    } else {
        console.error("Error al guardar la ruta");
    }
});


fetchDestinations().catch(error => console.log(error));

