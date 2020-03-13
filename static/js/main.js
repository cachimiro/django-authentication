// maps for main page 
function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
        center: {
            lat: 10.465295,
            lng: -75.501901
        }
    });

    var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    var locations = [
        { lat: 10.481924, lng: -75.490968 },
        
    ];

    var markers = locations.map(function(location, i) {
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
        });
    });

    var markerCluster = new MarkerClusterer(map, markers, { imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m' });
}

